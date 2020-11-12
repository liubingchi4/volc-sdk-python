
# Code generated by protoc-gen-volcengine-sdk
# source: VodMediaService
# DO NOT EDIT!
# coding:utf-8

from __future__ import print_function
import os
import threading
import time
from zlib import crc32
from google.protobuf.json_format import *
from volcengine.models.vod.request.request_vod_pb2 import *
from volcengine.models.vod.response.response_vod_pb2 import *

#
# Generated from protobuf service <code>VodMediaService</code>
#
from volcengine.vod.VodService import VodService


class VodMediaService(VodService):

    #
    # UpdateVideoInfo.
    #
    # @param request VodUpdateVideoInfoRequest
    # @return VodUpdateVideoInfoResponse
    # @raise Exception
    def update_video_info (self, request: VodUpdateVideoInfoRequest) -> VodUpdateVideoInfoResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            res = self.get("UpdateVideoInfo", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateVideoInfoResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateVideoInfoResponse(), True)

    #
    # UpdateVideoPublishStatus.
    #
    # @param request VodUpdateVideoPublishStatusRequest
    # @return VodUpdateVideoPublishStatusResponse
    # @raise Exception
    def update_video_publish_status (self, request: VodUpdateVideoPublishStatusRequest) -> VodUpdateVideoPublishStatusResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            res = self.get("UpdateVideoPublishStatus", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodUpdateVideoPublishStatusResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodUpdateVideoPublishStatusResponse(), True)

    #
    # GetVideoInfos.
    #
    # @param request VodGetVideoInfosRequest
    # @return VodGetVideoInfosResponse
    # @raise Exception
    def get_video_infos (self, request: VodGetVideoInfosRequest) -> VodGetVideoInfosResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            print(jsonData)
            params = json.loads(jsonData)
            res = self.get("GetVideoInfos", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetVideoInfosResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetVideoInfosResponse(), True)

    #
    # GetRecommendedPoster.
    #
    # @param request VodGetRecommendedPosterRequest
    # @return VodGetRecommendedPosterResponse
    # @raise Exception
    def get_recommended_poster (self, request: VodGetRecommendedPosterRequest) -> VodGetRecommendedPosterResponse:
        try:
            jsonData = MessageToJson(request, False, True)
            params = json.loads(jsonData)
            res = self.get("GetRecommendedPoster", params)
        except Exception as Argument:
            try:
                resp = Parse(Argument.__str__(), VodGetRecommendedPosterResponse(), True)
            except Exception:
                raise Argument
            else:
                raise Exception(resp.ResponseMetadata.Error.Code)
        else:
            return Parse(res, VodGetRecommendedPosterResponse(), True)

# end of service interface
