# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delf/protos/delf_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='delf/protos/delf_config.proto',
  package='delf.protos',
  syntax='proto2',
  serialized_pb=_b('\n\x1d\x64\x65lf/protos/delf_config.proto\x12\x0b\x64\x65lf.protos\"\x91\x01\n\x11\x44\x65lfPcaParameters\x12\x11\n\tmean_path\x18\x01 \x01(\t\x12\x1e\n\x16projection_matrix_path\x18\x02 \x01(\t\x12\x0f\n\x07pca_dim\x18\x03 \x01(\x05\x12\x1c\n\ruse_whitening\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x12pca_variances_path\x18\x05 \x01(\t\"\xd4\x01\n\x16\x44\x65lfLocalFeatureConfig\x12\x15\n\x07use_pca\x18\x01 \x01(\x08:\x04true\x12\x14\n\nlayer_name\x18\x02 \x01(\t:\x00\x12\x18\n\riou_threshold\x18\x03 \x01(\x02:\x01\x31\x12\x1d\n\x0fmax_feature_num\x18\x04 \x01(\x05:\x04\x31\x30\x30\x30\x12\x1c\n\x0fscore_threshold\x18\x05 \x01(\x02:\x03\x31\x30\x30\x12\x36\n\x0epca_parameters\x18\x06 \x01(\x0b\x32\x1e.delf.protos.DelfPcaParameters\"\xae\x01\n\nDelfConfig\x12\x12\n\nmodel_path\x18\x01 \x01(\t\x12\x14\n\x0cimage_scales\x18\x02 \x03(\x02\x12>\n\x11\x64\x65lf_local_config\x18\x03 \x01(\x0b\x32#.delf.protos.DelfLocalFeatureConfig\x12\x1a\n\x0emax_image_size\x18\x04 \x01(\x05:\x02-1\x12\x1a\n\x0emin_image_size\x18\x05 \x01(\x05:\x02-1')
)




_DELFPCAPARAMETERS = _descriptor.Descriptor(
  name='DelfPcaParameters',
  full_name='delf.protos.DelfPcaParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mean_path', full_name='delf.protos.DelfPcaParameters.mean_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='projection_matrix_path', full_name='delf.protos.DelfPcaParameters.projection_matrix_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pca_dim', full_name='delf.protos.DelfPcaParameters.pca_dim', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_whitening', full_name='delf.protos.DelfPcaParameters.use_whitening', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pca_variances_path', full_name='delf.protos.DelfPcaParameters.pca_variances_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=192,
)


_DELFLOCALFEATURECONFIG = _descriptor.Descriptor(
  name='DelfLocalFeatureConfig',
  full_name='delf.protos.DelfLocalFeatureConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_pca', full_name='delf.protos.DelfLocalFeatureConfig.use_pca', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='layer_name', full_name='delf.protos.DelfLocalFeatureConfig.layer_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iou_threshold', full_name='delf.protos.DelfLocalFeatureConfig.iou_threshold', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_feature_num', full_name='delf.protos.DelfLocalFeatureConfig.max_feature_num', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='delf.protos.DelfLocalFeatureConfig.score_threshold', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(100),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pca_parameters', full_name='delf.protos.DelfLocalFeatureConfig.pca_parameters', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=407,
)


_DELFCONFIG = _descriptor.Descriptor(
  name='DelfConfig',
  full_name='delf.protos.DelfConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_path', full_name='delf.protos.DelfConfig.model_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_scales', full_name='delf.protos.DelfConfig.image_scales', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delf_local_config', full_name='delf.protos.DelfConfig.delf_local_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_image_size', full_name='delf.protos.DelfConfig.max_image_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_image_size', full_name='delf.protos.DelfConfig.min_image_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=410,
  serialized_end=584,
)

_DELFLOCALFEATURECONFIG.fields_by_name['pca_parameters'].message_type = _DELFPCAPARAMETERS
_DELFCONFIG.fields_by_name['delf_local_config'].message_type = _DELFLOCALFEATURECONFIG
DESCRIPTOR.message_types_by_name['DelfPcaParameters'] = _DELFPCAPARAMETERS
DESCRIPTOR.message_types_by_name['DelfLocalFeatureConfig'] = _DELFLOCALFEATURECONFIG
DESCRIPTOR.message_types_by_name['DelfConfig'] = _DELFCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DelfPcaParameters = _reflection.GeneratedProtocolMessageType('DelfPcaParameters', (_message.Message,), dict(
  DESCRIPTOR = _DELFPCAPARAMETERS,
  __module__ = 'delf.protos.delf_config_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.DelfPcaParameters)
  ))
_sym_db.RegisterMessage(DelfPcaParameters)

DelfLocalFeatureConfig = _reflection.GeneratedProtocolMessageType('DelfLocalFeatureConfig', (_message.Message,), dict(
  DESCRIPTOR = _DELFLOCALFEATURECONFIG,
  __module__ = 'delf.protos.delf_config_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.DelfLocalFeatureConfig)
  ))
_sym_db.RegisterMessage(DelfLocalFeatureConfig)

DelfConfig = _reflection.GeneratedProtocolMessageType('DelfConfig', (_message.Message,), dict(
  DESCRIPTOR = _DELFCONFIG,
  __module__ = 'delf.protos.delf_config_pb2'
  # @@protoc_insertion_point(class_scope:delf.protos.DelfConfig)
  ))
_sym_db.RegisterMessage(DelfConfig)


# @@protoc_insertion_point(module_scope)
