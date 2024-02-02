# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Tms/allowlist.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tms_python_client.proto import common_pb2 as proto_dot_common__pb2
try:
  proto_dot_error__code__pb2 = proto_dot_common__pb2.proto_dot_error__code__pb2
except AttributeError:
  proto_dot_error__code__pb2 = proto_dot_common__pb2.proto.error_code_pb2
from tms_python_client.proto import model_state_pb2 as proto_dot_model__state__pb2

from tms_python_client.proto.common_pb2 import *
from tms_python_client.proto.model_state_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proto/Tms/allowlist.proto\x12\x18triton.management.server\x1a\x12proto/common.proto\x1a\x17proto/model-state.proto\"g\n\x1cTritonAllowlistAppendRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12\x15\n\rtriton_images\x18\x02 \x03(\t\"\x96\x02\n\x1dTritonAllowlistAppendResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12U\n\x07results\x18\x02 \x03(\x0b\x32\x44.triton.management.server.TritonAllowlistAppendResponse.AppendResult\x1ak\n\x0c\x41ppendResult\x12\x14\n\x0ctriton_image\x18\x01 \x01(\t\x12\x45\n\x06result\x18\x02 \x01(\x0e\x32\x35.triton.management.server.TritonAllowlistChangeResult\"N\n\x1aTritonAllowlistListRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\"f\n\x1bTritonAllowlistListResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12\x14\n\x0ctriton_image\x18\x02 \x01(\t\"g\n\x1cTritonAllowlistRemoveRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12\x15\n\rtriton_images\x18\x02 \x03(\t\"\x96\x02\n\x1dTritonAllowlistRemoveResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12U\n\x07results\x18\x02 \x03(\x0b\x32\x44.triton.management.server.TritonAllowlistRemoveResponse.RemoveResult\x1ak\n\x0cRemoveResult\x12\x14\n\x0ctriton_image\x18\x01 \x01(\t\x12\x45\n\x06result\x18\x02 \x01(\x0e\x32\x35.triton.management.server.TritonAllowlistChangeResult*\xe4\x01\n\x1bTritonAllowlistChangeResult\x12#\n\x1f\x41LLOWLIST_CHANGE_RESULT_UNKNOWN\x10\x00\x12#\n\x1f\x41LLOWLIST_CHANGE_RESULT_SUCCESS\x10\x01\x12%\n!ALLOWLIST_CHANGE_RESULT_DUPLICATE\x10\x02\x12+\n\'ALLOWLIST_CHANGE_RESULT_ALREADY_PRESENT\x10\x03\x12\'\n#ALLOWLIST_CHANGE_RESULT_NOT_PRESENT\x10\x04\x32\xfe\x02\n\x0fTritonAllowlist\x12y\n\x06\x41ppend\x12\x36.triton.management.server.TritonAllowlistAppendRequest\x1a\x37.triton.management.server.TritonAllowlistAppendResponse\x12u\n\x04List\x12\x34.triton.management.server.TritonAllowlistListRequest\x1a\x35.triton.management.server.TritonAllowlistListResponse0\x01\x12y\n\x06Remove\x12\x36.triton.management.server.TritonAllowlistRemoveRequest\x1a\x37.triton.management.server.TritonAllowlistRemoveResponseBM\n\x1a\x63om.triton.management.grpcZ\x16triton.management.grpc\xaa\x02\x16Triton.Management.GrpcP\x00P\x01\x62\x06proto3')

_TRITONALLOWLISTCHANGERESULT = DESCRIPTOR.enum_types_by_name['TritonAllowlistChangeResult']
TritonAllowlistChangeResult = enum_type_wrapper.EnumTypeWrapper(_TRITONALLOWLISTCHANGERESULT)
ALLOWLIST_CHANGE_RESULT_UNKNOWN = 0
ALLOWLIST_CHANGE_RESULT_SUCCESS = 1
ALLOWLIST_CHANGE_RESULT_DUPLICATE = 2
ALLOWLIST_CHANGE_RESULT_ALREADY_PRESENT = 3
ALLOWLIST_CHANGE_RESULT_NOT_PRESENT = 4


_TRITONALLOWLISTAPPENDREQUEST = DESCRIPTOR.message_types_by_name['TritonAllowlistAppendRequest']
_TRITONALLOWLISTAPPENDRESPONSE = DESCRIPTOR.message_types_by_name['TritonAllowlistAppendResponse']
_TRITONALLOWLISTAPPENDRESPONSE_APPENDRESULT = _TRITONALLOWLISTAPPENDRESPONSE.nested_types_by_name['AppendResult']
_TRITONALLOWLISTLISTREQUEST = DESCRIPTOR.message_types_by_name['TritonAllowlistListRequest']
_TRITONALLOWLISTLISTRESPONSE = DESCRIPTOR.message_types_by_name['TritonAllowlistListResponse']
_TRITONALLOWLISTREMOVEREQUEST = DESCRIPTOR.message_types_by_name['TritonAllowlistRemoveRequest']
_TRITONALLOWLISTREMOVERESPONSE = DESCRIPTOR.message_types_by_name['TritonAllowlistRemoveResponse']
_TRITONALLOWLISTREMOVERESPONSE_REMOVERESULT = _TRITONALLOWLISTREMOVERESPONSE.nested_types_by_name['RemoveResult']
TritonAllowlistAppendRequest = _reflection.GeneratedProtocolMessageType('TritonAllowlistAppendRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRITONALLOWLISTAPPENDREQUEST,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistAppendRequest)
  })
_sym_db.RegisterMessage(TritonAllowlistAppendRequest)

TritonAllowlistAppendResponse = _reflection.GeneratedProtocolMessageType('TritonAllowlistAppendResponse', (_message.Message,), {

  'AppendResult' : _reflection.GeneratedProtocolMessageType('AppendResult', (_message.Message,), {
    'DESCRIPTOR' : _TRITONALLOWLISTAPPENDRESPONSE_APPENDRESULT,
    '__module__' : 'proto.Tms.allowlist_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistAppendResponse.AppendResult)
    })
  ,
  'DESCRIPTOR' : _TRITONALLOWLISTAPPENDRESPONSE,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistAppendResponse)
  })
_sym_db.RegisterMessage(TritonAllowlistAppendResponse)
_sym_db.RegisterMessage(TritonAllowlistAppendResponse.AppendResult)

TritonAllowlistListRequest = _reflection.GeneratedProtocolMessageType('TritonAllowlistListRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRITONALLOWLISTLISTREQUEST,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistListRequest)
  })
_sym_db.RegisterMessage(TritonAllowlistListRequest)

TritonAllowlistListResponse = _reflection.GeneratedProtocolMessageType('TritonAllowlistListResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRITONALLOWLISTLISTRESPONSE,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistListResponse)
  })
_sym_db.RegisterMessage(TritonAllowlistListResponse)

TritonAllowlistRemoveRequest = _reflection.GeneratedProtocolMessageType('TritonAllowlistRemoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRITONALLOWLISTREMOVEREQUEST,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistRemoveRequest)
  })
_sym_db.RegisterMessage(TritonAllowlistRemoveRequest)

TritonAllowlistRemoveResponse = _reflection.GeneratedProtocolMessageType('TritonAllowlistRemoveResponse', (_message.Message,), {

  'RemoveResult' : _reflection.GeneratedProtocolMessageType('RemoveResult', (_message.Message,), {
    'DESCRIPTOR' : _TRITONALLOWLISTREMOVERESPONSE_REMOVERESULT,
    '__module__' : 'proto.Tms.allowlist_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistRemoveResponse.RemoveResult)
    })
  ,
  'DESCRIPTOR' : _TRITONALLOWLISTREMOVERESPONSE,
  '__module__' : 'proto.Tms.allowlist_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.TritonAllowlistRemoveResponse)
  })
_sym_db.RegisterMessage(TritonAllowlistRemoveResponse)
_sym_db.RegisterMessage(TritonAllowlistRemoveResponse.RemoveResult)

_TRITONALLOWLIST = DESCRIPTOR.services_by_name['TritonAllowlist']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.triton.management.grpcZ\026triton.management.grpc\252\002\026Triton.Management.Grpc'
  _TRITONALLOWLISTCHANGERESULT._serialized_start=1057
  _TRITONALLOWLISTCHANGERESULT._serialized_end=1285
  _TRITONALLOWLISTAPPENDREQUEST._serialized_start=100
  _TRITONALLOWLISTAPPENDREQUEST._serialized_end=203
  _TRITONALLOWLISTAPPENDRESPONSE._serialized_start=206
  _TRITONALLOWLISTAPPENDRESPONSE._serialized_end=484
  _TRITONALLOWLISTAPPENDRESPONSE_APPENDRESULT._serialized_start=377
  _TRITONALLOWLISTAPPENDRESPONSE_APPENDRESULT._serialized_end=484
  _TRITONALLOWLISTLISTREQUEST._serialized_start=486
  _TRITONALLOWLISTLISTREQUEST._serialized_end=564
  _TRITONALLOWLISTLISTRESPONSE._serialized_start=566
  _TRITONALLOWLISTLISTRESPONSE._serialized_end=668
  _TRITONALLOWLISTREMOVEREQUEST._serialized_start=670
  _TRITONALLOWLISTREMOVEREQUEST._serialized_end=773
  _TRITONALLOWLISTREMOVERESPONSE._serialized_start=776
  _TRITONALLOWLISTREMOVERESPONSE._serialized_end=1054
  _TRITONALLOWLISTREMOVERESPONSE_REMOVERESULT._serialized_start=947
  _TRITONALLOWLISTREMOVERESPONSE_REMOVERESULT._serialized_end=1054
  _TRITONALLOWLIST._serialized_start=1288
  _TRITONALLOWLIST._serialized_end=1670
# @@protoc_insertion_point(module_scope)
