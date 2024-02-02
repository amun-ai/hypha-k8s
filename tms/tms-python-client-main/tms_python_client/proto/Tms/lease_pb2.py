# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/Tms/lease.proto
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
from tms_python_client.proto.Tms import lease_event_pb2 as proto_dot_Tms_dot_lease__event__pb2
try:
  proto_dot_common__pb2 = proto_dot_Tms_dot_lease__event__pb2.proto_dot_common__pb2
except AttributeError:
  proto_dot_common__pb2 = proto_dot_Tms_dot_lease__event__pb2.proto.common_pb2
try:
  proto_dot_error__code__pb2 = proto_dot_Tms_dot_lease__event__pb2.proto_dot_error__code__pb2
except AttributeError:
  proto_dot_error__code__pb2 = proto_dot_Tms_dot_lease__event__pb2.proto.error_code_pb2

from tms_python_client.proto.common_pb2 import *
from tms_python_client.proto.model_state_pb2 import *
from tms_python_client.proto.Tms.lease_event_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proto/Tms/lease.proto\x12\x18triton.management.server\x1a\x12proto/common.proto\x1a\x17proto/model-state.proto\x1a\x1bproto/Tms/lease-event.proto\"\xb3\x01\n\x0fModelDescriptor\x12\x12\n\nmodel_name\x18\x01 \x01(\t\x12\x11\n\tmodel_urn\x18\x02 \x01(\t\x12\x16\n\x0einstance_count\x18\x06 \x01(\x05\x12\x32\n\x0bmodel_state\x18\x03 \x01(\x0e\x32\x1d.triton.management.ModelState\x12\x16\n\x0emodel_versions\x18\x04 \x03(\t\x12\x15\n\rmodel_backend\x18\x05 \x01(\t\"\x9d\x04\n\x13LeaseAcquireRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12J\n\x06models\x18\x02 \x03(\x0b\x32:.triton.management.server.LeaseAcquireRequest.ModelRequest\x12\x14\n\x0ctriton_image\x18\x03 \x01(\t\x12\x43\n\x10\x64uration_options\x18\x04 \x01(\x0b\x32).triton.management.server.DurationOptions\x12\x36\n\x06shared\x18\x05 \x01(\x0e\x32&.triton.management.server.SharedTriton\x12U\n\x18triton_resource_requests\x18\x06 \x01(\x0b\x32\x33.triton.management.server.ContainerResourceRequests\x12I\n\x13\x61utoscaling_options\x18\x07 \x01(\x0b\x32,.triton.management.server.AutoscalingOptions\x1aS\n\x0cModelRequest\x12\x11\n\tmodel_urn\x18\x01 \x01(\t\x12\x12\n\nmodel_name\x18\x02 \x01(\t\x12\x1c\n\x14model_instance_count\x18\x03 \x01(\x05\"\xc1\x01\n\x19\x43ontainerResourceRequests\x12\x16\n\tcpu_milli\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x10\n\x03gpu\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0cmemory_bytes\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12 \n\x13shared_memory_bytes\x18\x04 \x01(\x03H\x03\x88\x01\x01\x42\x0c\n\n_cpu_milliB\x06\n\x04_gpuB\x0f\n\r_memory_bytesB\x16\n\x14_shared_memory_bytes\"\xe6\x04\n\x12\x41utoscalingOptions\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x19\n\x0cmax_replicas\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x19\n\x0cmin_replicas\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12[\n\x1emetric_gpu_utilization_percent\x18\x04 \x01(\x0b\x32\x33.triton.management.server.AutoscalingOptions.Metric\x12[\n\x1emetric_cpu_utilization_percent\x18\x05 \x01(\x0b\x32\x33.triton.management.server.AutoscalingOptions.Metric\x12S\n\x16metric_queue_time_usec\x18\x06 \x01(\x0b\x32\x33.triton.management.server.AutoscalingOptions.Metric\x1aw\n\x06Metric\x12G\n\x05state\x18\x01 \x01(\x0e\x32\x38.triton.management.server.AutoscalingOptions.MetricState\x12\x16\n\tthreshold\x18\x02 \x01(\x05H\x00\x88\x01\x01\x42\x0c\n\n_threshold\"`\n\x0bMetricState\x12\x1c\n\x18METRIC_STATE_UNSPECIFIED\x10\x00\x12\x18\n\x14METRIC_STATE_ENABLED\x10\x01\x12\x19\n\x15METRIC_STATE_DISABLED\x10\x02\x42\x0f\n\r_max_replicasB\x0f\n\r_min_replicas\"\xc0\x02\n\x0f\x44urationOptions\x12:\n\x10initial_duration\x18\x01 \x01(\x0b\x32\x1b.triton.management.DurationH\x00\x88\x01\x01\x12:\n\x10renewal_duration\x18\x02 \x01(\x0b\x32\x1b.triton.management.DurationH\x01\x88\x01\x01\x12\x17\n\nauto_renew\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x44\n\x1a\x61uto_renew_activity_window\x18\x04 \x01(\x0b\x32\x1b.triton.management.DurationH\x03\x88\x01\x01\x42\x13\n\x11_initial_durationB\x13\n\x11_renewal_durationB\r\n\x0b_auto_renewB\x1d\n\x1b_auto_renew_activity_window\"\xbe\x04\n\x14LeaseAcquireResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12\x10\n\x08lease_id\x18\x02 \x01(\x0c\x12\x39\n\x13requested_timestamp\x18\x0c \x01(\x0b\x32\x1c.triton.management.Timestamp\x12\x39\n\x0blease_state\x18\x03 \x01(\x0e\x32$.triton.management.server.LeaseState\x12\x12\n\ntriton_urn\x18\x04 \x01(\t\x12-\n\x07\x65xpires\x18\x05 \x01(\x0b\x32\x1c.triton.management.Timestamp\x12\x39\n\x06models\x18\x06 \x03(\x0b\x32).triton.management.server.ModelDescriptor\x12\x14\n\x0ctriton_image\x18\x07 \x01(\t\x12\x15\n\rshared_triton\x18\x08 \x01(\x08\x12G\n\x12\x61utoscaling_status\x18\t \x01(\x0b\x32+.triton.management.server.AutoscalingStatus\x12\x41\n\x0f\x64uration_status\x18\n \x01(\x0b\x32(.triton.management.server.DurationStatus\x12\x34\n\x06\x65vents\x18\x0b \x03(\x0b\x32$.triton.management.server.LeaseEvent\"D\n\x10LeaseListRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\"Y\n\x13LeaseReleaseRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12\x10\n\x08lease_id\x18\x02 \x01(\x0c\"~\n\x14LeaseReleaseResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12\x33\n\x05state\x18\x02 \x01(\x0e\x32$.triton.management.server.LeaseState\"W\n\x11LeaseRenewRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12\x10\n\x08lease_id\x18\x02 \x01(\x0c\"\xab\x01\n\x12LeaseRenewResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12\x33\n\x05state\x18\x02 \x01(\x0e\x32$.triton.management.server.LeaseState\x12-\n\x07\x65xpires\x18\x03 \x01(\x0b\x32\x1c.triton.management.Timestamp\"X\n\x12LeaseStatusRequest\x12\x30\n\x06header\x18\x01 \x01(\x0b\x32 .triton.management.RequestHeader\x12\x10\n\x08lease_id\x18\x02 \x01(\x0c\"\xb3\x06\n\x13LeaseStatusResponse\x12\x31\n\x06header\x18\x01 \x01(\x0b\x32!.triton.management.ResponseHeader\x12\x10\n\x08lease_id\x18\x02 \x01(\x0c\x12\x39\n\x0blease_state\x18\x03 \x01(\x0e\x32$.triton.management.server.LeaseState\x12\x39\n\x13requested_timestamp\x18\r \x01(\x0b\x32\x1c.triton.management.Timestamp\x12:\n\x0fready_timestamp\x18\x0e \x01(\x0b\x32\x1c.triton.management.TimestampH\x00\x88\x01\x01\x12\x12\n\ntriton_urn\x18\x04 \x01(\t\x12-\n\x07\x65xpires\x18\x05 \x01(\x0b\x32\x1c.triton.management.Timestamp\x12\x39\n\x06models\x18\x06 \x03(\x0b\x32).triton.management.server.ModelDescriptor\x12N\n\x08renewals\x18\x07 \x03(\x0b\x32<.triton.management.server.LeaseStatusResponse.RenewalDetails\x12\x14\n\x0ctriton_image\x18\x08 \x01(\t\x12\x41\n\x0f\x64uration_status\x18\t \x01(\x0b\x32(.triton.management.server.DurationStatus\x12\x15\n\rshared_triton\x18\n \x01(\x08\x12G\n\x12\x61utoscaling_status\x18\x0b \x01(\x0b\x32+.triton.management.server.AutoscalingStatus\x12\x34\n\x06\x65vents\x18\x0c \x03(\x0b\x32$.triton.management.server.LeaseEvent\x1aT\n\x0eRenewalDetails\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12/\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1c.triton.management.TimestampB\x12\n\x10_ready_timestamp\"\x8a\x03\n\x11\x41utoscalingStatus\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x14\n\x0cmax_replicas\x18\x02 \x01(\x05\x12\x14\n\x0cmin_replicas\x18\x03 \x01(\x05\x12Z\n\x1emetric_gpu_utilization_percent\x18\x04 \x01(\x0b\x32\x32.triton.management.server.AutoscalingStatus.Metric\x12Z\n\x1emetric_cpu_utilization_percent\x18\x05 \x01(\x0b\x32\x32.triton.management.server.AutoscalingStatus.Metric\x12R\n\x16metric_queue_time_usec\x18\x06 \x01(\x0b\x32\x32.triton.management.server.AutoscalingStatus.Metric\x1a,\n\x06Metric\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x11\n\tthreshold\x18\x02 \x01(\x05\"\xd3\x01\n\x0e\x44urationStatus\x12\x12\n\nauto_renew\x18\x01 \x01(\x08\x12?\n\x1a\x61uto_renew_activity_window\x18\x02 \x01(\x0b\x32\x1b.triton.management.Duration\x12\x35\n\x10initial_duration\x18\x03 \x01(\x0b\x32\x1b.triton.management.Duration\x12\x35\n\x10renewal_duration\x18\x04 \x01(\x0b\x32\x1b.triton.management.Duration*\x9f\x01\n\nLeaseState\x12\x17\n\x13LEASE_STATE_UNKNOWN\x10\x00\x12\x17\n\x13LEASE_STATE_PENDING\x10\x01\x12\x15\n\x11LEASE_STATE_VALID\x10\x02\x12\x18\n\x14LEASE_STATE_RELEASED\x10\x03\x12\x17\n\x13LEASE_STATE_EXPIRED\x10\x04\x12\x15\n\x11LEASE_STATE_ERROR\x10\x05*^\n\x0cSharedTriton\x12\x1d\n\x19SHARED_TRITON_UNSPECIFIED\x10\x00\x12\x17\n\x13SHARED_TRITON_FALSE\x10\x01\x12\x16\n\x12SHARED_TRITON_TRUE\x10\x02\x32\x8d\x04\n\x05Lease\x12j\n\x07\x41\x63quire\x12-.triton.management.server.LeaseAcquireRequest\x1a..triton.management.server.LeaseAcquireResponse0\x01\x12\x63\n\x04List\x12*.triton.management.server.LeaseListRequest\x1a-.triton.management.server.LeaseStatusResponse0\x01\x12h\n\x07Release\x12-.triton.management.server.LeaseReleaseRequest\x1a..triton.management.server.LeaseReleaseResponse\x12\x62\n\x05Renew\x12+.triton.management.server.LeaseRenewRequest\x1a,.triton.management.server.LeaseRenewResponse\x12\x65\n\x06Status\x12,.triton.management.server.LeaseStatusRequest\x1a-.triton.management.server.LeaseStatusResponseBM\n\x1a\x63om.triton.management.grpcZ\x16triton.management.grpc\xaa\x02\x16Triton.Management.GrpcP\x00P\x01P\x02\x62\x06proto3')

_LEASESTATE = DESCRIPTOR.enum_types_by_name['LeaseState']
LeaseState = enum_type_wrapper.EnumTypeWrapper(_LEASESTATE)
_SHAREDTRITON = DESCRIPTOR.enum_types_by_name['SharedTriton']
SharedTriton = enum_type_wrapper.EnumTypeWrapper(_SHAREDTRITON)
LEASE_STATE_UNKNOWN = 0
LEASE_STATE_PENDING = 1
LEASE_STATE_VALID = 2
LEASE_STATE_RELEASED = 3
LEASE_STATE_EXPIRED = 4
LEASE_STATE_ERROR = 5
SHARED_TRITON_UNSPECIFIED = 0
SHARED_TRITON_FALSE = 1
SHARED_TRITON_TRUE = 2


_MODELDESCRIPTOR = DESCRIPTOR.message_types_by_name['ModelDescriptor']
_LEASEACQUIREREQUEST = DESCRIPTOR.message_types_by_name['LeaseAcquireRequest']
_LEASEACQUIREREQUEST_MODELREQUEST = _LEASEACQUIREREQUEST.nested_types_by_name['ModelRequest']
_CONTAINERRESOURCEREQUESTS = DESCRIPTOR.message_types_by_name['ContainerResourceRequests']
_AUTOSCALINGOPTIONS = DESCRIPTOR.message_types_by_name['AutoscalingOptions']
_AUTOSCALINGOPTIONS_METRIC = _AUTOSCALINGOPTIONS.nested_types_by_name['Metric']
_DURATIONOPTIONS = DESCRIPTOR.message_types_by_name['DurationOptions']
_LEASEACQUIRERESPONSE = DESCRIPTOR.message_types_by_name['LeaseAcquireResponse']
_LEASELISTREQUEST = DESCRIPTOR.message_types_by_name['LeaseListRequest']
_LEASERELEASEREQUEST = DESCRIPTOR.message_types_by_name['LeaseReleaseRequest']
_LEASERELEASERESPONSE = DESCRIPTOR.message_types_by_name['LeaseReleaseResponse']
_LEASERENEWREQUEST = DESCRIPTOR.message_types_by_name['LeaseRenewRequest']
_LEASERENEWRESPONSE = DESCRIPTOR.message_types_by_name['LeaseRenewResponse']
_LEASESTATUSREQUEST = DESCRIPTOR.message_types_by_name['LeaseStatusRequest']
_LEASESTATUSRESPONSE = DESCRIPTOR.message_types_by_name['LeaseStatusResponse']
_LEASESTATUSRESPONSE_RENEWALDETAILS = _LEASESTATUSRESPONSE.nested_types_by_name['RenewalDetails']
_AUTOSCALINGSTATUS = DESCRIPTOR.message_types_by_name['AutoscalingStatus']
_AUTOSCALINGSTATUS_METRIC = _AUTOSCALINGSTATUS.nested_types_by_name['Metric']
_DURATIONSTATUS = DESCRIPTOR.message_types_by_name['DurationStatus']
_AUTOSCALINGOPTIONS_METRICSTATE = _AUTOSCALINGOPTIONS.enum_types_by_name['MetricState']
ModelDescriptor = _reflection.GeneratedProtocolMessageType('ModelDescriptor', (_message.Message,), {
  'DESCRIPTOR' : _MODELDESCRIPTOR,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.ModelDescriptor)
  })
_sym_db.RegisterMessage(ModelDescriptor)

LeaseAcquireRequest = _reflection.GeneratedProtocolMessageType('LeaseAcquireRequest', (_message.Message,), {

  'ModelRequest' : _reflection.GeneratedProtocolMessageType('ModelRequest', (_message.Message,), {
    'DESCRIPTOR' : _LEASEACQUIREREQUEST_MODELREQUEST,
    '__module__' : 'proto.Tms.lease_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.LeaseAcquireRequest.ModelRequest)
    })
  ,
  'DESCRIPTOR' : _LEASEACQUIREREQUEST,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseAcquireRequest)
  })
_sym_db.RegisterMessage(LeaseAcquireRequest)
_sym_db.RegisterMessage(LeaseAcquireRequest.ModelRequest)

ContainerResourceRequests = _reflection.GeneratedProtocolMessageType('ContainerResourceRequests', (_message.Message,), {
  'DESCRIPTOR' : _CONTAINERRESOURCEREQUESTS,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.ContainerResourceRequests)
  })
_sym_db.RegisterMessage(ContainerResourceRequests)

AutoscalingOptions = _reflection.GeneratedProtocolMessageType('AutoscalingOptions', (_message.Message,), {

  'Metric' : _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
    'DESCRIPTOR' : _AUTOSCALINGOPTIONS_METRIC,
    '__module__' : 'proto.Tms.lease_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.AutoscalingOptions.Metric)
    })
  ,
  'DESCRIPTOR' : _AUTOSCALINGOPTIONS,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.AutoscalingOptions)
  })
_sym_db.RegisterMessage(AutoscalingOptions)
_sym_db.RegisterMessage(AutoscalingOptions.Metric)

DurationOptions = _reflection.GeneratedProtocolMessageType('DurationOptions', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONOPTIONS,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.DurationOptions)
  })
_sym_db.RegisterMessage(DurationOptions)

LeaseAcquireResponse = _reflection.GeneratedProtocolMessageType('LeaseAcquireResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEASEACQUIRERESPONSE,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseAcquireResponse)
  })
_sym_db.RegisterMessage(LeaseAcquireResponse)

LeaseListRequest = _reflection.GeneratedProtocolMessageType('LeaseListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEASELISTREQUEST,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseListRequest)
  })
_sym_db.RegisterMessage(LeaseListRequest)

LeaseReleaseRequest = _reflection.GeneratedProtocolMessageType('LeaseReleaseRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEASERELEASEREQUEST,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseReleaseRequest)
  })
_sym_db.RegisterMessage(LeaseReleaseRequest)

LeaseReleaseResponse = _reflection.GeneratedProtocolMessageType('LeaseReleaseResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEASERELEASERESPONSE,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseReleaseResponse)
  })
_sym_db.RegisterMessage(LeaseReleaseResponse)

LeaseRenewRequest = _reflection.GeneratedProtocolMessageType('LeaseRenewRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEASERENEWREQUEST,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseRenewRequest)
  })
_sym_db.RegisterMessage(LeaseRenewRequest)

LeaseRenewResponse = _reflection.GeneratedProtocolMessageType('LeaseRenewResponse', (_message.Message,), {
  'DESCRIPTOR' : _LEASERENEWRESPONSE,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseRenewResponse)
  })
_sym_db.RegisterMessage(LeaseRenewResponse)

LeaseStatusRequest = _reflection.GeneratedProtocolMessageType('LeaseStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _LEASESTATUSREQUEST,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseStatusRequest)
  })
_sym_db.RegisterMessage(LeaseStatusRequest)

LeaseStatusResponse = _reflection.GeneratedProtocolMessageType('LeaseStatusResponse', (_message.Message,), {

  'RenewalDetails' : _reflection.GeneratedProtocolMessageType('RenewalDetails', (_message.Message,), {
    'DESCRIPTOR' : _LEASESTATUSRESPONSE_RENEWALDETAILS,
    '__module__' : 'proto.Tms.lease_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.LeaseStatusResponse.RenewalDetails)
    })
  ,
  'DESCRIPTOR' : _LEASESTATUSRESPONSE,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.LeaseStatusResponse)
  })
_sym_db.RegisterMessage(LeaseStatusResponse)
_sym_db.RegisterMessage(LeaseStatusResponse.RenewalDetails)

AutoscalingStatus = _reflection.GeneratedProtocolMessageType('AutoscalingStatus', (_message.Message,), {

  'Metric' : _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), {
    'DESCRIPTOR' : _AUTOSCALINGSTATUS_METRIC,
    '__module__' : 'proto.Tms.lease_pb2'
    # @@protoc_insertion_point(class_scope:triton.management.server.AutoscalingStatus.Metric)
    })
  ,
  'DESCRIPTOR' : _AUTOSCALINGSTATUS,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.AutoscalingStatus)
  })
_sym_db.RegisterMessage(AutoscalingStatus)
_sym_db.RegisterMessage(AutoscalingStatus.Metric)

DurationStatus = _reflection.GeneratedProtocolMessageType('DurationStatus', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONSTATUS,
  '__module__' : 'proto.Tms.lease_pb2'
  # @@protoc_insertion_point(class_scope:triton.management.server.DurationStatus)
  })
_sym_db.RegisterMessage(DurationStatus)

_LEASE = DESCRIPTOR.services_by_name['Lease']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.triton.management.grpcZ\026triton.management.grpc\252\002\026Triton.Management.Grpc'
  _LEASESTATE._serialized_start=4640
  _LEASESTATE._serialized_end=4799
  _SHAREDTRITON._serialized_start=4801
  _SHAREDTRITON._serialized_end=4895
  _MODELDESCRIPTOR._serialized_start=126
  _MODELDESCRIPTOR._serialized_end=305
  _LEASEACQUIREREQUEST._serialized_start=308
  _LEASEACQUIREREQUEST._serialized_end=849
  _LEASEACQUIREREQUEST_MODELREQUEST._serialized_start=766
  _LEASEACQUIREREQUEST_MODELREQUEST._serialized_end=849
  _CONTAINERRESOURCEREQUESTS._serialized_start=852
  _CONTAINERRESOURCEREQUESTS._serialized_end=1045
  _AUTOSCALINGOPTIONS._serialized_start=1048
  _AUTOSCALINGOPTIONS._serialized_end=1662
  _AUTOSCALINGOPTIONS_METRIC._serialized_start=1411
  _AUTOSCALINGOPTIONS_METRIC._serialized_end=1530
  _AUTOSCALINGOPTIONS_METRICSTATE._serialized_start=1532
  _AUTOSCALINGOPTIONS_METRICSTATE._serialized_end=1628
  _DURATIONOPTIONS._serialized_start=1665
  _DURATIONOPTIONS._serialized_end=1985
  _LEASEACQUIRERESPONSE._serialized_start=1988
  _LEASEACQUIRERESPONSE._serialized_end=2562
  _LEASELISTREQUEST._serialized_start=2564
  _LEASELISTREQUEST._serialized_end=2632
  _LEASERELEASEREQUEST._serialized_start=2634
  _LEASERELEASEREQUEST._serialized_end=2723
  _LEASERELEASERESPONSE._serialized_start=2725
  _LEASERELEASERESPONSE._serialized_end=2851
  _LEASERENEWREQUEST._serialized_start=2853
  _LEASERENEWREQUEST._serialized_end=2940
  _LEASERENEWRESPONSE._serialized_start=2943
  _LEASERENEWRESPONSE._serialized_end=3114
  _LEASESTATUSREQUEST._serialized_start=3116
  _LEASESTATUSREQUEST._serialized_end=3204
  _LEASESTATUSRESPONSE._serialized_start=3207
  _LEASESTATUSRESPONSE._serialized_end=4026
  _LEASESTATUSRESPONSE_RENEWALDETAILS._serialized_start=3922
  _LEASESTATUSRESPONSE_RENEWALDETAILS._serialized_end=4006
  _AUTOSCALINGSTATUS._serialized_start=4029
  _AUTOSCALINGSTATUS._serialized_end=4423
  _AUTOSCALINGSTATUS_METRIC._serialized_start=4379
  _AUTOSCALINGSTATUS_METRIC._serialized_end=4423
  _DURATIONSTATUS._serialized_start=4426
  _DURATIONSTATUS._serialized_end=4637
  _LEASE._serialized_start=4898
  _LEASE._serialized_end=5423
# @@protoc_insertion_point(module_scope)
