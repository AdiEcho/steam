# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steamdatagram_messages_sdr.proto
# Protobuf Python Version: 4.25.6
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steamnetworkingsockets_messages_certs_pb2 as steamnetworkingsockets__messages__certs__pb2
import steam.protobufs.steamnetworkingsockets_messages_pb2 as steamnetworkingsockets__messages__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n steamdatagram_messages_sdr.proto\x1a+steamnetworkingsockets_messages_certs.proto\x1a%steamnetworkingsockets_messages.proto\"6\n\x1c\x43MsgSteamNetworkingIPAddress\x12\n\n\x02v4\x18\x01 \x01(\x07\x12\n\n\x02v6\x18\x02 \x01(\x0c\"\x96\x01\n%CMsgSteamDatagramSignedMessageGeneric\x12\x31\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x13\n\x0bsigned_data\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\x12\x12\n\tdummy_pad\x18\xff\x07 \x01(\x0c\"\xfd\x07\n CMsgSteamDatagramRouterPingReply\x12\x18\n\x10\x63lient_timestamp\x18\x01 \x01(\x07\x12\"\n\x16latency_datacenter_ids\x18\x02 \x03(\x07\x42\x02\x10\x01\x12\x1b\n\x0flatency_ping_ms\x18\x03 \x03(\rB\x02\x10\x01\x12&\n\x1alatency_datacenter_ids_p2p\x18\x0e \x03(\x07\x42\x02\x10\x01\x12\x1f\n\x13latency_ping_ms_p2p\x18\x0f \x03(\rB\x02\x10\x01\x12\x16\n\x0eyour_public_ip\x18\x04 \x01(\x07\x12\x18\n\x10your_public_port\x18\x0b \x01(\x07\x12\x13\n\x0bserver_time\x18\x05 \x01(\x07\x12\x11\n\tchallenge\x18\x06 \x01(\x06\x12\x1e\n\x16seconds_until_shutdown\x18\x07 \x01(\r\x12\x15\n\rclient_cookie\x18\x08 \x01(\x07\x12\x10\n\x08recv_tos\x18\x10 \x01(\r\x12\x15\n\recho_sent_tos\x18\x11 \x01(\r\x12\x10\n\x08sent_tos\x18\x12 \x01(\r\x12\x1e\n\x16\x65\x63ho_request_reply_tos\x18\x13 \x01(\r\x12%\n\x1dscoring_penalty_relay_cluster\x18\t \x01(\r\x12\r\n\x05\x66lags\x18\x0c \x01(\r\x12J\n\x10route_exceptions\x18\n \x03(\x0b\x32\x30.CMsgSteamDatagramRouterPingReply.RouteException\x12\x43\n\ralt_addresses\x18\r \x03(\x0b\x32,.CMsgSteamDatagramRouterPingReply.AltAddress\x12\x11\n\tdummy_pad\x18\x63 \x01(\x0c\x12\x14\n\x0c\x64ummy_varint\x18\x64 \x01(\x04\x1aH\n\x0eRouteException\x12\x16\n\x0e\x64\x61ta_center_id\x18\x01 \x01(\x07\x12\r\n\x05\x66lags\x18\x02 \x01(\r\x12\x0f\n\x07penalty\x18\x03 \x01(\r\x1a\xc0\x01\n\nAltAddress\x12\x0c\n\x04ipv4\x18\x01 \x01(\x07\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x0f\n\x07penalty\x18\x03 \x01(\r\x12X\n\x08protocol\x18\x04 \x01(\x0e\x32\x35.CMsgSteamDatagramRouterPingReply.AltAddress.Protocol:\x0f\x44\x65\x66\x61ultProtocol\x12\n\n\x02id\x18\x05 \x01(\t\"\x1f\n\x08Protocol\x12\x13\n\x0f\x44\x65\x66\x61ultProtocol\x10\x00\"L\n\x05\x46lags\x12 \n\x1c\x46LAG_MAYBE_MORE_DATA_CENTERS\x10\x01\x12!\n\x1d\x46LAG_MAYBE_MORE_ALT_ADDRESSES\x10\x02\"\x80\x02\n*CMsgSteamDatagramGameserverPingRequestBody\x12\x13\n\x0brelay_popid\x18\x01 \x01(\x07\x12\x35\n\x0eyour_public_ip\x18\x02 \x01(\x0b\x32\x1d.CMsgSteamNetworkingIPAddress\x12\x18\n\x10your_public_port\x18\x03 \x01(\r\x12\x17\n\x0frelay_unix_time\x18\x04 \x01(\x04\x12\x16\n\x0erouting_secret\x18\x05 \x01(\x06\x12-\n\x06my_ips\x18\x06 \x03(\x0b\x32\x1d.CMsgSteamNetworkingIPAddress\x12\x0c\n\x04\x65\x63ho\x18\x08 \x01(\x0c\"\xba\x02\n.CMsgSteamDatagramGameserverPingRequestEnvelope\x12\x31\n\x04\x63\x65rt\x18\x06 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x13\n\x0bsigned_data\x18\x07 \x01(\x0c\x12\x11\n\tsignature\x18\x08 \x01(\x0c\x12\x1d\n\x15legacy_your_public_ip\x18\x01 \x01(\x07\x12\x1f\n\x17legacy_your_public_port\x18\x05 \x01(\x07\x12\x1e\n\x16legacy_relay_unix_time\x18\x02 \x01(\x07\x12\x18\n\x10legacy_challenge\x18\x03 \x01(\x06\x12\x1f\n\x17legacy_router_timestamp\x18\x04 \x01(\x07\x12\x12\n\tdummy_pad\x18\xff\x07 \x01(\x0c\"\xad\x02\n(CMsgSteamDatagramGameserverPingReplyData\x12\x1c\n\x14\x65\x63ho_relay_unix_time\x18\x02 \x01(\x07\x12\x0c\n\x04\x65\x63ho\x18\x08 \x01(\x0c\x12\x18\n\x10legacy_challenge\x18\x03 \x01(\x06\x12\x1f\n\x17legacy_router_timestamp\x18\x04 \x01(\x07\x12\x16\n\x0e\x64\x61ta_center_id\x18\x05 \x01(\x07\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x12\x18\n\x10protocol_version\x18\x07 \x01(\r\x12\r\n\x05\x62uild\x18\t \x01(\t\x12\x1e\n\x16network_config_version\x18\n \x01(\x04\x12\x14\n\x0cmy_unix_time\x18\x0b \x01(\x07\x12\x14\n\x0crouting_blob\x18\x0c \x01(\x0c\"\xba\x01\n\'CMsgSteamDatagramNoSessionRelayToClient\x12\x15\n\rconnection_id\x18\x07 \x01(\x07\x12\x16\n\x0eyour_public_ip\x18\x02 \x01(\x07\x12\x18\n\x10your_public_port\x18\x06 \x01(\x07\x12\x13\n\x0bserver_time\x18\x03 \x01(\x07\x12\x11\n\tchallenge\x18\x04 \x01(\x06\x12\x1e\n\x16seconds_until_shutdown\x18\x05 \x01(\r\"\x97\x01\n%CMsgSteamDatagramNoSessionRelayToPeer\x12\x1f\n\x17legacy_relay_session_id\x18\x01 \x01(\r\x12\x1d\n\x15\x66rom_relay_session_id\x18\x02 \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\x07 \x01(\x07\x12\x12\n\nkludge_pad\x18\x63 \x01(\x06\"L\n\x10\x43MsgTOSTreatment\x12\x12\n\nl4s_detect\x18\x01 \x01(\t\x12\x0f\n\x07up_ecn1\x18\x02 \x01(\t\x12\x13\n\x0b\x64own_dscp45\x18\x03 \x01(\t\"A\n(CMsgSteamDatagramClientPingSampleRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\"\xb2\x07\n&CMsgSteamDatagramClientPingSampleReply\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x1d\n\x15relay_override_active\x18\x05 \x01(\x08\x12\x1e\n\x03tos\x18\x06 \x01(\x0b\x32\x11.CMsgTOSTreatment\x12\x39\n\x04pops\x18\x02 \x03(\x0b\x32+.CMsgSteamDatagramClientPingSampleReply.POP\x12U\n\x13legacy_data_centers\x18\x03 \x03(\x0b\x32\x38.CMsgSteamDatagramClientPingSampleReply.LegacyDataCenter\x1a\xb8\x04\n\x03POP\x12\x0e\n\x06pop_id\x18\x01 \x01(\x07\x12\x1d\n\x15\x64\x65\x66\x61ult_front_ping_ms\x18\x02 \x01(\r\x12\x17\n\x0f\x63luster_penalty\x18\x04 \x01(\r\x12M\n\ralt_addresses\x18\x07 \x03(\x0b\x32\x36.CMsgSteamDatagramClientPingSampleReply.POP.AltAddress\x12\x1b\n\x13\x64\x65\x66\x61ult_e2e_ping_ms\x18\x03 \x01(\r\x12\x19\n\x11\x64\x65\x66\x61ult_e2e_score\x18\x05 \x01(\r\x12!\n\x19p2p_via_peer_relay_pop_id\x18\x06 \x01(\x07\x12\x17\n\x0f\x62\x65st_dc_ping_ms\x18\t \x01(\r\x12\x15\n\rbest_dc_score\x18\n \x01(\r\x12 \n\x18\x62\x65st_dc_via_relay_pop_id\x18\x0b \x01(\x07\x12\x1a\n\x12\x64\x65\x66\x61ult_dc_ping_ms\x18\x0c \x01(\r\x12\x18\n\x10\x64\x65\x66\x61ult_dc_score\x18\r \x01(\r\x12#\n\x1b\x64\x65\x66\x61ult_dc_via_relay_pop_id\x18\x0e \x01(\x07\x12\x17\n\x0ftest_dc_ping_ms\x18\x0f \x01(\r\x12\x15\n\rtest_dc_score\x18\x10 \x01(\r\x12 \n\x18test_dc_via_relay_pop_id\x18\x11 \x01(\x07\x1a@\n\nAltAddress\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rfront_ping_ms\x18\x02 \x01(\r\x12\x0f\n\x07penalty\x18\x03 \x01(\r\x1a\x65\n\x10LegacyDataCenter\x12\x16\n\x0e\x64\x61ta_center_id\x18\x01 \x01(\x07\x12 \n\x18\x62\x65st_dc_via_relay_pop_id\x18\x02 \x01(\x07\x12\x17\n\x0f\x62\x65st_dc_ping_ms\x18\x03 \x01(\r\"\x8e\x05\n&CMsgSteamDatagramClientSwitchedPrimary\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x0f\n\x07\x66rom_ip\x18\x02 \x01(\x07\x12\x11\n\tfrom_port\x18\x03 \x01(\r\x12\x1b\n\x13\x66rom_router_cluster\x18\x04 \x01(\x07\x12\x18\n\x10\x66rom_active_time\x18\x05 \x01(\r\x12 \n\x18\x66rom_active_packets_recv\x18\x06 \x01(\r\x12\x1b\n\x13\x66rom_dropped_reason\x18\x07 \x01(\t\x12\x0e\n\x06gap_ms\x18\x08 \x01(\r\x12O\n\x10\x66rom_quality_now\x18\t \x01(\x0b\x32\x35.CMsgSteamDatagramClientSwitchedPrimary.RouterQuality\x12M\n\x0eto_quality_now\x18\n \x01(\x0b\x32\x35.CMsgSteamDatagramClientSwitchedPrimary.RouterQuality\x12P\n\x11\x66rom_quality_then\x18\x0b \x01(\x0b\x32\x35.CMsgSteamDatagramClientSwitchedPrimary.RouterQuality\x12N\n\x0fto_quality_then\x18\x0c \x01(\x0b\x32\x35.CMsgSteamDatagramClientSwitchedPrimary.RouterQuality\x1a\x61\n\rRouterQuality\x12\r\n\x05score\x18\x01 \x01(\r\x12\x12\n\nfront_ping\x18\x02 \x01(\r\x12\x11\n\tback_ping\x18\x03 \x01(\r\x12\x1a\n\x12seconds_until_down\x18\x04 \x01(\r\"\xc2\x02\n\x1f\x43MsgSteamDatagramConnectRequest\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x14\n\x0cmy_timestamp\x18\x04 \x01(\x06\x12\x13\n\x0bping_est_ms\x18\x05 \x01(\r\x12\x14\n\x0cvirtual_port\x18\t \x01(\r\x12#\n\x1bgameserver_relay_session_id\x18\x02 \x01(\r\x12\x37\n\x05\x63rypt\x18\x06 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x07 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x16\n\x0erouting_secret\x18\n \x01(\x06\x12\x1e\n\x16legacy_client_steam_id\x18\x03 \x01(\x06\"\x9a\x02\n\x1a\x43MsgSteamDatagramConnectOK\x12\x1c\n\x14\x63lient_connection_id\x18\x01 \x01(\x07\x12\x1c\n\x14server_connection_id\x18\x07 \x01(\x07\x12\x16\n\x0eyour_timestamp\x18\x03 \x01(\x06\x12\x17\n\x0f\x64\x65lay_time_usec\x18\x04 \x01(\r\x12#\n\x1bgameserver_relay_session_id\x18\x02 \x01(\r\x12\x37\n\x05\x63rypt\x18\x05 \x01(\x0b\x32(.CMsgSteamDatagramSessionCryptInfoSigned\x12\x31\n\x04\x63\x65rt\x18\x06 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\"\xae\x03\n\'CMsgSteamNetworkingP2PSDRRoutingSummary\x12\x14\n\x0cinitial_ping\x18\x01 \x01(\r\x12 \n\x18initial_ping_front_local\x18\x02 \x01(\r\x12!\n\x19initial_ping_front_remote\x18\x03 \x01(\r\x12\x15\n\rinitial_score\x18\x04 \x01(\r\x12\x19\n\x11initial_pop_local\x18\x05 \x01(\x07\x12\x1a\n\x12initial_pop_remote\x18\x06 \x01(\x07\x12\x11\n\tbest_ping\x18\x0b \x01(\r\x12\x1d\n\x15\x62\x65st_ping_front_local\x18\x0c \x01(\r\x12\x1e\n\x16\x62\x65st_ping_front_remote\x18\r \x01(\r\x12\x12\n\nbest_score\x18\x0e \x01(\r\x12\x16\n\x0e\x62\x65st_pop_local\x18\x0f \x01(\x07\x12\x17\n\x0f\x62\x65st_pop_remote\x18\x10 \x01(\x07\x12\x11\n\tbest_time\x18\x11 \x01(\r\x12\x16\n\x0enegotiation_ms\x18\x07 \x01(\r\x12\x18\n\x10selected_seconds\x18\x08 \x01(\r\"\x8f\x01\n\"CMsgSteamDatagramP2PRoutingSummary\x12\x32\n\x03ice\x18\x02 \x01(\x0b\x32%.CMsgSteamNetworkingICESessionSummary\x12\x35\n\x03sdr\x18\x03 \x01(\x0b\x32(.CMsgSteamNetworkingP2PSDRRoutingSummary\"\xe9\x06\n!CMsgSteamDatagramConnectionClosed\x12\x18\n\x10to_connection_id\x18\x07 \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\x08 \x01(\x07\x12\x1c\n\x14\x66rom_identity_string\x18\x0f \x01(\t\x12M\n\x1blegacy_from_identity_binary\x18\r \x01(\x0b\x32(.CMsgSteamNetworkingIdentityLegacyBinary\x12\x1c\n\x14legacy_from_steam_id\x18\x03 \x01(\x06\x12*\n\"legacy_gameserver_relay_session_id\x18\x02 \x01(\r\x12\x1b\n\x13to_relay_session_id\x18\t \x01(\x07\x12\x1d\n\x15\x66rom_relay_session_id\x18\n \x01(\x07\x12*\n\"forward_target_relay_routing_token\x18\x0b \x01(\x0c\x12\x1f\n\x17\x66orward_target_revision\x18\x0c \x01(\r\x12G\n\nrelay_mode\x18\x04 \x01(\x0e\x32-.CMsgSteamDatagramConnectionClosed.ERelayMode:\x04None\x12\r\n\x05\x64\x65\x62ug\x18\x05 \x01(\t\x12\x13\n\x0breason_code\x18\x06 \x01(\r\x12\x16\n\x0erouting_secret\x18\x0e \x01(\x06\x12\x1b\n\x13not_primary_session\x18\x10 \x01(\x08\x12\x1d\n\x15not_primary_transport\x18\x13 \x01(\x08\x12\x1d\n\x15relay_override_active\x18\x16 \x01(\x08\x12:\n\rquality_relay\x18\x11 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x12 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12@\n\x13p2p_routing_summary\x18\x15 \x01(\x0b\x32#.CMsgSteamDatagramP2PRoutingSummary\"6\n\nERelayMode\x12\x08\n\x04None\x10\x00\x12\x0c\n\x08\x45ndToEnd\x10\x01\x12\x10\n\x0c\x43losedByPeer\x10\x02\"\xcc\x04\n\x1d\x43MsgSteamDatagramNoConnection\x12\x18\n\x10to_connection_id\x18\x05 \x01(\x07\x12\x1a\n\x12\x66rom_connection_id\x18\x06 \x01(\x07\x12*\n\"legacy_gameserver_relay_session_id\x18\x02 \x01(\r\x12\x1b\n\x13to_relay_session_id\x18\t \x01(\x07\x12\x1d\n\x15\x66rom_relay_session_id\x18\n \x01(\x07\x12\x1c\n\x14\x66rom_identity_string\x18\x07 \x01(\t\x12\x1c\n\x14legacy_from_steam_id\x18\x03 \x01(\x06\x12\x12\n\nend_to_end\x18\x04 \x01(\x08\x12\x1b\n\x13not_primary_session\x18\x0c \x01(\x08\x12\x1d\n\x15not_primary_transport\x18\x0f \x01(\x08\x12\x1d\n\x15relay_override_active\x18\x11 \x01(\x08\x12:\n\rquality_relay\x18\r \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x0e \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12@\n\x13p2p_routing_summary\x18\x10 \x01(\x0b\x32#.CMsgSteamDatagramP2PRoutingSummary\x12\x16\n\x0erouting_secret\x18\x0b \x01(\x06\x12\x12\n\tdummy_pad\x18\xff\x07 \x01(\x07\"\xdc\x02\n)CMsgSteamDatagramGameserverSessionRequest\x12\x0e\n\x06ticket\x18\x01 \x01(\x0c\x12\x16\n\x0e\x63hallenge_time\x18\x03 \x01(\x07\x12\x11\n\tchallenge\x18\x04 \x01(\x06\x12\x1c\n\x14\x63lient_connection_id\x18\x05 \x01(\x07\x12\x1c\n\x14server_connection_id\x18\x08 \x01(\x07\x12\x1e\n\x16network_config_version\x18\x06 \x01(\x04\x12\x18\n\x10protocol_version\x18\x07 \x01(\r\x12\x10\n\x08platform\x18\t \x01(\t\x12\r\n\x05\x62uild\x18\n \x01(\t\x12\x1f\n\x17\x64\x65v_gameserver_identity\x18\x64 \x01(\t\x12<\n\x0f\x64\x65v_client_cert\x18\x65 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\"\xe8\x01\n-CMsgSteamDatagramGameserverSessionEstablished\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\"\n\x1agameserver_identity_string\x18\x02 \x01(\t\x12\x1e\n\x16seconds_until_shutdown\x18\x04 \x01(\r\x12\x13\n\x0bseq_num_r2c\x18\x06 \x01(\r\x12$\n\x1c\x64ummy_legacy_identity_binary\x18\x07 \x01(\x0c\x12!\n\x19legacy_gameserver_steamid\x18\x03 \x01(\x06\"\xad\x03\n.CMsgSteamDatagramConnectionStatsClientToRouter\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x11\n\tack_relay\x18\x04 \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\x05 \x03(\x07\x12\r\n\x05\x66lags\x18\x06 \x01(\r\x12\x1c\n\x14\x63lient_connection_id\x18\x08 \x01(\x07\x12\x13\n\x0bseq_num_c2r\x18\t \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\n \x01(\r\"\x82\x01\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\x12\x17\n\x13NOT_PRIMARY_SESSION\x10\x08\x12\x19\n\x15\x43LIENT_RELAY_OVERRIDE\x10 \"\xf9\x03\n.CMsgSteamDatagramConnectionStatsRouterToClient\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x1e\n\x16seconds_until_shutdown\x18\x06 \x01(\r\x12\x1a\n\x12migrate_request_ip\x18\n \x01(\x07\x12\x1c\n\x14migrate_request_port\x18\x0b \x01(\r\x12%\n\x1dscoring_penalty_relay_cluster\x18\x0c \x01(\r\x12\x11\n\tack_relay\x18\r \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\x0e \x03(\x07\x12\r\n\x05\x66lags\x18\x0f \x01(\r\x12\x1c\n\x14\x63lient_connection_id\x18\x07 \x01(\x07\x12\x13\n\x0bseq_num_r2c\x18\x08 \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\t \x01(\r\"N\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\"\x88\x04\n.CMsgSteamDatagramConnectionStatsRouterToServer\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x11\n\tack_relay\x18\n \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\x0b \x03(\x07\x12\r\n\x05\x66lags\x18\x0c \x01(\r\x12\x13\n\x0bseq_num_r2s\x18\x05 \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\x06 \x01(\r\x12\x1e\n\x16\x63lient_identity_string\x18\x0f \x01(\t\x12\x1e\n\x16legacy_client_steam_id\x18\x07 \x01(\x06\x12\x18\n\x10relay_session_id\x18\x08 \x01(\r\x12\x1c\n\x14\x63lient_connection_id\x18\t \x01(\x07\x12\x1c\n\x14server_connection_id\x18\r \x01(\x07\x12\x16\n\x0erouting_secret\x18\x0e \x01(\x06\"N\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\"\xb0\x03\n.CMsgSteamDatagramConnectionStatsServerToRouter\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x11\n\tack_relay\x18\x08 \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\t \x03(\x07\x12\r\n\x05\x66lags\x18\n \x01(\r\x12\x13\n\x0bseq_num_s2r\x18\x03 \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\x04 \x01(\r\x12\x18\n\x10relay_session_id\x18\x06 \x01(\r\x12\x1c\n\x14\x63lient_connection_id\x18\x07 \x01(\x07\x12\x1c\n\x14server_connection_id\x18\x0b \x01(\x07\"N\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\"\xc5\x03\n&CMsgSteamDatagramP2PSessionRequestBody\x12\x16\n\x0e\x63hallenge_time\x18\x01 \x01(\x07\x12\x11\n\tchallenge\x18\x02 \x01(\x06\x12\x1c\n\x14\x63lient_connection_id\x18\x03 \x01(\x07\x12\x1c\n\x14legacy_peer_steam_id\x18\x04 \x01(\x06\x12\x1c\n\x14peer_identity_string\x18\x0b \x01(\t\x12\x1a\n\x12peer_connection_id\x18\x05 \x01(\x07\x12\x16\n\x0e\x65ncrypted_data\x18\x0e \x01(\x0c\x12,\n$encryption_your_public_key_lead_byte\x18\x0f \x01(\r\x12*\n\"encryption_my_ephemeral_public_key\x18\x10 \x01(\x0c\x12\x18\n\x10protocol_version\x18\x08 \x01(\r\x12\x1e\n\x16network_config_version\x18\t \x01(\x04\x12\x10\n\x08platform\x18\x0c \x01(\t\x12\r\n\x05\x62uild\x18\r \x01(\t\x1a-\n\rEncryptedData\x12\x1c\n\x14peer_identity_string\x18\x01 \x01(\t\"x\n\"CMsgSteamDatagramP2PSessionRequest\x12\x31\n\x04\x63\x65rt\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramCertificateSigned\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"\x91\x01\n&CMsgSteamDatagramP2PSessionEstablished\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\x1e\n\x16seconds_until_shutdown\x18\x03 \x01(\r\x12\x1b\n\x13relay_routing_token\x18\x04 \x01(\x0c\x12\x13\n\x0bseq_num_r2c\x18\x05 \x01(\r\"\x89\x05\n1CMsgSteamDatagramConnectionStatsP2PClientToRouter\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12@\n\x13p2p_routing_summary\x18\x0e \x01(\x0b\x32#.CMsgSteamDatagramP2PRoutingSummary\x12\x11\n\tack_relay\x18\x03 \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\x04 \x03(\x07\x12\r\n\x05\x66lags\x18\x05 \x01(\r\x12*\n\"forward_target_relay_routing_token\x18\x06 \x01(\x0c\x12\x1f\n\x17\x66orward_target_revision\x18\x07 \x01(\r\x12\x0e\n\x06routes\x18\x08 \x01(\x0c\x12 \n\x18\x61\x63k_peer_routes_revision\x18\t \x01(\r\x12\x15\n\rconnection_id\x18\n \x01(\x07\x12\x13\n\x0bseq_num_c2r\x18\x0b \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\x0c \x01(\r\"\xa1\x01\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\x12\x17\n\x13NOT_PRIMARY_SESSION\x10\x08\x12\x1d\n\x19NOT_PRIMARY_TRANSPORT_E2E\x10\x10\x12\x19\n\x15\x43LIENT_RELAY_OVERRIDE\x10 \"\xeb\x04\n1CMsgSteamDatagramConnectionStatsP2PRouterToClient\x12:\n\rquality_relay\x18\x01 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x38\n\x0bquality_e2e\x18\x02 \x01(\x0b\x32#.CMsgSteamDatagramConnectionQuality\x12\x1e\n\x16seconds_until_shutdown\x18\x03 \x01(\r\x12\x1a\n\x12migrate_request_ip\x18\x04 \x01(\x07\x12\x1c\n\x14migrate_request_port\x18\x05 \x01(\r\x12%\n\x1dscoring_penalty_relay_cluster\x18\x06 \x01(\r\x12\x11\n\tack_relay\x18\x07 \x03(\x07\x12\x16\n\x0elegacy_ack_e2e\x18\x08 \x03(\x07\x12\r\n\x05\x66lags\x18\t \x01(\r\x12#\n\x1b\x61\x63k_forward_target_revision\x18\n \x01(\r\x12\x0e\n\x06routes\x18\x0b \x01(\x0c\x12 \n\x18\x61\x63k_peer_routes_revision\x18\x0c \x01(\r\x12\x15\n\rconnection_id\x18\r \x01(\x07\x12\x13\n\x0bseq_num_r2c\x18\x0e \x01(\r\x12\x13\n\x0bseq_num_e2e\x18\x0f \x01(\r\"m\n\x05\x46lags\x12\x15\n\x11\x41\x43K_REQUEST_RELAY\x10\x01\x12\x13\n\x0f\x41\x43K_REQUEST_E2E\x10\x02\x12\x19\n\x15\x41\x43K_REQUEST_IMMEDIATE\x10\x04\x12\x1d\n\x19NOT_PRIMARY_TRANSPORT_E2E\x10\x10\"\xa0\x01\n*CMsgSteamDatagramP2PBadRouteRouterToClient\x12\x15\n\rconnection_id\x18\x01 \x01(\x07\x12\"\n\x1a\x66\x61iled_relay_routing_token\x18\x02 \x01(\x0c\x12#\n\x1b\x61\x63k_forward_target_revision\x18\x03 \x01(\r\x12\x12\n\nkludge_pad\x18\x63 \x01(\x06\"\xef\x02\n\x1a\x43MsgSteamDatagramP2PRoutes\x12@\n\x0erelay_clusters\x18\x01 \x03(\x0b\x32(.CMsgSteamDatagramP2PRoutes.RelayCluster\x12\x31\n\x06routes\x18\x02 \x03(\x0b\x32!.CMsgSteamDatagramP2PRoutes.Route\x12\x10\n\x08revision\x18\x03 \x01(\r\x1ak\n\x0cRelayCluster\x12\x0e\n\x06pop_id\x18\x01 \x01(\x07\x12\x0f\n\x07ping_ms\x18\x02 \x01(\r\x12\x15\n\rscore_penalty\x18\x03 \x01(\r\x12#\n\x1bsession_relay_routing_token\x18\x04 \x01(\x0c\x1a]\n\x05Route\x12\x11\n\tmy_pop_id\x18\x01 \x01(\x07\x12\x13\n\x0byour_pop_id\x18\x02 \x01(\x07\x12\x14\n\x0clegacy_score\x18\x03 \x01(\r\x12\x16\n\x0einterior_score\x18\x04 \x01(\r\"\xcc\x01\n+CMsgSteamDatagramSetSecondaryAddressRequest\x12\x16\n\x0e\x63lient_main_ip\x18\x01 \x01(\x07\x12\x18\n\x10\x63lient_main_port\x18\x02 \x01(\x07\x12\x1c\n\x14\x63lient_connection_id\x18\x03 \x01(\x07\x12\x17\n\x0f\x63lient_identity\x18\x04 \x01(\t\x12 \n\x18request_send_duplication\x18\x05 \x01(\x08\x12\x12\n\nkludge_pad\x18\x63 \x01(\x0c\"N\n*CMsgSteamDatagramSetSecondaryAddressResult\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t*\xe0\x0b\n\x13\x45SteamDatagramMsgID\x12\x1f\n\x1bk_ESteamDatagramMsg_Invalid\x10\x00\x12)\n%k_ESteamDatagramMsg_RouterPingRequest\x10\x01\x12\'\n#k_ESteamDatagramMsg_RouterPingReply\x10\x02\x12-\n)k_ESteamDatagramMsg_GameserverPingRequest\x10\x03\x12\x30\n,k_ESteamDatagramMsg_GameserverSessionRequest\x10\x05\x12\x34\n0k_ESteamDatagramMsg_GameserverSessionEstablished\x10\x06\x12!\n\x1dk_ESteamDatagramMsg_NoSession\x10\x07\x12\"\n\x1ek_ESteamDatagramMsg_Diagnostic\x10\x08\x12*\n&k_ESteamDatagramMsg_DataClientToRouter\x10\t\x12*\n&k_ESteamDatagramMsg_DataRouterToServer\x10\n\x12*\n&k_ESteamDatagramMsg_DataServerToRouter\x10\x0b\x12*\n&k_ESteamDatagramMsg_DataRouterToClient\x10\x0c\x12\x1d\n\x19k_ESteamDatagramMsg_Stats\x10\r\x12/\n+k_ESteamDatagramMsg_ClientPingSampleRequest\x10\x0e\x12-\n)k_ESteamDatagramMsg_ClientPingSampleReply\x10\x0f\x12\x35\n1k_ESteamDatagramMsg_ClientToRouterSwitchedPrimary\x10\x10\x12#\n\x1fk_ESteamDatagramMsg_RelayHealth\x10\x11\x12&\n\"k_ESteamDatagramMsg_ConnectRequest\x10\x12\x12!\n\x1dk_ESteamDatagramMsg_ConnectOK\x10\x13\x12(\n$k_ESteamDatagramMsg_ConnectionClosed\x10\x14\x12$\n k_ESteamDatagramMsg_NoConnection\x10\x15\x12,\n(k_ESteamDatagramMsg_TicketDecryptRequest\x10\x16\x12*\n&k_ESteamDatagramMsg_TicketDecryptReply\x10\x17\x12)\n%k_ESteamDatagramMsg_P2PSessionRequest\x10\x18\x12-\n)k_ESteamDatagramMsg_P2PSessionEstablished\x10\x19\x12&\n\"k_ESteamDatagramMsg_P2PStatsClient\x10\x1a\x12%\n!k_ESteamDatagramMsg_P2PStatsRelay\x10\x1b\x12#\n\x1fk_ESteamDatagramMsg_P2PBadRoute\x10\x1c\x12+\n\'k_ESteamDatagramMsg_GameserverPingReply\x10\x1d\x12\x34\n0k_ESteamDatagramMsg_LegacyGameserverRegistration\x10\x1e\x12\x32\n.k_ESteamDatagramMsg_SetSecondaryAddressRequest\x10\x1f\x12\x31\n-k_ESteamDatagramMsg_SetSecondaryAddressResult\x10 \x12/\n+k_ESteamDatagramMsg_RelayToRelayPingRequest\x10!\x12-\n)k_ESteamDatagramMsg_RelayToRelayPingReply\x10\"B\x05H\x01\x90\x01\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'steamdatagram_messages_sdr_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'H\001\220\001\000'
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_datacenter_ids']._options = None
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_datacenter_ids']._serialized_options = b'\020\001'
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_ping_ms']._options = None
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_ping_ms']._serialized_options = b'\020\001'
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_datacenter_ids_p2p']._options = None
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_datacenter_ids_p2p']._serialized_options = b'\020\001'
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_ping_ms_p2p']._options = None
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY'].fields_by_name['latency_ping_ms_p2p']._serialized_options = b'\020\001'
  _globals['_ESTEAMDATAGRAMMSGID']._serialized_start=12288
  _globals['_ESTEAMDATAGRAMMSGID']._serialized_end=13792
  _globals['_CMSGSTEAMNETWORKINGIPADDRESS']._serialized_start=120
  _globals['_CMSGSTEAMNETWORKINGIPADDRESS']._serialized_end=174
  _globals['_CMSGSTEAMDATAGRAMSIGNEDMESSAGEGENERIC']._serialized_start=177
  _globals['_CMSGSTEAMDATAGRAMSIGNEDMESSAGEGENERIC']._serialized_end=327
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY']._serialized_start=330
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY']._serialized_end=1351
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ROUTEEXCEPTION']._serialized_start=1006
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ROUTEEXCEPTION']._serialized_end=1078
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ALTADDRESS']._serialized_start=1081
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ALTADDRESS']._serialized_end=1273
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ALTADDRESS_PROTOCOL']._serialized_start=1242
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_ALTADDRESS_PROTOCOL']._serialized_end=1273
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_FLAGS']._serialized_start=1275
  _globals['_CMSGSTEAMDATAGRAMROUTERPINGREPLY_FLAGS']._serialized_end=1351
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREQUESTBODY']._serialized_start=1354
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREQUESTBODY']._serialized_end=1610
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREQUESTENVELOPE']._serialized_start=1613
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREQUESTENVELOPE']._serialized_end=1927
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREPLYDATA']._serialized_start=1930
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERPINGREPLYDATA']._serialized_end=2231
  _globals['_CMSGSTEAMDATAGRAMNOSESSIONRELAYTOCLIENT']._serialized_start=2234
  _globals['_CMSGSTEAMDATAGRAMNOSESSIONRELAYTOCLIENT']._serialized_end=2420
  _globals['_CMSGSTEAMDATAGRAMNOSESSIONRELAYTOPEER']._serialized_start=2423
  _globals['_CMSGSTEAMDATAGRAMNOSESSIONRELAYTOPEER']._serialized_end=2574
  _globals['_CMSGTOSTREATMENT']._serialized_start=2576
  _globals['_CMSGTOSTREATMENT']._serialized_end=2652
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREQUEST']._serialized_start=2654
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREQUEST']._serialized_end=2719
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY']._serialized_start=2722
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY']._serialized_end=3668
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_POP']._serialized_start=2997
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_POP']._serialized_end=3565
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_POP_ALTADDRESS']._serialized_start=3501
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_POP_ALTADDRESS']._serialized_end=3565
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_LEGACYDATACENTER']._serialized_start=3567
  _globals['_CMSGSTEAMDATAGRAMCLIENTPINGSAMPLEREPLY_LEGACYDATACENTER']._serialized_end=3668
  _globals['_CMSGSTEAMDATAGRAMCLIENTSWITCHEDPRIMARY']._serialized_start=3671
  _globals['_CMSGSTEAMDATAGRAMCLIENTSWITCHEDPRIMARY']._serialized_end=4325
  _globals['_CMSGSTEAMDATAGRAMCLIENTSWITCHEDPRIMARY_ROUTERQUALITY']._serialized_start=4228
  _globals['_CMSGSTEAMDATAGRAMCLIENTSWITCHEDPRIMARY_ROUTERQUALITY']._serialized_end=4325
  _globals['_CMSGSTEAMDATAGRAMCONNECTREQUEST']._serialized_start=4328
  _globals['_CMSGSTEAMDATAGRAMCONNECTREQUEST']._serialized_end=4650
  _globals['_CMSGSTEAMDATAGRAMCONNECTOK']._serialized_start=4653
  _globals['_CMSGSTEAMDATAGRAMCONNECTOK']._serialized_end=4935
  _globals['_CMSGSTEAMNETWORKINGP2PSDRROUTINGSUMMARY']._serialized_start=4938
  _globals['_CMSGSTEAMNETWORKINGP2PSDRROUTINGSUMMARY']._serialized_end=5368
  _globals['_CMSGSTEAMDATAGRAMP2PROUTINGSUMMARY']._serialized_start=5371
  _globals['_CMSGSTEAMDATAGRAMP2PROUTINGSUMMARY']._serialized_end=5514
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONCLOSED']._serialized_start=5517
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONCLOSED']._serialized_end=6390
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONCLOSED_ERELAYMODE']._serialized_start=6336
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONCLOSED_ERELAYMODE']._serialized_end=6390
  _globals['_CMSGSTEAMDATAGRAMNOCONNECTION']._serialized_start=6393
  _globals['_CMSGSTEAMDATAGRAMNOCONNECTION']._serialized_end=6981
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERSESSIONREQUEST']._serialized_start=6984
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERSESSIONREQUEST']._serialized_end=7332
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERSESSIONESTABLISHED']._serialized_start=7335
  _globals['_CMSGSTEAMDATAGRAMGAMESERVERSESSIONESTABLISHED']._serialized_end=7567
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSCLIENTTOROUTER']._serialized_start=7570
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSCLIENTTOROUTER']._serialized_end=7999
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSCLIENTTOROUTER_FLAGS']._serialized_start=7869
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSCLIENTTOROUTER_FLAGS']._serialized_end=7999
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOCLIENT']._serialized_start=8002
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOCLIENT']._serialized_end=8507
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOCLIENT_FLAGS']._serialized_start=7869
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOCLIENT_FLAGS']._serialized_end=7947
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOSERVER']._serialized_start=8510
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOSERVER']._serialized_end=9030
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOSERVER_FLAGS']._serialized_start=7869
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSROUTERTOSERVER_FLAGS']._serialized_end=7947
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSSERVERTOROUTER']._serialized_start=9033
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSSERVERTOROUTER']._serialized_end=9465
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSSERVERTOROUTER_FLAGS']._serialized_start=7869
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSSERVERTOROUTER_FLAGS']._serialized_end=7947
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUESTBODY']._serialized_start=9468
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUESTBODY']._serialized_end=9921
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUESTBODY_ENCRYPTEDDATA']._serialized_start=9876
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUESTBODY_ENCRYPTEDDATA']._serialized_end=9921
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUEST']._serialized_start=9923
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONREQUEST']._serialized_end=10043
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONESTABLISHED']._serialized_start=10046
  _globals['_CMSGSTEAMDATAGRAMP2PSESSIONESTABLISHED']._serialized_end=10191
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PCLIENTTOROUTER']._serialized_start=10194
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PCLIENTTOROUTER']._serialized_end=10843
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PCLIENTTOROUTER_FLAGS']._serialized_start=10682
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PCLIENTTOROUTER_FLAGS']._serialized_end=10843
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PROUTERTOCLIENT']._serialized_start=10846
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PROUTERTOCLIENT']._serialized_end=11465
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PROUTERTOCLIENT_FLAGS']._serialized_start=11356
  _globals['_CMSGSTEAMDATAGRAMCONNECTIONSTATSP2PROUTERTOCLIENT_FLAGS']._serialized_end=11465
  _globals['_CMSGSTEAMDATAGRAMP2PBADROUTEROUTERTOCLIENT']._serialized_start=11468
  _globals['_CMSGSTEAMDATAGRAMP2PBADROUTEROUTERTOCLIENT']._serialized_end=11628
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES']._serialized_start=11631
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES']._serialized_end=11998
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES_RELAYCLUSTER']._serialized_start=11796
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES_RELAYCLUSTER']._serialized_end=11903
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES_ROUTE']._serialized_start=11905
  _globals['_CMSGSTEAMDATAGRAMP2PROUTES_ROUTE']._serialized_end=11998
  _globals['_CMSGSTEAMDATAGRAMSETSECONDARYADDRESSREQUEST']._serialized_start=12001
  _globals['_CMSGSTEAMDATAGRAMSETSECONDARYADDRESSREQUEST']._serialized_end=12205
  _globals['_CMSGSTEAMDATAGRAMSETSECONDARYADDRESSRESULT']._serialized_start=12207
  _globals['_CMSGSTEAMDATAGRAMSETSECONDARYADDRESSRESULT']._serialized_end=12285
# @@protoc_insertion_point(module_scope)
