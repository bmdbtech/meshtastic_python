# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meshtastic/mqtt.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from meshtastic.pbDefinitions import mesh_pb2 as meshtastic_dot_mesh__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15meshtastic/mqtt.proto\x12\nmeshtastic\x1a\x15meshtastic/mesh.proto\"a\n\x0fServiceEnvelope\x12&\n\x06packet\x18\x01 \x01(\x0b\x32\x16.meshtastic.MeshPacket\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x12\n\ngateway_id\x18\x03 \x01(\tB_\n\x13\x63om.geeksville.meshB\nMQTTProtosZ\"github.com/meshtastic/go/generated\xaa\x02\x14Meshtastic.Protobufs\xba\x02\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meshtastic.mqtt_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.geeksville.meshB\nMQTTProtosZ\"github.com/meshtastic/go/generated\252\002\024Meshtastic.Protobufs\272\002\000'
  _SERVICEENVELOPE._serialized_start=60
  _SERVICEENVELOPE._serialized_end=157
# @@protoc_insertion_point(module_scope)
