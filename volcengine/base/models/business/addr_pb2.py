# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: live/business/addr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18live/business/addr.proto\x12\x1fVolcengine.Live.Models.Business\"R\n\x15GeneratePlayURLResult\x12\x39\n\x07URLList\x18\x01 \x03(\x0b\x32(.Volcengine.Live.Models.Business.PlayURL\"C\n\x07PlayURL\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\x0b\n\x03\x43\x44N\x18\x02 \x01(\t\x12\x10\n\x08Protocol\x18\x03 \x01(\t\x12\x0c\n\x04Type\x18\x04 \x01(\t\"\xbf\x01\n\x15GeneratePushURLResult\x12\x13\n\x0bPushURLList\x18\x01 \x03(\t\x12G\n\x11PushURLListDetail\x18\x02 \x03(\x0b\x32,.Volcengine.Live.Models.Business.PushURLItem\x12\x18\n\x10TsOverSrtURLList\x18\x03 \x03(\t\x12\x1a\n\x12RtmpOverSrtURLList\x18\x04 \x03(\t\x12\x12\n\nRtmURLList\x18\x05 \x03(\t\"A\n\x0bPushURLItem\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\x11\n\tDomainApp\x18\x02 \x01(\t\x12\x12\n\nStreamSign\x18\x03 \x01(\tB\xcc\x01\n*com.volcengine.service.live.model.businessB\x04\x41\x64\x64rP\x01ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02!Volc\\Service\\Live\\Models\\Business\xe2\x02$Volc\\Service\\Live\\Models\\GPBMetadatab\x06proto3')



_GENERATEPLAYURLRESULT = DESCRIPTOR.message_types_by_name['GeneratePlayURLResult']
_PLAYURL = DESCRIPTOR.message_types_by_name['PlayURL']
_GENERATEPUSHURLRESULT = DESCRIPTOR.message_types_by_name['GeneratePushURLResult']
_PUSHURLITEM = DESCRIPTOR.message_types_by_name['PushURLItem']
GeneratePlayURLResult = _reflection.GeneratedProtocolMessageType('GeneratePlayURLResult', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEPLAYURLRESULT,
  '__module__' : 'live.business.addr_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.GeneratePlayURLResult)
  })
_sym_db.RegisterMessage(GeneratePlayURLResult)

PlayURL = _reflection.GeneratedProtocolMessageType('PlayURL', (_message.Message,), {
  'DESCRIPTOR' : _PLAYURL,
  '__module__' : 'live.business.addr_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.PlayURL)
  })
_sym_db.RegisterMessage(PlayURL)

GeneratePushURLResult = _reflection.GeneratedProtocolMessageType('GeneratePushURLResult', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEPUSHURLRESULT,
  '__module__' : 'live.business.addr_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.GeneratePushURLResult)
  })
_sym_db.RegisterMessage(GeneratePushURLResult)

PushURLItem = _reflection.GeneratedProtocolMessageType('PushURLItem', (_message.Message,), {
  'DESCRIPTOR' : _PUSHURLITEM,
  '__module__' : 'live.business.addr_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Live.Models.Business.PushURLItem)
  })
_sym_db.RegisterMessage(PushURLItem)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n*com.volcengine.service.live.model.businessB\004AddrP\001ZBgithub.com/volcengine/volc-sdk-golang/service/live/models/business\240\001\001\330\001\001\302\002\000\312\002!Volc\\Service\\Live\\Models\\Business\342\002$Volc\\Service\\Live\\Models\\GPBMetadata'
  _GENERATEPLAYURLRESULT._serialized_start=61
  _GENERATEPLAYURLRESULT._serialized_end=143
  _PLAYURL._serialized_start=145
  _PLAYURL._serialized_end=212
  _GENERATEPUSHURLRESULT._serialized_start=215
  _GENERATEPUSHURLRESULT._serialized_end=406
  _PUSHURLITEM._serialized_start=408
  _PUSHURLITEM._serialized_end=473
# @@protoc_insertion_point(module_scope)
