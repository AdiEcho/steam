# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_video.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19steammessages_video.proto\x1a\x18steammessages_base.proto\x1a steammessages_unified_base.proto\"K\n CVideo_ClientGetVideoURL_Request\x12\x10\n\x08video_id\x18\x01 \x01(\x04\x12\x15\n\rclient_cellid\x18\x02 \x01(\r\"H\n!CVideo_ClientGetVideoURL_Response\x12\x10\n\x08video_id\x18\x01 \x01(\x04\x12\x11\n\tvideo_url\x18\x02 \x01(\t\"\xf2\x01\n\rVideoBookmark\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12$\n\x1cplayback_position_in_seconds\x18\x02 \x01(\r\x12\x16\n\x0evideo_track_id\x18\x03 \x01(\x04\x12\x16\n\x0e\x61udio_track_id\x18\x04 \x01(\x04\x12\x1a\n\x12timedtext_track_id\x18\x05 \x01(\x04\x12\x15\n\rlast_modified\x18\x06 \x01(\r\x12&\n\x17hide_from_watch_history\x18\x07 \x01(\x08:\x05\x66\x61lse\x12 \n\x11hide_from_library\x18\x08 \x01(\x08:\x05\x66\x61lse\"I\n$CVideo_SetVideoBookmark_Notification\x12!\n\tbookmarks\x18\x01 \x03(\x0b\x32\x0e.VideoBookmark\"I\n CVideo_GetVideoBookmarks_Request\x12\x0e\n\x06\x61ppids\x18\x01 \x03(\r\x12\x15\n\rupdated_since\x18\x02 \x01(\r\"F\n!CVideo_GetVideoBookmarks_Response\x12!\n\tbookmarks\x18\x01 \x03(\x0b\x32\x0e.VideoBookmark\":\n CVideo_UnlockedH264_Notification\x12\x16\n\x0e\x65ncryption_key\x18\x01 \x01(\x0c\"Q\n(CFovasVideo_ClientGetOPFSettings_Request\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x15\n\rclient_cellid\x18\x02 \x01(\r\"Q\n)CFovasVideo_ClientGetOPFSettings_Response\x12\x0e\n\x06\x61pp_id\x18\x01 \x01(\r\x12\x14\n\x0copf_settings\x18\x02 \x01(\t2\x87\x02\n\x05Video\x12Z\n\x11\x43lientGetVideoURL\x12!.CVideo_ClientGetVideoURL_Request\x1a\".CVideo_ClientGetVideoURL_Response\x12\x46\n\x10SetVideoBookmark\x12%.CVideo_SetVideoBookmark_Notification\x1a\x0b.NoResponse\x12Z\n\x11GetVideoBookmarks\x12!.CVideo_GetVideoBookmarks_Request\x1a\".CVideo_GetVideoBookmarks_Response2Y\n\x0bVideoClient\x12\x44\n\x12NotifyUnlockedH264\x12!.CVideo_UnlockedH264_Notification\x1a\x0b.NoResponse\x1a\x04\xc0\xb5\x18\x02\x32{\n\nFovasVideo\x12m\n\x14\x43lientGetOPFSettings\x12).CFovasVideo_ClientGetOPFSettings_Request\x1a*.CFovasVideo_ClientGetOPFSettings_ResponseB\x03\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steammessages_video_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\220\001\001'
  _globals['_VIDEOCLIENT']._options = None
  _globals['_VIDEOCLIENT']._serialized_options = b'\300\265\030\002'
  _globals['_CVIDEO_CLIENTGETVIDEOURL_REQUEST']._serialized_start=89
  _globals['_CVIDEO_CLIENTGETVIDEOURL_REQUEST']._serialized_end=164
  _globals['_CVIDEO_CLIENTGETVIDEOURL_RESPONSE']._serialized_start=166
  _globals['_CVIDEO_CLIENTGETVIDEOURL_RESPONSE']._serialized_end=238
  _globals['_VIDEOBOOKMARK']._serialized_start=241
  _globals['_VIDEOBOOKMARK']._serialized_end=483
  _globals['_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION']._serialized_start=485
  _globals['_CVIDEO_SETVIDEOBOOKMARK_NOTIFICATION']._serialized_end=558
  _globals['_CVIDEO_GETVIDEOBOOKMARKS_REQUEST']._serialized_start=560
  _globals['_CVIDEO_GETVIDEOBOOKMARKS_REQUEST']._serialized_end=633
  _globals['_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE']._serialized_start=635
  _globals['_CVIDEO_GETVIDEOBOOKMARKS_RESPONSE']._serialized_end=705
  _globals['_CVIDEO_UNLOCKEDH264_NOTIFICATION']._serialized_start=707
  _globals['_CVIDEO_UNLOCKEDH264_NOTIFICATION']._serialized_end=765
  _globals['_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST']._serialized_start=767
  _globals['_CFOVASVIDEO_CLIENTGETOPFSETTINGS_REQUEST']._serialized_end=848
  _globals['_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE']._serialized_start=850
  _globals['_CFOVASVIDEO_CLIENTGETOPFSETTINGS_RESPONSE']._serialized_end=931
  _globals['_VIDEO']._serialized_start=934
  _globals['_VIDEO']._serialized_end=1197
  _globals['_VIDEOCLIENT']._serialized_start=1199
  _globals['_VIDEOCLIENT']._serialized_end=1288
  _globals['_FOVASVIDEO']._serialized_start=1290
  _globals['_FOVASVIDEO']._serialized_end=1413
_builder.BuildServices(DESCRIPTOR, 'steammessages_video_pb2', _globals)
# @@protoc_insertion_point(module_scope)
