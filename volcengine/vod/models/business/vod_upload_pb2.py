# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: volcengine/vod/business/vod_upload.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from volcengine.vod.models.business import vod_common_pb2 as volcengine_dot_vod_dot_business_dot_vod__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(volcengine/vod/business/vod_upload.proto\x12\x1eVolcengine.Vod.Models.Business\x1a(volcengine/vod/business/vod_common.proto\"\xd3\x03\n\x12VodUrlUploadURLSet\x12\x11\n\tSourceUrl\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x0b\n\x03Md5\x18\x03 \x01(\t\x12\x12\n\nTemplateId\x18\x04 \x01(\t\x12\r\n\x05Title\x18\x05 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x06 \x01(\t\x12\x0c\n\x04Tags\x18\x07 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x08 \x01(\t\x12\x10\n\x08\x46ileName\x18\t \x01(\t\x12\x18\n\x10\x43lassificationId\x18\n \x01(\x03\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\x12\x15\n\rFileExtension\x18\x0c \x01(\t\x12\x1e\n\x16UrlEncryptionAlgorithm\x18\r \x01(\t\x12\x19\n\x11\x45nableLowPriority\x18\x0e \x01(\x08\x12\x62\n\x10\x43ustomURLHeaders\x18\x0f \x03(\x0b\x32H.Volcengine.Vod.Models.Business.VodUrlUploadURLSet.CustomURLHeadersEntry\x1a\x37\n\x15\x43ustomURLHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x12VodUrlResponseData\x12\x37\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.ValuePair\"-\n\tValuePair\x12\r\n\x05JobId\x18\x01 \x01(\t\x12\x11\n\tSourceUrl\x18\x02 \x01(\t\"R\n\x0cVodQueryData\x12\x42\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x34.Volcengine.Vod.Models.Business.VodQueryUploadResult\"p\n\x14VodQueryUploadResult\x12@\n\rMediaInfoList\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.VodURLSet\x12\x16\n\x0eNotExistJobIds\x18\x02 \x03(\t\"^\n\rVodCommitData\x12M\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32?.Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData\"\xa7\x01\n\x1fVodCommitUploadInfoResponseData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x41\n\nSourceInfo\x18\x02 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x03 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\"\xdb\x01\n\tVodURLSet\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\r\n\x05JobId\x18\x02 \x01(\t\x12\x11\n\tSourceUrl\x18\x03 \x01(\t\x12\r\n\x05State\x18\x04 \x01(\t\x12\x0b\n\x03Vid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x11\n\tAccountId\x18\x07 \x01(\t\x12\x41\n\nSourceInfo\x18\x08 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x14\n\x0c\x43\x61llbackArgs\x18\t \x01(\t\"`\n\x18VodApplyUploadInfoResult\x12\x44\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodApplyUploadInfoData\"a\n\x16VodApplyUploadInfoData\x12G\n\rUploadAddress\x18\x01 \x01(\x0b\x32\x30.Volcengine.Vod.Models.Business.VodUploadAddress\"\xc2\x01\n\x10VodUploadAddress\x12@\n\nStoreInfos\x18\x01 \x03(\x0b\x32,.Volcengine.Vod.Models.Business.VodStoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12\x43\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32-.Volcengine.Vod.Models.Business.VodHeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\".\n\x0cVodStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"+\n\rVodHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"b\n\x19VodCommitUploadInfoResult\x12\x45\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x37.Volcengine.Vod.Models.Business.VodCommitUploadInfoData\"\x89\x01\n\x17VodCommitUploadInfoData\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x11\n\tPosterUri\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x0b\n\x03Mid\x18\x04 \x01(\t\"\xf6\x02\n\x16VodUploadFunctionInput\x12\x14\n\x0cSnapshotTime\x18\x01 \x01(\x01\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x0c\n\x04Tags\x18\x03 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x04 \x01(\t\x12\x10\n\x08\x43\x61tegory\x18\x05 \x01(\t\x12\x12\n\nRecordType\x18\x06 \x01(\x05\x12\x0e\n\x06\x46ormat\x18\x07 \x01(\t\x12\x18\n\x10\x43lassificationId\x18\x08 \x01(\x05\x12\x12\n\nTemplateId\x18\t \x01(\t\x12\x0b\n\x03Vid\x18\n \x01(\t\x12\x0b\n\x03\x46id\x18\x0b \x01(\t\x12\x10\n\x08Language\x18\x0c \x01(\t\x12\x10\n\x08StoreUri\x18\r \x01(\t\x12\x0e\n\x06Source\x18\x0e \x01(\t\x12\x0b\n\x03Tag\x18\x0f \x01(\t\x12\x13\n\x0b\x41utoPublish\x18\x10 \x01(\x08\x12\x12\n\nActionType\x18\x11 \x01(\t\x12\x16\n\x0eIsHlsIndexOnly\x18\x12 \x01(\x08\x12\x14\n\x0cHlsMediaSize\x18\x13 \x01(\t\"h\n\x11VodUploadFunction\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x45\n\x05Input\x18\x02 \x01(\x0b\x32\x36.Volcengine.Vod.Models.Business.VodUploadFunctionInput\"\xc8\x01\n\x15\x43ommitUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x44\n\tFunctions\x18\x04 \x03(\x0b\x32\x31.Volcengine.Vod.Models.Business.VodUploadFunction\x12\x13\n\x0bGetMetaMode\x18\x05 \x01(\t\x12\x17\n\x0fVodUploadSource\x18\x06 \x01(\t\"\x95\x01\n\x15\x43ommitRequestBodyJson\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x12\n\nSessionKey\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x11\n\tFunctions\x18\x04 \x01(\t\x12\x13\n\x0bGetMetaMode\x18\x05 \x01(\t\x12\x17\n\x0fVodUploadSource\x18\x06 \x01(\t\"\xec\x01\n\x14\x41pplyUploadInfoParam\x12\x11\n\tSpaceName\x18\x01 \x01(\t\x12\x10\n\x08\x46ileType\x18\x02 \x01(\t\x12\x12\n\nSessionKey\x18\x03 \x01(\t\x12\x10\n\x08\x46ileSize\x18\x04 \x01(\x01\x12\x11\n\tMediaType\x18\x05 \x01(\t\x12\x0f\n\x07TosKeys\x18\x06 \x01(\t\x12\x15\n\rFileExtension\x18\x07 \x01(\t\x12\x12\n\nFilePrefix\x18\x08 \x01(\t\x12\x17\n\x0f\x46lushUploadMode\x18\t \x01(\x05\x12\x0b\n\x03Md5\x18\n \x01(\t\x12\x14\n\x0cStorageClass\x18\x0b \x01(\x05\"\x96\x01\n\x0e\x43ommitResponse\x12\x0b\n\x03Vid\x18\x01 \x01(\t\x12\x0b\n\x03Mid\x18\x02 \x01(\t\x12\x41\n\nSourceInfo\x18\x03 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x04 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x05 \x01(\t\")\n\x13VodUploadOptionInfo\x12\x12\n\nTemplateId\x18\x01 \x01(\t\"\x98\x02\n\x15VodUploadCallbackData\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x03 \x01(\t\x12\x0b\n\x03Vid\x18\x04 \x01(\t\x12\x0b\n\x03Mid\x18\x05 \x01(\t\x12\x11\n\tSpaceName\x18\x06 \x01(\t\x12\x41\n\nSourceInfo\x18\x07 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x08 \x01(\t\x12G\n\nOptionInfo\x18\t \x01(\x0b\x32\x33.Volcengine.Vod.Models.Business.VodUploadOptionInfo\"\xa1\x01\n\x10\x43\x61llbackResponse\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12\x11\n\tEventTime\x18\x03 \x01(\t\x12\x11\n\tEventType\x18\x04 \x01(\t\x12\x43\n\x04\x44\x61ta\x18\x05 \x01(\x0b\x32\x35.Volcengine.Vod.Models.Business.VodUploadCallbackData\"+\n\tStoreInfo\x12\x10\n\x08StoreUri\x18\x01 \x01(\t\x12\x0c\n\x04\x41uth\x18\x02 \x01(\t\"(\n\nHeaderPair\x12\x0b\n\x03Key\x18\x01 \x01(\t\x12\r\n\x05Value\x18\x02 \x01(\t\"\xb9\x01\n\rUploadAddress\x12=\n\nStoreInfos\x18\x01 \x03(\x0b\x32).Volcengine.Vod.Models.Business.StoreInfo\x12\x13\n\x0bUploadHosts\x18\x02 \x03(\t\x12@\n\x0cUploadHeader\x18\x03 \x03(\x0b\x32*.Volcengine.Vod.Models.Business.HeaderPair\x12\x12\n\nSessionKey\x18\x04 \x01(\t\"\xae\x01\n\x11\x46lushUploadResult\x12\x13\n\x0b\x46lushUpload\x18\x01 \x01(\x08\x12\x0b\n\x03Vid\x18\x02 \x01(\t\x12\x0b\n\x03Mid\x18\x03 \x01(\t\x12\x41\n\nSourceInfo\x18\x04 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.VodSourceInfo\x12\x11\n\tPosterUri\x18\x05 \x01(\t\x12\x14\n\x0c\x43\x61llbackArgs\x18\x06 \x01(\t\"\xb5\x01\n\rApplyResponse\x12\x44\n\rUploadAddress\x18\x01 \x01(\x0b\x32-.Volcengine.Vod.Models.Business.UploadAddress\x12L\n\x11\x46lushUploadResult\x18\x02 \x01(\x0b\x32\x31.Volcengine.Vod.Models.Business.FlushUploadResult\x12\x10\n\x08SDKParam\x18\x03 \x01(\t*B\n\x10StorageClassType\x12\x0b\n\x07\x44\x65\x66\x61ult\x10\x00\x12\x0c\n\x08Standard\x10\x01\x12\x0b\n\x07\x41rchive\x10\x02\x12\x06\n\x02IA\x10\x03\x42\xcd\x01\n)com.volcengine.service.vod.model.businessB\tVodUploadP\x01ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02 Volc\\Service\\Vod\\Models\\Business\xe2\x02#Volc\\Service\\Vod\\Models\\GPBMetadatab\x06proto3')

_STORAGECLASSTYPE = DESCRIPTOR.enum_types_by_name['StorageClassType']
StorageClassType = enum_type_wrapper.EnumTypeWrapper(_STORAGECLASSTYPE)
Default = 0
Standard = 1
Archive = 2
IA = 3


_VODURLUPLOADURLSET = DESCRIPTOR.message_types_by_name['VodUrlUploadURLSet']
_VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY = _VODURLUPLOADURLSET.nested_types_by_name['CustomURLHeadersEntry']
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
_VODUPLOADFUNCTIONINPUT = DESCRIPTOR.message_types_by_name['VodUploadFunctionInput']
_VODUPLOADFUNCTION = DESCRIPTOR.message_types_by_name['VodUploadFunction']
_COMMITUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['CommitUploadInfoParam']
_COMMITREQUESTBODYJSON = DESCRIPTOR.message_types_by_name['CommitRequestBodyJson']
_APPLYUPLOADINFOPARAM = DESCRIPTOR.message_types_by_name['ApplyUploadInfoParam']
_COMMITRESPONSE = DESCRIPTOR.message_types_by_name['CommitResponse']
_VODUPLOADOPTIONINFO = DESCRIPTOR.message_types_by_name['VodUploadOptionInfo']
_VODUPLOADCALLBACKDATA = DESCRIPTOR.message_types_by_name['VodUploadCallbackData']
_CALLBACKRESPONSE = DESCRIPTOR.message_types_by_name['CallbackResponse']
_STOREINFO = DESCRIPTOR.message_types_by_name['StoreInfo']
_HEADERPAIR = DESCRIPTOR.message_types_by_name['HeaderPair']
_UPLOADADDRESS = DESCRIPTOR.message_types_by_name['UploadAddress']
_FLUSHUPLOADRESULT = DESCRIPTOR.message_types_by_name['FlushUploadResult']
_APPLYRESPONSE = DESCRIPTOR.message_types_by_name['ApplyResponse']
VodUrlUploadURLSet = _reflection.GeneratedProtocolMessageType('VodUrlUploadURLSet', (_message.Message,), {

  'CustomURLHeadersEntry' : _reflection.GeneratedProtocolMessageType('CustomURLHeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY,
    '__module__' : 'volcengine.vod.business.vod_upload_pb2'
    # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet.CustomURLHeadersEntry)
    })
  ,
  'DESCRIPTOR' : _VODURLUPLOADURLSET,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlUploadURLSet)
  })
_sym_db.RegisterMessage(VodUrlUploadURLSet)
_sym_db.RegisterMessage(VodUrlUploadURLSet.CustomURLHeadersEntry)

VodUrlResponseData = _reflection.GeneratedProtocolMessageType('VodUrlResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODURLRESPONSEDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUrlResponseData)
  })
_sym_db.RegisterMessage(VodUrlResponseData)

ValuePair = _reflection.GeneratedProtocolMessageType('ValuePair', (_message.Message,), {
  'DESCRIPTOR' : _VALUEPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ValuePair)
  })
_sym_db.RegisterMessage(ValuePair)

VodQueryData = _reflection.GeneratedProtocolMessageType('VodQueryData', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryData)
  })
_sym_db.RegisterMessage(VodQueryData)

VodQueryUploadResult = _reflection.GeneratedProtocolMessageType('VodQueryUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _VODQUERYUPLOADRESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodQueryUploadResult)
  })
_sym_db.RegisterMessage(VodQueryUploadResult)

VodCommitData = _reflection.GeneratedProtocolMessageType('VodCommitData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitData)
  })
_sym_db.RegisterMessage(VodCommitData)

VodCommitUploadInfoResponseData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResponseData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESPONSEDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResponseData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResponseData)

VodURLSet = _reflection.GeneratedProtocolMessageType('VodURLSet', (_message.Message,), {
  'DESCRIPTOR' : _VODURLSET,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodURLSet)
  })
_sym_db.RegisterMessage(VodURLSet)

VodApplyUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFORESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoResult)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoResult)

VodApplyUploadInfoData = _reflection.GeneratedProtocolMessageType('VodApplyUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODAPPLYUPLOADINFODATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodApplyUploadInfoData)
  })
_sym_db.RegisterMessage(VodApplyUploadInfoData)

VodUploadAddress = _reflection.GeneratedProtocolMessageType('VodUploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADADDRESS,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadAddress)
  })
_sym_db.RegisterMessage(VodUploadAddress)

VodStoreInfo = _reflection.GeneratedProtocolMessageType('VodStoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODSTOREINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodStoreInfo)
  })
_sym_db.RegisterMessage(VodStoreInfo)

VodHeaderPair = _reflection.GeneratedProtocolMessageType('VodHeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _VODHEADERPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodHeaderPair)
  })
_sym_db.RegisterMessage(VodHeaderPair)

VodCommitUploadInfoResult = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoResult', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFORESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoResult)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoResult)

VodCommitUploadInfoData = _reflection.GeneratedProtocolMessageType('VodCommitUploadInfoData', (_message.Message,), {
  'DESCRIPTOR' : _VODCOMMITUPLOADINFODATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodCommitUploadInfoData)
  })
_sym_db.RegisterMessage(VodCommitUploadInfoData)

VodUploadFunctionInput = _reflection.GeneratedProtocolMessageType('VodUploadFunctionInput', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTIONINPUT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunctionInput)
  })
_sym_db.RegisterMessage(VodUploadFunctionInput)

VodUploadFunction = _reflection.GeneratedProtocolMessageType('VodUploadFunction', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADFUNCTION,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadFunction)
  })
_sym_db.RegisterMessage(VodUploadFunction)

CommitUploadInfoParam = _reflection.GeneratedProtocolMessageType('CommitUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _COMMITUPLOADINFOPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitUploadInfoParam)
  })
_sym_db.RegisterMessage(CommitUploadInfoParam)

CommitRequestBodyJson = _reflection.GeneratedProtocolMessageType('CommitRequestBodyJson', (_message.Message,), {
  'DESCRIPTOR' : _COMMITREQUESTBODYJSON,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitRequestBodyJson)
  })
_sym_db.RegisterMessage(CommitRequestBodyJson)

ApplyUploadInfoParam = _reflection.GeneratedProtocolMessageType('ApplyUploadInfoParam', (_message.Message,), {
  'DESCRIPTOR' : _APPLYUPLOADINFOPARAM,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyUploadInfoParam)
  })
_sym_db.RegisterMessage(ApplyUploadInfoParam)

CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMITRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CommitResponse)
  })
_sym_db.RegisterMessage(CommitResponse)

VodUploadOptionInfo = _reflection.GeneratedProtocolMessageType('VodUploadOptionInfo', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADOPTIONINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadOptionInfo)
  })
_sym_db.RegisterMessage(VodUploadOptionInfo)

VodUploadCallbackData = _reflection.GeneratedProtocolMessageType('VodUploadCallbackData', (_message.Message,), {
  'DESCRIPTOR' : _VODUPLOADCALLBACKDATA,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.VodUploadCallbackData)
  })
_sym_db.RegisterMessage(VodUploadCallbackData)

CallbackResponse = _reflection.GeneratedProtocolMessageType('CallbackResponse', (_message.Message,), {
  'DESCRIPTOR' : _CALLBACKRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.CallbackResponse)
  })
_sym_db.RegisterMessage(CallbackResponse)

StoreInfo = _reflection.GeneratedProtocolMessageType('StoreInfo', (_message.Message,), {
  'DESCRIPTOR' : _STOREINFO,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.StoreInfo)
  })
_sym_db.RegisterMessage(StoreInfo)

HeaderPair = _reflection.GeneratedProtocolMessageType('HeaderPair', (_message.Message,), {
  'DESCRIPTOR' : _HEADERPAIR,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.HeaderPair)
  })
_sym_db.RegisterMessage(HeaderPair)

UploadAddress = _reflection.GeneratedProtocolMessageType('UploadAddress', (_message.Message,), {
  'DESCRIPTOR' : _UPLOADADDRESS,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.UploadAddress)
  })
_sym_db.RegisterMessage(UploadAddress)

FlushUploadResult = _reflection.GeneratedProtocolMessageType('FlushUploadResult', (_message.Message,), {
  'DESCRIPTOR' : _FLUSHUPLOADRESULT,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.FlushUploadResult)
  })
_sym_db.RegisterMessage(FlushUploadResult)

ApplyResponse = _reflection.GeneratedProtocolMessageType('ApplyResponse', (_message.Message,), {
  'DESCRIPTOR' : _APPLYRESPONSE,
  '__module__' : 'volcengine.vod.business.vod_upload_pb2'
  # @@protoc_insertion_point(class_scope:Volcengine.Vod.Models.Business.ApplyResponse)
  })
_sym_db.RegisterMessage(ApplyResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)com.volcengine.service.vod.model.businessB\tVodUploadP\001ZAgithub.com/volcengine/volc-sdk-golang/service/vod/models/business\240\001\001\330\001\001\302\002\000\312\002 Volc\\Service\\Vod\\Models\\Business\342\002#Volc\\Service\\Vod\\Models\\GPBMetadata'
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._options = None
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_options = b'8\001'
  _STORAGECLASSTYPE._serialized_start=4483
  _STORAGECLASSTYPE._serialized_end=4549
  _VODURLUPLOADURLSET._serialized_start=119
  _VODURLUPLOADURLSET._serialized_end=586
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_start=531
  _VODURLUPLOADURLSET_CUSTOMURLHEADERSENTRY._serialized_end=586
  _VODURLRESPONSEDATA._serialized_start=588
  _VODURLRESPONSEDATA._serialized_end=665
  _VALUEPAIR._serialized_start=667
  _VALUEPAIR._serialized_end=712
  _VODQUERYDATA._serialized_start=714
  _VODQUERYDATA._serialized_end=796
  _VODQUERYUPLOADRESULT._serialized_start=798
  _VODQUERYUPLOADRESULT._serialized_end=910
  _VODCOMMITDATA._serialized_start=912
  _VODCOMMITDATA._serialized_end=1006
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_start=1009
  _VODCOMMITUPLOADINFORESPONSEDATA._serialized_end=1176
  _VODURLSET._serialized_start=1179
  _VODURLSET._serialized_end=1398
  _VODAPPLYUPLOADINFORESULT._serialized_start=1400
  _VODAPPLYUPLOADINFORESULT._serialized_end=1496
  _VODAPPLYUPLOADINFODATA._serialized_start=1498
  _VODAPPLYUPLOADINFODATA._serialized_end=1595
  _VODUPLOADADDRESS._serialized_start=1598
  _VODUPLOADADDRESS._serialized_end=1792
  _VODSTOREINFO._serialized_start=1794
  _VODSTOREINFO._serialized_end=1840
  _VODHEADERPAIR._serialized_start=1842
  _VODHEADERPAIR._serialized_end=1885
  _VODCOMMITUPLOADINFORESULT._serialized_start=1887
  _VODCOMMITUPLOADINFORESULT._serialized_end=1985
  _VODCOMMITUPLOADINFODATA._serialized_start=1988
  _VODCOMMITUPLOADINFODATA._serialized_end=2125
  _VODUPLOADFUNCTIONINPUT._serialized_start=2128
  _VODUPLOADFUNCTIONINPUT._serialized_end=2502
  _VODUPLOADFUNCTION._serialized_start=2504
  _VODUPLOADFUNCTION._serialized_end=2608
  _COMMITUPLOADINFOPARAM._serialized_start=2611
  _COMMITUPLOADINFOPARAM._serialized_end=2811
  _COMMITREQUESTBODYJSON._serialized_start=2814
  _COMMITREQUESTBODYJSON._serialized_end=2963
  _APPLYUPLOADINFOPARAM._serialized_start=2966
  _APPLYUPLOADINFOPARAM._serialized_end=3202
  _COMMITRESPONSE._serialized_start=3205
  _COMMITRESPONSE._serialized_end=3355
  _VODUPLOADOPTIONINFO._serialized_start=3357
  _VODUPLOADOPTIONINFO._serialized_end=3398
  _VODUPLOADCALLBACKDATA._serialized_start=3401
  _VODUPLOADCALLBACKDATA._serialized_end=3681
  _CALLBACKRESPONSE._serialized_start=3684
  _CALLBACKRESPONSE._serialized_end=3845
  _STOREINFO._serialized_start=3847
  _STOREINFO._serialized_end=3890
  _HEADERPAIR._serialized_start=3892
  _HEADERPAIR._serialized_end=3932
  _UPLOADADDRESS._serialized_start=3935
  _UPLOADADDRESS._serialized_end=4120
  _FLUSHUPLOADRESULT._serialized_start=4123
  _FLUSHUPLOADRESULT._serialized_end=4297
  _APPLYRESPONSE._serialized_start=4300
  _APPLYRESPONSE._serialized_end=4481
# @@protoc_insertion_point(module_scope)
