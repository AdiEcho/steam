# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_unified_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_unified_test.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n steammessages_unified_test.proto\x1a steammessages_unified_base.proto\"G\n CMsgTest_MessageToClient_Request\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.\"H\n!CMsgTest_MessageToClient_Response\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.\"I\n\"CMsgTest_NotifyClient_Notification\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.\"G\n CMsgTest_MessageToServer_Request\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.\"H\n!CMsgTest_MessageToServer_Response\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.\"I\n\"CMsgTest_NotifyServer_Notification\x12#\n\tsome_text\x18\x01 \x01(\tB\x10\x82\xb5\x18\x0cSome string.2\x83\x02\n\x0fTestSteamClient\x12\x81\x01\n\x0fMessageToClient\x12!.CMsgTest_MessageToClient_Request\x1a\".CMsgTest_MessageToClient_Response\"\'\x82\xb5\x18#Some description - MessageToClient.\x12\x66\n\x0cNotifyClient\x12#.CMsgTest_NotifyClient_Notification\x1a\x0b.NoResponse\"$\x82\xb5\x18 Some description - NotifyClient.\x1a\x04\xc0\xb5\x18\x02\x32\x82\x02\n\x14TestServerFromClient\x12\x81\x01\n\x0fMessageToServer\x12!.CMsgTest_MessageToServer_Request\x1a\".CMsgTest_MessageToServer_Response\"\'\x82\xb5\x18#Some description - MessageToServer.\x12\x66\n\x0cNotifyServer\x12#.CMsgTest_NotifyServer_Notification\x1a\x0b.NoResponse\"$\x82\xb5\x18 Some description - NotifyServer.B\x03\x90\x01\x01')
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CMSGTEST_MESSAGETOCLIENT_REQUEST = _descriptor.Descriptor(
  name='CMsgTest_MessageToClient_Request',
  full_name='CMsgTest_MessageToClient_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_MessageToClient_Request.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=70,
  serialized_end=141,
)


_CMSGTEST_MESSAGETOCLIENT_RESPONSE = _descriptor.Descriptor(
  name='CMsgTest_MessageToClient_Response',
  full_name='CMsgTest_MessageToClient_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_MessageToClient_Response.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=143,
  serialized_end=215,
)


_CMSGTEST_NOTIFYCLIENT_NOTIFICATION = _descriptor.Descriptor(
  name='CMsgTest_NotifyClient_Notification',
  full_name='CMsgTest_NotifyClient_Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_NotifyClient_Notification.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=217,
  serialized_end=290,
)


_CMSGTEST_MESSAGETOSERVER_REQUEST = _descriptor.Descriptor(
  name='CMsgTest_MessageToServer_Request',
  full_name='CMsgTest_MessageToServer_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_MessageToServer_Request.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=292,
  serialized_end=363,
)


_CMSGTEST_MESSAGETOSERVER_RESPONSE = _descriptor.Descriptor(
  name='CMsgTest_MessageToServer_Response',
  full_name='CMsgTest_MessageToServer_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_MessageToServer_Response.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=365,
  serialized_end=437,
)


_CMSGTEST_NOTIFYSERVER_NOTIFICATION = _descriptor.Descriptor(
  name='CMsgTest_NotifyServer_Notification',
  full_name='CMsgTest_NotifyServer_Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='some_text', full_name='CMsgTest_NotifyServer_Notification.some_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))),
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
  serialized_start=439,
  serialized_end=512,
)

DESCRIPTOR.message_types_by_name['CMsgTest_MessageToClient_Request'] = _CMSGTEST_MESSAGETOCLIENT_REQUEST
DESCRIPTOR.message_types_by_name['CMsgTest_MessageToClient_Response'] = _CMSGTEST_MESSAGETOCLIENT_RESPONSE
DESCRIPTOR.message_types_by_name['CMsgTest_NotifyClient_Notification'] = _CMSGTEST_NOTIFYCLIENT_NOTIFICATION
DESCRIPTOR.message_types_by_name['CMsgTest_MessageToServer_Request'] = _CMSGTEST_MESSAGETOSERVER_REQUEST
DESCRIPTOR.message_types_by_name['CMsgTest_MessageToServer_Response'] = _CMSGTEST_MESSAGETOSERVER_RESPONSE
DESCRIPTOR.message_types_by_name['CMsgTest_NotifyServer_Notification'] = _CMSGTEST_NOTIFYSERVER_NOTIFICATION

CMsgTest_MessageToClient_Request = _reflection.GeneratedProtocolMessageType('CMsgTest_MessageToClient_Request', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_MESSAGETOCLIENT_REQUEST,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_MessageToClient_Request)
  ))
_sym_db.RegisterMessage(CMsgTest_MessageToClient_Request)

CMsgTest_MessageToClient_Response = _reflection.GeneratedProtocolMessageType('CMsgTest_MessageToClient_Response', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_MESSAGETOCLIENT_RESPONSE,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_MessageToClient_Response)
  ))
_sym_db.RegisterMessage(CMsgTest_MessageToClient_Response)

CMsgTest_NotifyClient_Notification = _reflection.GeneratedProtocolMessageType('CMsgTest_NotifyClient_Notification', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_NOTIFYCLIENT_NOTIFICATION,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_NotifyClient_Notification)
  ))
_sym_db.RegisterMessage(CMsgTest_NotifyClient_Notification)

CMsgTest_MessageToServer_Request = _reflection.GeneratedProtocolMessageType('CMsgTest_MessageToServer_Request', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_MESSAGETOSERVER_REQUEST,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_MessageToServer_Request)
  ))
_sym_db.RegisterMessage(CMsgTest_MessageToServer_Request)

CMsgTest_MessageToServer_Response = _reflection.GeneratedProtocolMessageType('CMsgTest_MessageToServer_Response', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_MESSAGETOSERVER_RESPONSE,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_MessageToServer_Response)
  ))
_sym_db.RegisterMessage(CMsgTest_MessageToServer_Response)

CMsgTest_NotifyServer_Notification = _reflection.GeneratedProtocolMessageType('CMsgTest_NotifyServer_Notification', (_message.Message,), dict(
  DESCRIPTOR = _CMSGTEST_NOTIFYSERVER_NOTIFICATION,
  __module__ = 'steammessages_unified_test_pb2'
  # @@protoc_insertion_point(class_scope:CMsgTest_NotifyServer_Notification)
  ))
_sym_db.RegisterMessage(CMsgTest_NotifyServer_Notification)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))
_CMSGTEST_MESSAGETOCLIENT_REQUEST.fields_by_name['some_text'].has_options = True
_CMSGTEST_MESSAGETOCLIENT_REQUEST.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))
_CMSGTEST_MESSAGETOCLIENT_RESPONSE.fields_by_name['some_text'].has_options = True
_CMSGTEST_MESSAGETOCLIENT_RESPONSE.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))
_CMSGTEST_NOTIFYCLIENT_NOTIFICATION.fields_by_name['some_text'].has_options = True
_CMSGTEST_NOTIFYCLIENT_NOTIFICATION.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))
_CMSGTEST_MESSAGETOSERVER_REQUEST.fields_by_name['some_text'].has_options = True
_CMSGTEST_MESSAGETOSERVER_REQUEST.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))
_CMSGTEST_MESSAGETOSERVER_RESPONSE.fields_by_name['some_text'].has_options = True
_CMSGTEST_MESSAGETOSERVER_RESPONSE.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))
_CMSGTEST_NOTIFYSERVER_NOTIFICATION.fields_by_name['some_text'].has_options = True
_CMSGTEST_NOTIFYSERVER_NOTIFICATION.fields_by_name['some_text']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\014Some string.'))

_TESTSTEAMCLIENT = _descriptor.ServiceDescriptor(
  name='TestSteamClient',
  full_name='TestSteamClient',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\300\265\030\002')),
  serialized_start=515,
  serialized_end=774,
  methods=[
  _descriptor.MethodDescriptor(
    name='MessageToClient',
    full_name='TestSteamClient.MessageToClient',
    index=0,
    containing_service=None,
    input_type=_CMSGTEST_MESSAGETOCLIENT_REQUEST,
    output_type=_CMSGTEST_MESSAGETOCLIENT_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030#Some description - MessageToClient.')),
  ),
  _descriptor.MethodDescriptor(
    name='NotifyClient',
    full_name='TestSteamClient.NotifyClient',
    index=1,
    containing_service=None,
    input_type=_CMSGTEST_NOTIFYCLIENT_NOTIFICATION,
    output_type=steammessages__unified__base__pb2._NORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030 Some description - NotifyClient.')),
  ),
])

TestSteamClient = service_reflection.GeneratedServiceType('TestSteamClient', (_service.Service,), dict(
  DESCRIPTOR = _TESTSTEAMCLIENT,
  __module__ = 'steammessages_unified_test_pb2'
  ))

TestSteamClient_Stub = service_reflection.GeneratedServiceStubType('TestSteamClient_Stub', (TestSteamClient,), dict(
  DESCRIPTOR = _TESTSTEAMCLIENT,
  __module__ = 'steammessages_unified_test_pb2'
  ))



_TESTSERVERFROMCLIENT = _descriptor.ServiceDescriptor(
  name='TestServerFromClient',
  full_name='TestServerFromClient',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=777,
  serialized_end=1035,
  methods=[
  _descriptor.MethodDescriptor(
    name='MessageToServer',
    full_name='TestServerFromClient.MessageToServer',
    index=0,
    containing_service=None,
    input_type=_CMSGTEST_MESSAGETOSERVER_REQUEST,
    output_type=_CMSGTEST_MESSAGETOSERVER_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030#Some description - MessageToServer.')),
  ),
  _descriptor.MethodDescriptor(
    name='NotifyServer',
    full_name='TestServerFromClient.NotifyServer',
    index=1,
    containing_service=None,
    input_type=_CMSGTEST_NOTIFYSERVER_NOTIFICATION,
    output_type=steammessages__unified__base__pb2._NORESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030 Some description - NotifyServer.')),
  ),
])

TestServerFromClient = service_reflection.GeneratedServiceType('TestServerFromClient', (_service.Service,), dict(
  DESCRIPTOR = _TESTSERVERFROMCLIENT,
  __module__ = 'steammessages_unified_test_pb2'
  ))

TestServerFromClient_Stub = service_reflection.GeneratedServiceStubType('TestServerFromClient_Stub', (TestServerFromClient,), dict(
  DESCRIPTOR = _TESTSERVERFROMCLIENT,
  __module__ = 'steammessages_unified_test_pb2'
  ))


# @@protoc_insertion_point(module_scope)
