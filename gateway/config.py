# coding: utf-8
"""
node gateway config module \n
every variable in this config module start as 'cg'
"""

version = 'V0.2.9'

###### Common ######
# tcp end of file don't modify
cg_end_mark = "/eof/"
cg_bytes_encoding = "utf-8"
###### Common ######


###### Gateway ######
cg_tcp_addr = ("0.0.0.0", 8189)
cg_wsocket_addr = ("0.0.0.0", 8866)
cg_local_jsonrpc_addr = ("0.0.0.0", 8177)
cg_remote_jsonrpc_addr = ("0.0.0.0", 21556)
cg_public_ip_port = "localhost:8189"
# cg_public_ip_port = "p1"
cg_node_name = "trinity1"
cg_max_wallet_cli = 10
###### Gateway ######

# only for debug control
cg_debug = False
cg_debug_multi_ports = False
cg_reused_tcp_connection = True
