# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webuimessages_gamerecording.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.enums_pb2 as enums__pb2
import steam.protobufs.steammessages_base_pb2 as steammessages__base__pb2
import steam.protobufs.webuimessages_base_pb2 as webuimessages__base__pb2
import steam.protobufs.webuimessages_gamerecordingfiles_pb2 as webuimessages__gamerecordingfiles__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!webuimessages_gamerecording.proto\x1a\x0b\x65nums.proto\x1a\x18steammessages_base.proto\x1a\x18webuimessages_base.proto\x1a&webuimessages_gamerecordingfiles.proto\"3\n1CGameRecording_GetAppsWithBackgroundVideo_Request\"\xe8\x02\n2CGameRecording_GetAppsWithBackgroundVideo_Response\x12\x45\n\x04\x61pps\x18\x01 \x03(\x0b\x32\x37.CGameRecording_GetAppsWithBackgroundVideo_Response.App\x1a\xea\x01\n\x03\x41pp\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x1e\n\x16most_recent_start_time\x18\x02 \x01(\r\x12I\n\x0erecording_type\x18\x03 \x01(\x0e\x32\x13.EGameRecordingType:\x1ck_EGameRecordingType_Unknown\x12\x1e\n\x16video_duration_seconds\x18\x04 \x01(\x01\x12!\n\x19timeline_duration_seconds\x18\x05 \x01(\x01\x12\x11\n\tis_active\x18\x06 \x01(\x08\x12\x11\n\tfile_size\x18\x07 \x01(\x04\"<\n)CGameRecording_GetTimelinesForApp_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"`\n*CGameRecording_GetTimelinesForApp_Response\x12\x32\n\ttimelines\x18\x01 \x03(\x0b\x32\x1f.CGameRecordingTimelineMetadata\"=\n*CGameRecording_GetTimelinesForClip_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\"\x9a\x01\n+CGameRecording_GetTimelinesForClip_Response\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x32\n\ttimelines\x18\x02 \x03(\x0b\x32\x1f.CGameRecordingTimelineMetadata\x12&\n\x1e\x66irst_timeline_start_offset_ms\x18\x03 \x01(\x04\"\xf1\x01\n\"CGameRecording_QueryPhases_Request\x12\x0c\n\x04page\x18\x01 \x01(\r\x12\r\n\x05\x63ount\x18\x02 \x01(\r\x12\x15\n\rfilter_gameid\x18\n \x01(\x04\x12\x1c\n\x14\x66ilter_search_string\x18\x0b \x01(\t\x12<\n\x0b\x66ilter_tags\x18\x0c \x03(\x0b\x32\'.CGameRecording_QueryPhases_Request.Tag\x12\x17\n\x0f\x66ilter_phase_id\x18\r \x01(\t\x1a\"\n\x03Tag\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x9d\x05\n#CGameRecording_QueryPhases_Response\x12:\n\x06phases\x18\x01 \x03(\x0b\x32*.CGameRecording_QueryPhases_Response.Phase\x12\x13\n\x0btotal_count\x18\x02 \x01(\r\x1a\xa4\x04\n\x05Phase\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x15\n\rdate_recorded\x18\x05 \x01(\r\x12\x13\n\x0b\x64uration_ms\x18\x06 \x01(\x04\x12\x1b\n\x04tags\x18\x07 \x03(\x0b\x32\r.CTimelineTag\x12%\n\x0e\x63ontained_tags\x18\x08 \x03(\x0b\x32\r.CTimelineTag\x12\\\n\x14\x62\x61\x63kground_recording\x18\t \x01(\x0b\x32>.CGameRecording_QueryPhases_Response.Phase.BackgroundRecording\x12\x10\n\x08\x63lip_ids\x18\n \x03(\t\x12=\n\x04type\x18\x0b \x01(\x0e\x32\x11.EPhaseResultType:\x1ck_EPhaseResultType_Automatic\x12\x10\n\x08start_ms\x18\x0c \x01(\x04\x12\x13\n\x0bscreenshots\x18\r \x03(\r\x12\x0e\n\x06\x61\x63tive\x18\x0e \x01(\x08\x12\x10\n\x08phase_id\x18\x0f \x01(\t\x12+\n\x12significant_events\x18\x10 \x03(\x0b\x32\x0f.CTimelineEntry\x12$\n\nattributes\x18\x11 \x03(\x0b\x32\x10.CPhaseAttribute\x1aO\n\x13\x42\x61\x63kgroundRecording\x12\x13\n\x0btimeline_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x04\"1\n\x1e\x43GameRecording_GetTags_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\">\n\x1f\x43GameRecording_GetTags_Response\x12\x1b\n\x04tags\x18\x01 \x03(\x0b\x32\r.CTimelineTag\"+\n)CGameRecording_GetEnoughDiskSpace_Request\"B\n*CGameRecording_GetEnoughDiskSpace_Response\x12\x14\n\x0c\x65nough_space\x18\x01 \x01(\x08\".\n,CGameRecording_GetAvailableDiskSpace_Request\"=\n-CGameRecording_GetAvailableDiskSpace_Response\x12\x0c\n\x04size\x18\x01 \x01(\x01\"\xe4\x01\n+CGameRecording_TimelineChanged_Notification\x12\x66\n\x11notification_type\x18\x01 \x01(\x0e\x32 .ETimelineChangeNotificationType:)k_ETimelineChangeNotificationType_Started\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x0f\n\x07game_id\x18\x03 \x01(\x04\x12\x12\n\nstart_time\x18\x04 \x01(\r\x12\x13\n\x0b\x64uration_ms\x18\x05 \x01(\x04\"\xdd\x02\n3CGameRecording_RecordingSessionChanged_Notification\x12v\n\x11notification_type\x18\x01 \x01(\x0e\x32(.ERecordingSessionChangeNotificationType:1k_ERecordingSessionChangeNotificationType_Started\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x0f\n\x07game_id\x18\x04 \x01(\x04\x12\x12\n\nsession_id\x18\x05 \x01(\t\x12\x14\n\x0cstart_offset\x18\x06 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x07 \x01(\x04\x12I\n\x0erecording_type\x18\x08 \x01(\x0e\x32\x13.EGameRecordingType:\x1ck_EGameRecordingType_Unknown\"\xcf\x03\n\x0e\x43TimelineEntry\x12\x13\n\x0btimeline_id\x18\x01 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x02 \x01(\x04\x12\x0c\n\x04time\x18\x03 \x01(\x04\x12?\n\x04type\x18\x04 \x01(\x0e\x32\x13.ETimelineEntryType:\x1ck_ETimelineEntryType_Invalid\x12\x11\n\tgame_mode\x18\x05 \x01(\x05\x12\x13\n\x0brange_title\x18\x07 \x01(\t\x12\x16\n\x0erange_duration\x18\x08 \x01(\x04\x12\x1b\n\x13range_possible_clip\x18\t \x01(\x05\x12\x17\n\x0ftimestamp_title\x18\n \x01(\t\x12\x13\n\x0bmarker_icon\x18\x0b \x01(\t\x12\x1a\n\x12marker_description\x18\r \x01(\t\x12\x17\n\x0fmarker_priority\x18\x0e \x01(\x05\x12\x19\n\x11screenshot_handle\x18\x0f \x01(\r\x12\x18\n\x10\x61\x63hievement_name\x18\x10 \x01(\t\x12\x1a\n\x03tag\x18\x11 \x03(\x0b\x32\r.CTimelineTag\x12\x10\n\x08phase_id\x18\x12 \x01(\t\x12$\n\nattributes\x18\x13 \x03(\x0b\x32\x10.CPhaseAttribute\"c\n0CGameRecording_TimelineEntryChanged_Notification\x12\x1e\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x0f.CTimelineEntry\x12\x0f\n\x07game_id\x18\x02 \x01(\x06\"j\n0CGameRecording_TimelineEntryRemoved_Notification\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x03 \x01(\x04\"*\n(CGameRecording_LowDiskSpace_Notification\"H\n5CGameRecording_PostGameHighlightsChanged_Notification\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"W\n2CGameRecording_OpenOverlayToGamePhase_Notification\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x10\n\x08phase_id\x18\x02 \x01(\t\"[\n6CGameRecording_OpenOverlayToTimelineEvent_Notification\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x10\n\x08\x65ntry_id\x18\x02 \x01(\x04\".\n,CGameRecording_PhaseListChanged_Notification\"\xa4\x03\n\x1a\x43GameRecording_ClipSummary\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\x04\x12\x13\n\x0b\x64uration_ms\x18\x03 \x01(\x04\x12\x15\n\rdate_recorded\x18\x04 \x01(\r\x12\x19\n\x11start_timeline_id\x18\x05 \x01(\t\x12\x17\n\x0fstart_offset_ms\x18\x06 \x01(\x04\x12\x19\n\x11published_file_id\x18\x07 \x01(\x04\x12\x11\n\tfile_size\x18\x08 \x01(\x04\x12\x0c\n\x04name\x18\t \x01(\t\x12\x14\n\x0c\x64\x61te_clipped\x18\n \x01(\r\x12\x11\n\ttemporary\x18\x0b \x01(\x08\x12\x17\n\x0foriginal_device\x18\x0c \x01(\t\x12#\n\x1boriginal_gaming_device_type\x18\r \x01(\r\x12\x17\n\x0f\x64\x61te_downloaded\x18\x0e \x01(\r\x12\x15\n\rthumbnail_url\x18\x0f \x01(\t\x12\x17\n\x0fthumbnail_width\x18\x10 \x01(\r\x12\x18\n\x10thumbnail_height\x18\x11 \x01(\r\"\xa7\x02\n\x1f\x43GameRecording_SaveClip_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x38\n\x05start\x18\x02 \x01(\x0b\x32).CGameRecording_SaveClip_Request.Position\x12\x36\n\x03\x65nd\x18\x03 \x01(\x0b\x32).CGameRecording_SaveClip_Request.Position\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0bsrc_clip_id\x18\x05 \x01(\t\x12\x11\n\ttemporary\x18\x06 \x01(\x08\x12\x17\n\x0f\x66orce_thumbnail\x18\x07 \x01(\x08\x1a\x32\n\x08Position\x12\x13\n\x0btimeline_id\x18\x01 \x01(\t\x12\x11\n\toffset_ms\x18\x02 \x01(\x04\"P\n CGameRecording_SaveClip_Response\x12,\n\x07summary\x18\x01 \x01(\x0b\x32\x1b.CGameRecording_ClipSummary\"4\n!CGameRecording_DeleteClip_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\"$\n\"CGameRecording_DeleteClip_Response\"\xaa\x01\n\"CGameRecording_ExportClip_Settings\x12\x14\n\x0c\x62itrate_kbps\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x19\n\x11\x66rames_per_second\x18\x04 \x01(\x05\x12\x34\n\x05\x63odec\x18\x05 \x01(\x0e\x32\r.EExportCodec:\x16k_EExportCodec_Default\"\xa1\x01\n!CGameRecording_ExportClip_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\x17\n\x0f\x65xport_mp4_path\x18\x02 \x01(\t\x12\x35\n\x08settings\x18\x03 \x01(\x0b\x32#.CGameRecording_ExportClip_Settings\x12\x1b\n\x13use_unique_filename\x18\x04 \x01(\x08\"$\n\"CGameRecording_ExportClip_Response\"\x8d\x01\n(CGameRecording_ExportClipPreview_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\x35\n\x08settings\x18\x02 \x01(\x0b\x32#.CGameRecording_ExportClip_Settings\x12\x19\n\x11run_policy_checks\x18\x03 \x01(\x08\"z\n)CGameRecording_ExportClipPreview_Response\x12\x16\n\x0e\x65stimated_size\x18\x01 \x01(\x04\x12\x35\n\x08settings\x18\x02 \x01(\x0b\x32#.CGameRecording_ExportClip_Settings\"i\n%CGameRecording_TakeScreenshot_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x06\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x1a\n\x12timeline_offset_ms\x18\x03 \x01(\x04\"?\n&CGameRecording_TakeScreenshot_Response\x12\x15\n\rscreenshot_id\x18\x01 \x01(\x06\"l\n(CGameRecording_UploadClipToSteam_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x12\n\nvisibility\x18\x04 \x01(\x05\"Y\n)CGameRecording_UploadClipToSteam_Response\x12,\n\x07summary\x18\x01 \x01(\x0b\x32\x1b.CGameRecording_ClipSummary\"1\n\x1e\x43GameRecording_ZipClip_Request\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\"3\n\x1f\x43GameRecording_ZipClip_Response\x12\x10\n\x08zip_path\x18\x01 \x01(\t\"d\n\x1f\x43GameRecording_GetClips_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x15\n\rcreated_after\x18\x02 \x01(\r\x12\x19\n\x11include_temporary\x18\x03 \x01(\x08\"M\n CGameRecording_GetClips_Response\x12)\n\x04\x63lip\x18\x01 \x03(\x0b\x32\x1b.CGameRecording_ClipSummary\"]\n3CGameRecording_GetAndTrimPostGameHighlights_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x15\n\rcreated_after\x18\x02 \x01(\r\"d\n4CGameRecording_GetAndTrimPostGameHighlights_Response\x12,\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1c.CGameRecordingTimelineEvent\"o\n+CGameRecording_UserAddTimelineEntry_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x1e\n\x05\x65ntry\x18\x02 \x01(\x0b\x32\x0f.CTimelineEntry\x12\x0f\n\x07\x63lip_id\x18\x03 \x01(\t\"@\n,CGameRecording_UserAddTimelineEntry_Response\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\x04\"r\n.CGameRecording_UserUpdateTimelineEntry_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x1e\n\x05\x65ntry\x18\x02 \x01(\x0b\x32\x0f.CTimelineEntry\x12\x0f\n\x07\x63lip_id\x18\x03 \x01(\t\"1\n/CGameRecording_UserUpdateTimelineEntry_Response\"y\n.CGameRecording_UserRemoveTimelineEntry_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\x12\x13\n\x0btimeline_id\x18\x02 \x01(\t\x12\x10\n\x08\x65ntry_id\x18\x03 \x01(\x04\x12\x0f\n\x07\x63lip_id\x18\x04 \x01(\t\"1\n/CGameRecording_UserRemoveTimelineEntry_Response\"J\n6CGameRecording_ManuallyDeleteRecordingsForApps_Request\x12\x10\n\x08game_ids\x18\x01 \x03(\x04\"9\n7CGameRecording_ManuallyDeleteRecordingsForApps_Response\"\x7f\n-CGameRecording_GetTotalDiskSpaceUsage_Request\x12\x13\n\x0b\x66older_path\x18\x01 \x01(\t\x12\x39\n\x04type\x18\x02 \x01(\x0e\x32\x0f.EDiskSpaceType:\x1ak_eDiskSpaceType_Recording\">\n.CGameRecording_GetTotalDiskSpaceUsage_Response\x12\x0c\n\x04size\x18\x01 \x01(\x04\"\xfe\x01\n$CGameRecording_GetThumbnails_Request\x12\x14\n\x0crecording_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63lip_id\x18\x03 \x01(\t\x12\x13\n\x0btimeline_id\x18\x07 \x01(\t\x12\x17\n\x0fstart_offset_us\x18\x04 \x03(\x03\x12\x17\n\nmajor_axis\x18\x05 \x01(\r:\x03\x35\x31\x32\x12<\n\x0etime_precision\x18\x06 \x01(\x0e\x32\x18.EThumbnailTimePrecision:\nk_ePrecise\x12*\n\x06\x66ormat\x18\x08 \x01(\x0e\x32\x11.EThumbnailFormat:\x07k_eJPEG\"\xad\x01\n%CGameRecording_GetThumbnails_Response\x12\x44\n\nthumbnails\x18\x01 \x03(\x0b\x32\x30.CGameRecording_GetThumbnails_Response.Thumbnail\x1a>\n\tThumbnail\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\"8\n%CGameRecording_StartRecording_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"(\n&CGameRecording_StartRecording_Response\"7\n$CGameRecording_StopRecording_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"U\n%CGameRecording_StopRecording_Response\x12,\n\x07summary\x18\x01 \x01(\x0b\x32\x1b.CGameRecording_ClipSummary\":\n\'CGameRecording_GetRecordingSize_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"=\n(CGameRecording_GetRecordingSize_Response\x12\x11\n\tfile_size\x18\x01 \x01(\x04\"4\n2CGameRecording_CleanupBackgroundRecordings_Request\"5\n3CGameRecording_CleanupBackgroundRecordings_Response\"0\n.CGameRecording_GetPlatformCapabilities_Request\"T\n/CGameRecording_GetPlatformCapabilities_Response\x12!\n\x19per_process_audio_capture\x18\x01 \x01(\x08\"W\n\'CGameRecording_ClipCreated_Notification\x12,\n\x07summary\x18\x01 \x01(\x0b\x32\x1b.CGameRecording_ClipSummary\"K\n\'CGameRecording_ClipDeleted_Notification\x12\x0f\n\x07\x63lip_id\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\x04\"`\n*CGameRecording_ExportProgress_Notification\x12\x10\n\x08progress\x18\x01 \x01(\x02\x12\x0f\n\x07\x63lip_id\x18\x02 \x01(\t\x12\x0f\n\x07\x65result\x18\x03 \x01(\x05\"u\n\x1e\x43GameRecording_PerGameSettings\x12\x0e\n\x06gameid\x18\x01 \x01(\x06\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0f\n\x07minutes\x18\x03 \x01(\r\x12\x0f\n\x07\x62itrate\x18\x04 \x01(\t\x12\x10\n\x08infinite\x18\x05 \x01(\x08\"+\n)CGameRecording_GetPerGameSettings_Request\"_\n*CGameRecording_GetPerGameSettings_Response\x12\x31\n\x08settings\x18\x01 \x03(\x0b\x32\x1f.CGameRecording_PerGameSettings\"c\n)CGameRecording_SetPerGameSettings_Request\x12\x36\n\rgame_settings\x18\x01 \x01(\x0b\x32\x1f.CGameRecording_PerGameSettings\",\n*CGameRecording_SetPerGameSettings_Response\">\n,CGameRecording_DeletePerGameSettings_Request\x12\x0e\n\x06gameid\x18\x01 \x01(\x06\"/\n-CGameRecording_DeletePerGameSettings_Response\"`\n*CGameRecording_UploadProgress_Notification\x12\x10\n\x08progress\x18\x01 \x01(\x02\x12\x0f\n\x07\x63lip_id\x18\x02 \x01(\t\x12\x0f\n\x07\x65result\x18\x03 \x01(\x05\"G\n4CGameRecording_SwitchBackgroundRecordingGame_Request\x12\x0f\n\x07game_id\x18\x01 \x01(\x04\"7\n5CGameRecording_SwitchBackgroundRecordingGame_Response*\xf6\x02\n\x12\x45TimelineEntryType\x12 \n\x1ck_ETimelineEntryType_Invalid\x10\x00\x12!\n\x1dk_ETimelineEntryType_GameMode\x10\x01\x12\x1e\n\x1ak_ETimelineEntryType_Event\x10\x02\x12)\n%k_ETimelineEntryType_StateDescription\x10\x03\x12$\n k_ETimelineEntryType_Achievement\x10\x04\x12#\n\x1fk_ETimelineEntryType_UserMarker\x10\x05\x12#\n\x1fk_ETimelineEntryType_Screenshot\x10\x06\x12\x1e\n\x1ak_ETimelineEntryType_Error\x10\x07\x12\x1c\n\x18k_ETimelineEntryType_Tag\x10\x08\x12\"\n\x1ek_ETimelineEntryType_GamePhase\x10\t*n\n\x10\x45PhaseResultType\x12 \n\x1ck_EPhaseResultType_Automatic\x10\x01\x12\x1c\n\x18k_EPhaseResultType_Blank\x10\x02\x12\x1a\n\x16k_EPhaseResultType_API\x10\x03*\xd6\x02\n\x1f\x45TimelineChangeNotificationType\x12-\n)k_ETimelineChangeNotificationType_Started\x10\x01\x12-\n)k_ETimelineChangeNotificationType_Stopped\x10\x02\x12-\n)k_ETimelineChangeNotificationType_Deleted\x10\x03\x12\x36\n2k_ETimelineChangeNotificationType_RecordingStarted\x10\x04\x12\x36\n2k_ETimelineChangeNotificationType_RecordingStopped\x10\x05\x12\x36\n2k_ETimelineChangeNotificationType_RecordingUpdated\x10\x06*\x85\x02\n\'ERecordingSessionChangeNotificationType\x12\x35\n1k_ERecordingSessionChangeNotificationType_Started\x10\x01\x12\x35\n1k_ERecordingSessionChangeNotificationType_Stopped\x10\x02\x12\x35\n1k_ERecordingSessionChangeNotificationType_Deleted\x10\x03\x12\x35\n1k_ERecordingSessionChangeNotificationType_Updated\x10\x04*K\n\x0e\x45\x44iskSpaceType\x12\x1e\n\x1ak_eDiskSpaceType_Recording\x10\x00\x12\x19\n\x15k_eDiskSpaceType_Clip\x10\x01*7\n\x17\x45ThumbnailTimePrecision\x12\x0e\n\nk_ePrecise\x10\x00\x12\x0c\n\x08k_eLoose\x10\x01*+\n\x10\x45ThumbnailFormat\x12\x0b\n\x07k_eJPEG\x10\x01\x12\n\n\x06k_eRGB\x10\x02\x32\xca$\n\rGameRecording\x12\x85\x01\n\x1aGetAppsWithBackgroundVideo\x12\x32.CGameRecording_GetAppsWithBackgroundVideo_Request\x1a\x33.CGameRecording_GetAppsWithBackgroundVideo_Response\x12m\n\x12GetTimelinesForApp\x12*.CGameRecording_GetTimelinesForApp_Request\x1a+.CGameRecording_GetTimelinesForApp_Response\x12p\n\x13GetTimelinesForClip\x12+.CGameRecording_GetTimelinesForClip_Request\x1a,.CGameRecording_GetTimelinesForClip_Response\x12X\n\x0bQueryPhases\x12#.CGameRecording_QueryPhases_Request\x1a$.CGameRecording_QueryPhases_Response\x12L\n\x07GetTags\x12\x1f.CGameRecording_GetTags_Request\x1a .CGameRecording_GetTags_Response\x12m\n\x12GetEnoughDiskSpace\x12*.CGameRecording_GetEnoughDiskSpace_Request\x1a+.CGameRecording_GetEnoughDiskSpace_Response\x12v\n\x15GetAvailableDiskSpace\x12-.CGameRecording_GetAvailableDiskSpace_Request\x1a..CGameRecording_GetAvailableDiskSpace_Response\x12O\n\x08SaveClip\x12 .CGameRecording_SaveClip_Request\x1a!.CGameRecording_SaveClip_Response\x12U\n\nDeleteClip\x12\".CGameRecording_DeleteClip_Request\x1a#.CGameRecording_DeleteClip_Response\x12O\n\x08GetClips\x12 .CGameRecording_GetClips_Request\x1a!.CGameRecording_GetClips_Response\x12j\n\x11UploadClipToSteam\x12).CGameRecording_UploadClipToSteam_Request\x1a*.CGameRecording_UploadClipToSteam_Response\x12U\n\nExportClip\x12\".CGameRecording_ExportClip_Request\x1a#.CGameRecording_ExportClip_Response\x12j\n\x11\x45xportClipPreview\x12).CGameRecording_ExportClipPreview_Request\x1a*.CGameRecording_ExportClipPreview_Response\x12\x61\n\x0eTakeScreenshot\x12&.CGameRecording_TakeScreenshot_Request\x1a\'.CGameRecording_TakeScreenshot_Response\x12L\n\x07ZipClip\x12\x1f.CGameRecording_ZipClip_Request\x1a .CGameRecording_ZipClip_Response\x12\x61\n\x0eStartRecording\x12&.CGameRecording_StartRecording_Request\x1a\'.CGameRecording_StartRecording_Response\x12^\n\rStopRecording\x12%.CGameRecording_StopRecording_Request\x1a&.CGameRecording_StopRecording_Response\x12u\n\x1eGetBackgroundRecordingFileSize\x12(.CGameRecording_GetRecordingSize_Request\x1a).CGameRecording_GetRecordingSize_Response\x12\x88\x01\n\x1b\x43leanupBackgroundRecordings\x12\x33.CGameRecording_CleanupBackgroundRecordings_Request\x1a\x34.CGameRecording_CleanupBackgroundRecordings_Response\x12\x8b\x01\n\x1cGetAndTrimPostGameHighlights\x12\x34.CGameRecording_GetAndTrimPostGameHighlights_Request\x1a\x35.CGameRecording_GetAndTrimPostGameHighlights_Response\x12^\n\rGetThumbnails\x12%.CGameRecording_GetThumbnails_Request\x1a&.CGameRecording_GetThumbnails_Response\x12|\n\x17GetPlatformCapabilities\x12/.CGameRecording_GetPlatformCapabilities_Request\x1a\x30.CGameRecording_GetPlatformCapabilities_Response\x12W\n\x15NotifyTimelineChanged\x12,.CGameRecording_TimelineChanged_Notification\x1a\x10.WebUINoResponse\x12g\n\x1dNotifyRecordingSessionChanged\x12\x34.CGameRecording_RecordingSessionChanged_Notification\x1a\x10.WebUINoResponse\x12\x61\n\x1aNotifyTimelineEntryChanged\x12\x31.CGameRecording_TimelineEntryChanged_Notification\x1a\x10.WebUINoResponse\x12\x61\n\x1aNotifyTimelineEntryRemoved\x12\x31.CGameRecording_TimelineEntryRemoved_Notification\x1a\x10.WebUINoResponse\x12O\n\x11NotifyClipCreated\x12(.CGameRecording_ClipCreated_Notification\x1a\x10.WebUINoResponse\x12O\n\x11NotifyClipDeleted\x12(.CGameRecording_ClipDeleted_Notification\x1a\x10.WebUINoResponse\x12U\n\x14NotifyExportProgress\x12+.CGameRecording_ExportProgress_Notification\x1a\x10.WebUINoResponse\x12U\n\x14NotifyUploadProgress\x12+.CGameRecording_UploadProgress_Notification\x1a\x10.WebUINoResponse\x12Q\n\x12NotifyLowDiskSpace\x12).CGameRecording_LowDiskSpace_Notification\x1a\x10.WebUINoResponse\x12k\n\x1fNotifyPostGameHighlightsChanged\x12\x36.CGameRecording_PostGameHighlightsChanged_Notification\x1a\x10.WebUINoResponse\x12\x65\n\x1cNotifyOpenOverlayToGamePhase\x12\x33.CGameRecording_OpenOverlayToGamePhase_Notification\x1a\x10.WebUINoResponse\x12m\n NotifyOpenOverlayToTimelineEvent\x12\x37.CGameRecording_OpenOverlayToTimelineEvent_Notification\x1a\x10.WebUINoResponse\x12Y\n\x16NotifyPhaseListChanged\x12-.CGameRecording_PhaseListChanged_Notification\x1a\x10.WebUINoResponse\x12m\n\x12GetPerGameSettings\x12*.CGameRecording_GetPerGameSettings_Request\x1a+.CGameRecording_GetPerGameSettings_Response\x12m\n\x12SetPerGameSettings\x12*.CGameRecording_SetPerGameSettings_Request\x1a+.CGameRecording_SetPerGameSettings_Response\x12v\n\x15\x44\x65letePerGameSettings\x12-.CGameRecording_DeletePerGameSettings_Request\x1a..CGameRecording_DeletePerGameSettings_Response\x12s\n\x14UserAddTimelineEntry\x12,.CGameRecording_UserAddTimelineEntry_Request\x1a-.CGameRecording_UserAddTimelineEntry_Response\x12|\n\x17UserUpdateTimelineEntry\x12/.CGameRecording_UserUpdateTimelineEntry_Request\x1a\x30.CGameRecording_UserUpdateTimelineEntry_Response\x12|\n\x17UserRemoveTimelineEntry\x12/.CGameRecording_UserRemoveTimelineEntry_Request\x1a\x30.CGameRecording_UserRemoveTimelineEntry_Response\x12\x94\x01\n\x1fManuallyDeleteRecordingsForApps\x12\x37.CGameRecording_ManuallyDeleteRecordingsForApps_Request\x1a\x38.CGameRecording_ManuallyDeleteRecordingsForApps_Response\x12y\n\x16GetTotalDiskSpaceUsage\x12..CGameRecording_GetTotalDiskSpaceUsage_Request\x1a/.CGameRecording_GetTotalDiskSpaceUsage_Response\x12\x8e\x01\n\x1dSwitchBackgroundRecordingGame\x12\x35.CGameRecording_SwitchBackgroundRecordingGame_Request\x1a\x36.CGameRecording_SwitchBackgroundRecordingGame_Response\x1a\x04\x80\x97\"\x01\x42\x05H\x01\x90\x01\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webuimessages_gamerecording_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\001'
  _globals['_GAMERECORDING']._options = None
  _globals['_GAMERECORDING']._serialized_options = b'\200\227\"\001'
  _globals['_ETIMELINEENTRYTYPE']._serialized_start=9099
  _globals['_ETIMELINEENTRYTYPE']._serialized_end=9473
  _globals['_EPHASERESULTTYPE']._serialized_start=9475
  _globals['_EPHASERESULTTYPE']._serialized_end=9585
  _globals['_ETIMELINECHANGENOTIFICATIONTYPE']._serialized_start=9588
  _globals['_ETIMELINECHANGENOTIFICATIONTYPE']._serialized_end=9930
  _globals['_ERECORDINGSESSIONCHANGENOTIFICATIONTYPE']._serialized_start=9933
  _globals['_ERECORDINGSESSIONCHANGENOTIFICATIONTYPE']._serialized_end=10194
  _globals['_EDISKSPACETYPE']._serialized_start=10196
  _globals['_EDISKSPACETYPE']._serialized_end=10271
  _globals['_ETHUMBNAILTIMEPRECISION']._serialized_start=10273
  _globals['_ETHUMBNAILTIMEPRECISION']._serialized_end=10328
  _globals['_ETHUMBNAILFORMAT']._serialized_start=10330
  _globals['_ETHUMBNAILFORMAT']._serialized_end=10373
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_REQUEST']._serialized_start=142
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_REQUEST']._serialized_end=193
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_RESPONSE']._serialized_start=196
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_RESPONSE']._serialized_end=556
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_RESPONSE_APP']._serialized_start=322
  _globals['_CGAMERECORDING_GETAPPSWITHBACKGROUNDVIDEO_RESPONSE_APP']._serialized_end=556
  _globals['_CGAMERECORDING_GETTIMELINESFORAPP_REQUEST']._serialized_start=558
  _globals['_CGAMERECORDING_GETTIMELINESFORAPP_REQUEST']._serialized_end=618
  _globals['_CGAMERECORDING_GETTIMELINESFORAPP_RESPONSE']._serialized_start=620
  _globals['_CGAMERECORDING_GETTIMELINESFORAPP_RESPONSE']._serialized_end=716
  _globals['_CGAMERECORDING_GETTIMELINESFORCLIP_REQUEST']._serialized_start=718
  _globals['_CGAMERECORDING_GETTIMELINESFORCLIP_REQUEST']._serialized_end=779
  _globals['_CGAMERECORDING_GETTIMELINESFORCLIP_RESPONSE']._serialized_start=782
  _globals['_CGAMERECORDING_GETTIMELINESFORCLIP_RESPONSE']._serialized_end=936
  _globals['_CGAMERECORDING_QUERYPHASES_REQUEST']._serialized_start=939
  _globals['_CGAMERECORDING_QUERYPHASES_REQUEST']._serialized_end=1180
  _globals['_CGAMERECORDING_QUERYPHASES_REQUEST_TAG']._serialized_start=1146
  _globals['_CGAMERECORDING_QUERYPHASES_REQUEST_TAG']._serialized_end=1180
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE']._serialized_start=1183
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE']._serialized_end=1852
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE_PHASE']._serialized_start=1304
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE_PHASE']._serialized_end=1852
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE_PHASE_BACKGROUNDRECORDING']._serialized_start=1773
  _globals['_CGAMERECORDING_QUERYPHASES_RESPONSE_PHASE_BACKGROUNDRECORDING']._serialized_end=1852
  _globals['_CGAMERECORDING_GETTAGS_REQUEST']._serialized_start=1854
  _globals['_CGAMERECORDING_GETTAGS_REQUEST']._serialized_end=1903
  _globals['_CGAMERECORDING_GETTAGS_RESPONSE']._serialized_start=1905
  _globals['_CGAMERECORDING_GETTAGS_RESPONSE']._serialized_end=1967
  _globals['_CGAMERECORDING_GETENOUGHDISKSPACE_REQUEST']._serialized_start=1969
  _globals['_CGAMERECORDING_GETENOUGHDISKSPACE_REQUEST']._serialized_end=2012
  _globals['_CGAMERECORDING_GETENOUGHDISKSPACE_RESPONSE']._serialized_start=2014
  _globals['_CGAMERECORDING_GETENOUGHDISKSPACE_RESPONSE']._serialized_end=2080
  _globals['_CGAMERECORDING_GETAVAILABLEDISKSPACE_REQUEST']._serialized_start=2082
  _globals['_CGAMERECORDING_GETAVAILABLEDISKSPACE_REQUEST']._serialized_end=2128
  _globals['_CGAMERECORDING_GETAVAILABLEDISKSPACE_RESPONSE']._serialized_start=2130
  _globals['_CGAMERECORDING_GETAVAILABLEDISKSPACE_RESPONSE']._serialized_end=2191
  _globals['_CGAMERECORDING_TIMELINECHANGED_NOTIFICATION']._serialized_start=2194
  _globals['_CGAMERECORDING_TIMELINECHANGED_NOTIFICATION']._serialized_end=2422
  _globals['_CGAMERECORDING_RECORDINGSESSIONCHANGED_NOTIFICATION']._serialized_start=2425
  _globals['_CGAMERECORDING_RECORDINGSESSIONCHANGED_NOTIFICATION']._serialized_end=2774
  _globals['_CTIMELINEENTRY']._serialized_start=2777
  _globals['_CTIMELINEENTRY']._serialized_end=3240
  _globals['_CGAMERECORDING_TIMELINEENTRYCHANGED_NOTIFICATION']._serialized_start=3242
  _globals['_CGAMERECORDING_TIMELINEENTRYCHANGED_NOTIFICATION']._serialized_end=3341
  _globals['_CGAMERECORDING_TIMELINEENTRYREMOVED_NOTIFICATION']._serialized_start=3343
  _globals['_CGAMERECORDING_TIMELINEENTRYREMOVED_NOTIFICATION']._serialized_end=3449
  _globals['_CGAMERECORDING_LOWDISKSPACE_NOTIFICATION']._serialized_start=3451
  _globals['_CGAMERECORDING_LOWDISKSPACE_NOTIFICATION']._serialized_end=3493
  _globals['_CGAMERECORDING_POSTGAMEHIGHLIGHTSCHANGED_NOTIFICATION']._serialized_start=3495
  _globals['_CGAMERECORDING_POSTGAMEHIGHLIGHTSCHANGED_NOTIFICATION']._serialized_end=3567
  _globals['_CGAMERECORDING_OPENOVERLAYTOGAMEPHASE_NOTIFICATION']._serialized_start=3569
  _globals['_CGAMERECORDING_OPENOVERLAYTOGAMEPHASE_NOTIFICATION']._serialized_end=3656
  _globals['_CGAMERECORDING_OPENOVERLAYTOTIMELINEEVENT_NOTIFICATION']._serialized_start=3658
  _globals['_CGAMERECORDING_OPENOVERLAYTOTIMELINEEVENT_NOTIFICATION']._serialized_end=3749
  _globals['_CGAMERECORDING_PHASELISTCHANGED_NOTIFICATION']._serialized_start=3751
  _globals['_CGAMERECORDING_PHASELISTCHANGED_NOTIFICATION']._serialized_end=3797
  _globals['_CGAMERECORDING_CLIPSUMMARY']._serialized_start=3800
  _globals['_CGAMERECORDING_CLIPSUMMARY']._serialized_end=4220
  _globals['_CGAMERECORDING_SAVECLIP_REQUEST']._serialized_start=4223
  _globals['_CGAMERECORDING_SAVECLIP_REQUEST']._serialized_end=4518
  _globals['_CGAMERECORDING_SAVECLIP_REQUEST_POSITION']._serialized_start=4468
  _globals['_CGAMERECORDING_SAVECLIP_REQUEST_POSITION']._serialized_end=4518
  _globals['_CGAMERECORDING_SAVECLIP_RESPONSE']._serialized_start=4520
  _globals['_CGAMERECORDING_SAVECLIP_RESPONSE']._serialized_end=4600
  _globals['_CGAMERECORDING_DELETECLIP_REQUEST']._serialized_start=4602
  _globals['_CGAMERECORDING_DELETECLIP_REQUEST']._serialized_end=4654
  _globals['_CGAMERECORDING_DELETECLIP_RESPONSE']._serialized_start=4656
  _globals['_CGAMERECORDING_DELETECLIP_RESPONSE']._serialized_end=4692
  _globals['_CGAMERECORDING_EXPORTCLIP_SETTINGS']._serialized_start=4695
  _globals['_CGAMERECORDING_EXPORTCLIP_SETTINGS']._serialized_end=4865
  _globals['_CGAMERECORDING_EXPORTCLIP_REQUEST']._serialized_start=4868
  _globals['_CGAMERECORDING_EXPORTCLIP_REQUEST']._serialized_end=5029
  _globals['_CGAMERECORDING_EXPORTCLIP_RESPONSE']._serialized_start=5031
  _globals['_CGAMERECORDING_EXPORTCLIP_RESPONSE']._serialized_end=5067
  _globals['_CGAMERECORDING_EXPORTCLIPPREVIEW_REQUEST']._serialized_start=5070
  _globals['_CGAMERECORDING_EXPORTCLIPPREVIEW_REQUEST']._serialized_end=5211
  _globals['_CGAMERECORDING_EXPORTCLIPPREVIEW_RESPONSE']._serialized_start=5213
  _globals['_CGAMERECORDING_EXPORTCLIPPREVIEW_RESPONSE']._serialized_end=5335
  _globals['_CGAMERECORDING_TAKESCREENSHOT_REQUEST']._serialized_start=5337
  _globals['_CGAMERECORDING_TAKESCREENSHOT_REQUEST']._serialized_end=5442
  _globals['_CGAMERECORDING_TAKESCREENSHOT_RESPONSE']._serialized_start=5444
  _globals['_CGAMERECORDING_TAKESCREENSHOT_RESPONSE']._serialized_end=5507
  _globals['_CGAMERECORDING_UPLOADCLIPTOSTEAM_REQUEST']._serialized_start=5509
  _globals['_CGAMERECORDING_UPLOADCLIPTOSTEAM_REQUEST']._serialized_end=5617
  _globals['_CGAMERECORDING_UPLOADCLIPTOSTEAM_RESPONSE']._serialized_start=5619
  _globals['_CGAMERECORDING_UPLOADCLIPTOSTEAM_RESPONSE']._serialized_end=5708
  _globals['_CGAMERECORDING_ZIPCLIP_REQUEST']._serialized_start=5710
  _globals['_CGAMERECORDING_ZIPCLIP_REQUEST']._serialized_end=5759
  _globals['_CGAMERECORDING_ZIPCLIP_RESPONSE']._serialized_start=5761
  _globals['_CGAMERECORDING_ZIPCLIP_RESPONSE']._serialized_end=5812
  _globals['_CGAMERECORDING_GETCLIPS_REQUEST']._serialized_start=5814
  _globals['_CGAMERECORDING_GETCLIPS_REQUEST']._serialized_end=5914
  _globals['_CGAMERECORDING_GETCLIPS_RESPONSE']._serialized_start=5916
  _globals['_CGAMERECORDING_GETCLIPS_RESPONSE']._serialized_end=5993
  _globals['_CGAMERECORDING_GETANDTRIMPOSTGAMEHIGHLIGHTS_REQUEST']._serialized_start=5995
  _globals['_CGAMERECORDING_GETANDTRIMPOSTGAMEHIGHLIGHTS_REQUEST']._serialized_end=6088
  _globals['_CGAMERECORDING_GETANDTRIMPOSTGAMEHIGHLIGHTS_RESPONSE']._serialized_start=6090
  _globals['_CGAMERECORDING_GETANDTRIMPOSTGAMEHIGHLIGHTS_RESPONSE']._serialized_end=6190
  _globals['_CGAMERECORDING_USERADDTIMELINEENTRY_REQUEST']._serialized_start=6192
  _globals['_CGAMERECORDING_USERADDTIMELINEENTRY_REQUEST']._serialized_end=6303
  _globals['_CGAMERECORDING_USERADDTIMELINEENTRY_RESPONSE']._serialized_start=6305
  _globals['_CGAMERECORDING_USERADDTIMELINEENTRY_RESPONSE']._serialized_end=6369
  _globals['_CGAMERECORDING_USERUPDATETIMELINEENTRY_REQUEST']._serialized_start=6371
  _globals['_CGAMERECORDING_USERUPDATETIMELINEENTRY_REQUEST']._serialized_end=6485
  _globals['_CGAMERECORDING_USERUPDATETIMELINEENTRY_RESPONSE']._serialized_start=6487
  _globals['_CGAMERECORDING_USERUPDATETIMELINEENTRY_RESPONSE']._serialized_end=6536
  _globals['_CGAMERECORDING_USERREMOVETIMELINEENTRY_REQUEST']._serialized_start=6538
  _globals['_CGAMERECORDING_USERREMOVETIMELINEENTRY_REQUEST']._serialized_end=6659
  _globals['_CGAMERECORDING_USERREMOVETIMELINEENTRY_RESPONSE']._serialized_start=6661
  _globals['_CGAMERECORDING_USERREMOVETIMELINEENTRY_RESPONSE']._serialized_end=6710
  _globals['_CGAMERECORDING_MANUALLYDELETERECORDINGSFORAPPS_REQUEST']._serialized_start=6712
  _globals['_CGAMERECORDING_MANUALLYDELETERECORDINGSFORAPPS_REQUEST']._serialized_end=6786
  _globals['_CGAMERECORDING_MANUALLYDELETERECORDINGSFORAPPS_RESPONSE']._serialized_start=6788
  _globals['_CGAMERECORDING_MANUALLYDELETERECORDINGSFORAPPS_RESPONSE']._serialized_end=6845
  _globals['_CGAMERECORDING_GETTOTALDISKSPACEUSAGE_REQUEST']._serialized_start=6847
  _globals['_CGAMERECORDING_GETTOTALDISKSPACEUSAGE_REQUEST']._serialized_end=6974
  _globals['_CGAMERECORDING_GETTOTALDISKSPACEUSAGE_RESPONSE']._serialized_start=6976
  _globals['_CGAMERECORDING_GETTOTALDISKSPACEUSAGE_RESPONSE']._serialized_end=7038
  _globals['_CGAMERECORDING_GETTHUMBNAILS_REQUEST']._serialized_start=7041
  _globals['_CGAMERECORDING_GETTHUMBNAILS_REQUEST']._serialized_end=7295
  _globals['_CGAMERECORDING_GETTHUMBNAILS_RESPONSE']._serialized_start=7298
  _globals['_CGAMERECORDING_GETTHUMBNAILS_RESPONSE']._serialized_end=7471
  _globals['_CGAMERECORDING_GETTHUMBNAILS_RESPONSE_THUMBNAIL']._serialized_start=7409
  _globals['_CGAMERECORDING_GETTHUMBNAILS_RESPONSE_THUMBNAIL']._serialized_end=7471
  _globals['_CGAMERECORDING_STARTRECORDING_REQUEST']._serialized_start=7473
  _globals['_CGAMERECORDING_STARTRECORDING_REQUEST']._serialized_end=7529
  _globals['_CGAMERECORDING_STARTRECORDING_RESPONSE']._serialized_start=7531
  _globals['_CGAMERECORDING_STARTRECORDING_RESPONSE']._serialized_end=7571
  _globals['_CGAMERECORDING_STOPRECORDING_REQUEST']._serialized_start=7573
  _globals['_CGAMERECORDING_STOPRECORDING_REQUEST']._serialized_end=7628
  _globals['_CGAMERECORDING_STOPRECORDING_RESPONSE']._serialized_start=7630
  _globals['_CGAMERECORDING_STOPRECORDING_RESPONSE']._serialized_end=7715
  _globals['_CGAMERECORDING_GETRECORDINGSIZE_REQUEST']._serialized_start=7717
  _globals['_CGAMERECORDING_GETRECORDINGSIZE_REQUEST']._serialized_end=7775
  _globals['_CGAMERECORDING_GETRECORDINGSIZE_RESPONSE']._serialized_start=7777
  _globals['_CGAMERECORDING_GETRECORDINGSIZE_RESPONSE']._serialized_end=7838
  _globals['_CGAMERECORDING_CLEANUPBACKGROUNDRECORDINGS_REQUEST']._serialized_start=7840
  _globals['_CGAMERECORDING_CLEANUPBACKGROUNDRECORDINGS_REQUEST']._serialized_end=7892
  _globals['_CGAMERECORDING_CLEANUPBACKGROUNDRECORDINGS_RESPONSE']._serialized_start=7894
  _globals['_CGAMERECORDING_CLEANUPBACKGROUNDRECORDINGS_RESPONSE']._serialized_end=7947
  _globals['_CGAMERECORDING_GETPLATFORMCAPABILITIES_REQUEST']._serialized_start=7949
  _globals['_CGAMERECORDING_GETPLATFORMCAPABILITIES_REQUEST']._serialized_end=7997
  _globals['_CGAMERECORDING_GETPLATFORMCAPABILITIES_RESPONSE']._serialized_start=7999
  _globals['_CGAMERECORDING_GETPLATFORMCAPABILITIES_RESPONSE']._serialized_end=8083
  _globals['_CGAMERECORDING_CLIPCREATED_NOTIFICATION']._serialized_start=8085
  _globals['_CGAMERECORDING_CLIPCREATED_NOTIFICATION']._serialized_end=8172
  _globals['_CGAMERECORDING_CLIPDELETED_NOTIFICATION']._serialized_start=8174
  _globals['_CGAMERECORDING_CLIPDELETED_NOTIFICATION']._serialized_end=8249
  _globals['_CGAMERECORDING_EXPORTPROGRESS_NOTIFICATION']._serialized_start=8251
  _globals['_CGAMERECORDING_EXPORTPROGRESS_NOTIFICATION']._serialized_end=8347
  _globals['_CGAMERECORDING_PERGAMESETTINGS']._serialized_start=8349
  _globals['_CGAMERECORDING_PERGAMESETTINGS']._serialized_end=8466
  _globals['_CGAMERECORDING_GETPERGAMESETTINGS_REQUEST']._serialized_start=8468
  _globals['_CGAMERECORDING_GETPERGAMESETTINGS_REQUEST']._serialized_end=8511
  _globals['_CGAMERECORDING_GETPERGAMESETTINGS_RESPONSE']._serialized_start=8513
  _globals['_CGAMERECORDING_GETPERGAMESETTINGS_RESPONSE']._serialized_end=8608
  _globals['_CGAMERECORDING_SETPERGAMESETTINGS_REQUEST']._serialized_start=8610
  _globals['_CGAMERECORDING_SETPERGAMESETTINGS_REQUEST']._serialized_end=8709
  _globals['_CGAMERECORDING_SETPERGAMESETTINGS_RESPONSE']._serialized_start=8711
  _globals['_CGAMERECORDING_SETPERGAMESETTINGS_RESPONSE']._serialized_end=8755
  _globals['_CGAMERECORDING_DELETEPERGAMESETTINGS_REQUEST']._serialized_start=8757
  _globals['_CGAMERECORDING_DELETEPERGAMESETTINGS_REQUEST']._serialized_end=8819
  _globals['_CGAMERECORDING_DELETEPERGAMESETTINGS_RESPONSE']._serialized_start=8821
  _globals['_CGAMERECORDING_DELETEPERGAMESETTINGS_RESPONSE']._serialized_end=8868
  _globals['_CGAMERECORDING_UPLOADPROGRESS_NOTIFICATION']._serialized_start=8870
  _globals['_CGAMERECORDING_UPLOADPROGRESS_NOTIFICATION']._serialized_end=8966
  _globals['_CGAMERECORDING_SWITCHBACKGROUNDRECORDINGGAME_REQUEST']._serialized_start=8968
  _globals['_CGAMERECORDING_SWITCHBACKGROUNDRECORDINGGAME_REQUEST']._serialized_end=9039
  _globals['_CGAMERECORDING_SWITCHBACKGROUNDRECORDINGGAME_RESPONSE']._serialized_start=9041
  _globals['_CGAMERECORDING_SWITCHBACKGROUNDRECORDINGGAME_RESPONSE']._serialized_end=9096
  _globals['_GAMERECORDING']._serialized_start=10376
  _globals['_GAMERECORDING']._serialized_end=15058
_builder.BuildServices(DESCRIPTOR, 'webuimessages_gamerecording_pb2', _globals)
# @@protoc_insertion_point(module_scope)
