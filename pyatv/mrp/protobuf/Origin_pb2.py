# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/Origin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import DeviceInfoMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/Origin.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1fpyatv/mrp/protobuf/Origin.proto\x1a*pyatv/mrp/protobuf/DeviceInfoMessage.proto\"g\n\x06Origin\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x13\n\x0b\x64isplayName\x18\x02 \x01(\t\x12\x12\n\nidentifier\x18\x03 \x01(\x05\x12&\n\ndeviceInfo\x18\x04 \x01(\x0b\x32\x12.DeviceInfoMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2.DESCRIPTOR,])




_ORIGIN = _descriptor.Descriptor(
  name='Origin',
  full_name='Origin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Origin.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayName', full_name='Origin.displayName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identifier', full_name='Origin.identifier', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deviceInfo', full_name='Origin.deviceInfo', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=182,
)

_ORIGIN.fields_by_name['deviceInfo'].message_type = pyatv_dot_mrp_dot_protobuf_dot_DeviceInfoMessage__pb2._DEVICEINFOMESSAGE
DESCRIPTOR.message_types_by_name['Origin'] = _ORIGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Origin = _reflection.GeneratedProtocolMessageType('Origin', (_message.Message,), {
  'DESCRIPTOR' : _ORIGIN,
  '__module__' : 'pyatv.mrp.protobuf.Origin_pb2'
  # @@protoc_insertion_point(class_scope:Origin)
  })
_sym_db.RegisterMessage(Origin)


# @@protoc_insertion_point(module_scope)
