# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: live/business/pull_to_push.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.live.models.business import snapshot_manage_pb2 as live_dot_business_dot_snapshot__manage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n live/business/pull_to_push.proto\x12\x1fVolcengine.Live.Models.Business\x1a#live/business/snapshot_manage.proto\",\n\x1a\x43reatePullToPushTaskResult\x12\x0e\n\x06TaskId\x18\x01 \x01(\t\"\x98\x01\n\x18ListPullToPushTaskResult\x12;\n\x04List\x18\x01 \x03(\x0b\x32-.Volcengine.Live.Models.Business.TaskInfoItem\x12?\n\nPagination\x18\x02 \x01(\x0b\x32+.Volcengine.Live.Models.Business.Pagination\"\xdf\x01\n\x0cTaskInfoItem\x12\r\n\x05Title\x18\x01 \x01(\t\x12\x0e\n\x06TaskId\x18\x02 \x01(\t\x12\x11\n\tStartTime\x18\x03 \x01(\t\x12\x0f\n\x07\x45ndTime\x18\x04 \x01(\t\x12\x13\n\x0b\x43\x61llbackURL\x18\x05 \x01(\t\x12\x0c\n\x04Type\x18\x06 \x01(\x05\x12\x11\n\tCycleMode\x18\x07 \x01(\x05\x12\x0f\n\x07\x44stAddr\x18\x08 \x01(\t\x12\x0f\n\x07SrcAddr\x18\t \x01(\t\x12\x10\n\x08SrcAddrS\x18\n \x03(\t\x12\x0e\n\x06Status\x18\x0b \x01(\t\x12\x12\n\nTaskStatus\x18\x0c \x01(\x05\x42\xd6\x01\n*com.volcengine.service.live.model.businessB\x0ePullToPushTaskP\x01ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02!Volc\\Service\\Live\\Models\\Business\xe2\x02$Volc\\Service\\Live\\Models\\GPBMetadatab\x06proto3')



_CREATEPULLTOPUSHTASKRESULT = DESCRIPTOR.message_types_by_name['CreatePullToPushTaskResult']
_LISTPULLTOPUSHTASKRESULT = DESCRIPTOR.message_types_by_name['ListPullToPushTaskResult']
_TASKINFOITEM = DESCRIPTOR.message_types_by_name['TaskInfoItem']
CreatePullToPushTaskResult = _reflection.GeneratedProtocolMessageType('CreatePullToPushTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPULLTOPUSHTASKRESULT,
  '__module__' : 'live.business.pull_to_push_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.CreatePullToPushTaskResult)
  })
_sym_db.RegisterMessage(CreatePullToPushTaskResult)

ListPullToPushTaskResult = _reflection.GeneratedProtocolMessageType('ListPullToPushTaskResult', (_message.Message,), {
  'DESCRIPTOR' : _LISTPULLTOPUSHTASKRESULT,
  '__module__' : 'live.business.pull_to_push_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.ListPullToPushTaskResult)
  })
_sym_db.RegisterMessage(ListPullToPushTaskResult)

TaskInfoItem = _reflection.GeneratedProtocolMessageType('TaskInfoItem', (_message.Message,), {
  'DESCRIPTOR' : _TASKINFOITEM,
  '__module__' : 'live.business.pull_to_push_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.TaskInfoItem)
  })
_sym_db.RegisterMessage(TaskInfoItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.volcengine.service.live.model.businessB\016PullToPushTaskP\001ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\240\001\001\330\001\001\302\002\000\312\002!Volc\\Service\\Live\\Models\\Business\342\002$Volc\\Service\\Live\\Models\\GPBMetadata'
  _CREATEPULLTOPUSHTASKRESULT._serialized_start=106
  _CREATEPULLTOPUSHTASKRESULT._serialized_end=150
  _LISTPULLTOPUSHTASKRESULT._serialized_start=153
  _LISTPULLTOPUSHTASKRESULT._serialized_end=305
  _TASKINFOITEM._serialized_start=308
  _TASKINFOITEM._serialized_end=531
# @@protoc_insertion_point(module_scope)
