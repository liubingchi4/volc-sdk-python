# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vod/business/vod_upload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.vod.models.business import vod_common_pb2 as vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dvod/business/vod_upload.proto\x12\x1eVolcengine.Vod.Models.Business\x1a\x1dvod/business/vod_common.proto\"\xce\x01\n\x12VodUrlUploadURLSet\x12\x11\n\tSourceUrl\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x0b\n\x03Md5\x18\x03 \x01(\t\x12\x12\n\nTemplateId\x18\x04 \x01(\t\x12\r\n\x05Title\x18\x05 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04Tags\x18\x07 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x08 \x01(\t\x12\x10\n\x08\x46ileName\x18\t \x01(\t\x12\x18\n\x10\x43lassificationId\x18\n \x01(\x03\"M\n\x12VodUrlResponseData\x12\x37\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.ValuePair\"-\n\tValuePair\x12\r\n\x05JobId\x18\x01 \x01(\t\x12\x11\n\tSourceUrl\x18\x02 \x01(\t\"R\n\x0cVodQueryData\x12\x42\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x34.Volcengine.Vod.Models.Business.VodQueryUploadResult\"p\n\x14VodQueryUploadResult\x12@\n\rMediaInfoList\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.VodURLSet\x12\x16\n\x0eNotExistJobIds\x18\x02 \x03(\t\"^\n\rVodCommitData\x12M\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32?.Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData\"\xa7\x01\n\x1fVodCommitUploadInfoResponseData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x41\n\nSourceInfo\x18\x02 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x03 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\"\xc5\x01\n\tVodURLSet\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\r\n\x05JobId\x18\x02 \x01(\t\x12\x11\n\tSourceUrl\x18\x03 \x01(\t\x12\r\n\x05State\x18\x04 \x01(\t\x12\x0b\n\x03Vid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x11\n\tAccountId\x18\x07 \x01(\t\x12\x41\n\nSourceInfo\x18\x08 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\"`\n\x18VodApplyUploadInfoResult\x12\x44\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodApplyUploadInfoData\"a\n\x16VodApplyUploadInfoData\x12G\n\rUploadAddress\x18\x01 \x01(\x0b\x32\x30.Volcengine.Vod.Models.Business.VodUploadAddress\"\xc2\x01\n\x10VodUploadAddress\x12@\n\nStoreInfos\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.VodStoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12\x43\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.VodHeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\".\n\x0cVodStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"+\n\rVodHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"b\n\x19VodCommitUploadInfoResult\x12\x45\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x37.Volcengine.Vod.Models.Business.VodCommitUploadInfoData\"\x89\x01\n\x17VodCommitUploadInfoData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x11\n\tPosterUri\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x0b\n\x03Mid\x18\x04 \x01(\tB\xcd\x01\n)com.volcengine.service.vod.model.businessB\tVodUploadP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')



_VODURLUPLOADURLSET = DESCRIPTOR.message_types_by_name['VodUrlUploadURLSet']
_VODURLRESPONSEDATA = DESCRIPTOR.message_types_by_name['VodUrlResponseData']
_VALUEPAIR = DESCRIPTOR.message_types_by_name['ValuePair']
_VODQUERYDATA = DESCRIPTOR.message_types_by_name['VodQueryData']
_VODQUERYUPLOADRESULT = DESCRIPTOR.message_types_by_name['VodQueryUploadResult']
_VODCOMMITDATA = DESCRIPTOR.message_types_by_name['VodCommitData']
_VODCOMMITUPLOADINFORESPONSEDATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResponseData']
_VODURLSET = DESCRIPTOR.message_types_by_name['VodURLSet']
_VODAPPLYUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoResult']
_VODAPPLYUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodApplyUploadInfoData']
_VODUPLOADADDRESS = DESCRIPTOR.message_types_by_name['VodUploadAddress']
_VODSTOREINFO = DESCRIPTOR.message_types_by_name['VodStoreInfo']
_VODHEADERPAIR = DESCRIPTOR.message_types_by_name['VodHeaderPair']
_VODCOMMITUPLOADINFORESULT = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoResult']
_VODCOMMITUPLOADINFODATA = DESCRIPTOR.message_types_by_name['VodCommitUploadInfoData']
VodUrlUploadURLSet = _reflection.GeneratedProtocolMessageType('VodUrlUploadURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLUPLOADURLSET,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet)
  })
_sym_db.RegisterMessage(VodUrlUploadURLSet)

VodUrlResponseData = _reflection.GeneratedProtocolMessageType('VodUrlResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODURLRESPONSEDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlResponseData)
  })
_sym_db.RegisterMessage(VodUrlResponseData)

ValuePair = _reflection.GeneratedProtocolMessageType('ValuePair', (_message.Message,), {
  'DESCRIPTOR' : _VALUEPAIR,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ValuePair)
  })
_sym_db.RegisterMessage(ValuePair)

VodQueryData = _reflection.GeneratedProtocolMessageType('VodQueryData', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryData)
  })
_sym_db.RegisterMessage(VodQueryData)

VodQueryUploadResult = _reflection.GeneratedProtocolMessageType('VodQueryUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYUPLOADRESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryUploadResult)
  })
_sym_db.RegisterMessage(VodQueryUploadResult)

VodCommitData = _reflection.GeneratedProtocolMessageType('VodCommitData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitData)
  })
_sym_db.RegisterMessage(VodCommitData)

VodCommitUploadInfoResponseData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESPONSEDATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResponseData)

VodURLSet = _reflection.GeneratedProtocolMessageType('VodURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLSET,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodURLSet)
  })
_sym_db.RegisterMessage(VodURLSet)

VodApplyUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFORESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoResult)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoResult)

VodApplyUploadInfoData = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFODATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoData)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoData)

VodUploadAddress = _reflection.GeneratedProtocolMessageType('VodUploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADADDRESS,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadAddress)
  })
_sym_db.RegisterMessage(VodUploadAddress)

VodStoreInfo = _reflection.GeneratedProtocolMessageType('VodStoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSTOREINFO,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodStoreInfo)
  })
_sym_db.RegisterMessage(VodStoreInfo)

VodHeaderPair = _reflection.GeneratedProtocolMessageType('VodHeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _VODHEADERPAIR,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodHeaderPair)
  })
_sym_db.RegisterMessage(VodHeaderPair)

VodCommitUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESULT,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResult)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResult)

VodCommitUploadInfoData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFODATA,
  '__module__' : 'vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\tVodUploadP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _VODURLUPLOADURLSET._serialized_start=97
  _VODURLUPLOADURLSET._serialized_end=303
  _VODURLRESPONSEDATA._serialized_start=305
  _VODURLRESPONSEDATA._serialized_end=382
  _VALUEPAIR._serialized_start=384
  _VALUEPAIR._serialized_end=429
  _VODQUERYDATA._serialized_start=431
  _VODQUERYDATA._serialized_end=513
  _VODQUERYUPLOADRESULT._serialized_start=515
  _VODQUERYUPLOADRESULT._serialized_end=627
  _VODCOMMITDATA._serialized_start=629
  _VODCOMMITDATA._serialized_end=723
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_start=726
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_end=893
  _VODURLSET._serialized_start=896
  _VODURLSET._serialized_end=1093
  _VODAPPLYUPLOADINFORESULT._serialized_start=1095
  _VODAPPLYUPLOADINFORESULT._serialized_end=1191
  _VODAPPLYUPLOADINFODATA._serialized_start=1193
  _VODAPPLYUPLOADINFODATA._serialized_end=1290
  _VODUPLOADADDRESS._serialized_start=1293
  _VODUPLOADADDRESS._serialized_end=1487
  _VODSTOREINFO._serialized_start=1489
  _VODSTOREINFO._serialized_end=1535
  _VODHEADERPAIR._serialized_start=1537
  _VODHEADERPAIR._serialized_end=1580
  _VODCOMMITUPLOADINFORESULT._serialized_start=1582
  _VODCOMMITUPLOADINFORESULT._serialized_end=1680
  _VODCOMMITUPLOADINFODATA._serialized_start=1683
  _VODCOMMITUPLOADINFODATA._serialized_end=1820
# @@protoc_insertion_point(module_scope)
