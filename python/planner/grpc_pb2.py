# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\x12\x07planner\"]\n\x1f\x43\x61lculateOptimalReplicasRequest\x12(\n\x0b\x64\x65ployments\x18\x01 \x03(\x0b\x32\x13.planner.Deployment\x12\x10\n\x08powerCap\x18\x02 \x01(\x01\"-\n\nDeployment\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\"[\n CalculateOptimalReplicasResponse\x12\x37\n\x12\x64\x65ploymentReplicas\x18\x01 \x03(\x0b\x32\x1b.planner.DeploymentReplicas\"N\n\x12\x44\x65ploymentReplicas\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x17\n\x0foptimalReplicas\x18\x03 \x01(\x05\x32|\n\x07Planner\x12q\n\x18\x43\x61lculateOptimalReplicas\x12(.planner.CalculateOptimalReplicasRequest\x1a).planner.CalculateOptimalReplicasResponse\"\x00\x42\x37Z5github.com/example/power-capping-operator/pkg/plannerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/example/power-capping-operator/pkg/planner'
  _globals['_CALCULATEOPTIMALREPLICASREQUEST']._serialized_start=23
  _globals['_CALCULATEOPTIMALREPLICASREQUEST']._serialized_end=116
  _globals['_DEPLOYMENT']._serialized_start=118
  _globals['_DEPLOYMENT']._serialized_end=163
  _globals['_CALCULATEOPTIMALREPLICASRESPONSE']._serialized_start=165
  _globals['_CALCULATEOPTIMALREPLICASRESPONSE']._serialized_end=256
  _globals['_DEPLOYMENTREPLICAS']._serialized_start=258
  _globals['_DEPLOYMENTREPLICAS']._serialized_end=336
  _globals['_PLANNER']._serialized_start=338
  _globals['_PLANNER']._serialized_end=462
# @@protoc_insertion_point(module_scope)
