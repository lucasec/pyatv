# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/AudioFormatSettingsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/AudioFormatSettingsMessage.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n3pyatv/mrp/protobuf/AudioFormatSettingsMessage.proto\"6\n\x13\x41udioFormatSettings\x12\x1f\n\x17\x66ormatSettingsPlistData\x18\x01 \x01(\x0c')
)




_AUDIOFORMATSETTINGS = _descriptor.Descriptor(
  name='AudioFormatSettings',
  full_name='AudioFormatSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='formatSettingsPlistData', full_name='AudioFormatSettings.formatSettingsPlistData', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=55,
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['AudioFormatSettings'] = _AUDIOFORMATSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AudioFormatSettings = _reflection.GeneratedProtocolMessageType('AudioFormatSettings', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOFORMATSETTINGS,
  '__module__' : 'pyatv.mrp.protobuf.AudioFormatSettingsMessage_pb2'
  # @@protoc_insertion_point(class_scope:AudioFormatSettings)
  })
_sym_db.RegisterMessage(AudioFormatSettings)


# @@protoc_insertion_point(module_scope)
