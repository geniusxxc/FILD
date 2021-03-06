#include "hnswlib.hpp"

namespace hnswlib {

    	template<typename dist_t>
        BruteforceSearch<dist_t>::BruteforceSearch(SpaceInterface <dist_t> *s) {

        }

    	template<typename dist_t>
        BruteforceSearch<dist_t>::BruteforceSearch(SpaceInterface<dist_t> *s, const std::string &location) {
            loadIndex(location, s);
        }

    	template<typename dist_t>
        BruteforceSearch<dist_t>::BruteforceSearch(SpaceInterface <dist_t> *s, size_t maxElements) {
            maxelements_ = maxElements;
            data_size_ = s->get_data_size();
            fstdistfunc_ = s->get_dist_func();
            dist_func_param_ = s->get_dist_func_param();
            size_per_element_ = data_size_ + sizeof(labeltype);
            data_ = (char *) malloc(maxElements * size_per_element_);
            cur_element_count = 0;
        }

    	template<typename dist_t>
        BruteforceSearch<dist_t>::~BruteforceSearch() {
            free(data_);
        }


    	template<typename dist_t>
        void BruteforceSearch<dist_t>::addPoint(void *datapoint, labeltype label) {
            if(dict_external_to_internal.count(label))
                throw std::runtime_error("Ids have to be unique");


            if (cur_element_count >= maxelements_) {
                throw std::runtime_error("The number of elements exceeds the specified limit\n");
            };
            memcpy(data_ + size_per_element_ * cur_element_count + data_size_, &label, sizeof(labeltype));
            memcpy(data_ + size_per_element_ * cur_element_count, datapoint, data_size_);
            dict_external_to_internal[label]=cur_element_count;

            cur_element_count++;
        };

    	template<typename dist_t>
        void BruteforceSearch<dist_t>::removePoint(labeltype cur_external) {
            size_t cur_c=dict_external_to_internal[cur_external];

            dict_external_to_internal.erase(cur_external);

            labeltype label=*((labeltype*)(data_ + size_per_element_ * (cur_element_count-1) + data_size_));
            dict_external_to_internal[label]=cur_c;
            memcpy(data_ + size_per_element_ * cur_c,
                   data_ + size_per_element_ * (cur_element_count-1),
                   data_size_+sizeof(labeltype));
            cur_element_count--;

        }


    	template<typename dist_t>
        std::priority_queue<std::pair<dist_t, labeltype >> BruteforceSearch<dist_t>::searchKnn(const void *query_data, size_t k) const {
            std::priority_queue<std::pair<dist_t, labeltype >> topResults;
            for (int i = 0; i < k; i++) {
                dist_t dist = fstdistfunc_(query_data, data_ + size_per_element_ * i, dist_func_param_);
                topResults.push(std::pair<dist_t, labeltype>(dist, *((labeltype *) (data_ + size_per_element_ * i +
                                                                                    data_size_))));
            }
            dist_t lastdist = topResults.top().first;
            for (int i = k; i < cur_element_count; i++) {
                dist_t dist = fstdistfunc_(query_data, data_ + size_per_element_ * i, dist_func_param_);
                if (dist <= lastdist) {
                    topResults.push(std::pair<dist_t, labeltype>(dist, *((labeltype *) (data_ + size_per_element_ * i +
                                                                                        data_size_))));
                    if (topResults.size() > k)
                        topResults.pop();
                    lastdist = topResults.top().first;
                }

            }
            return topResults;
        };

    	template<typename dist_t>
        void BruteforceSearch<dist_t>::saveIndex(const std::string &location) {
            std::ofstream output(location, std::ios::binary);
            std::streampos position;

            writeBinaryPOD(output, maxelements_);
            writeBinaryPOD(output, size_per_element_);
            writeBinaryPOD(output, cur_element_count);

            output.write(data_, maxelements_ * size_per_element_);

            output.close();
        }

    	template<typename dist_t>
        void BruteforceSearch<dist_t>::loadIndex(const std::string &location, SpaceInterface<dist_t> *s) {


            std::ifstream input(location, std::ios::binary);
            std::streampos position;

            readBinaryPOD(input, maxelements_);
            readBinaryPOD(input, size_per_element_);
            readBinaryPOD(input, cur_element_count);

            data_size_ = s->get_data_size();
            fstdistfunc_ = s->get_dist_func();
            dist_func_param_ = s->get_dist_func_param();
            size_per_element_ = data_size_ + sizeof(labeltype);
            data_ = (char *) malloc(maxelements_ * size_per_element_);

            input.read(data_, maxelements_ * size_per_element_);

            input.close();

            return;
        }
}
