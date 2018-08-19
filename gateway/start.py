# coding: utf-8
import time
import os
from gateway.gateway import gateway_singleton
from .config import cg_debug
import logging
from gateway.glog import tcp_logger,wst_logger,rpc_logger

if __name__ == "__main__":

    logging.getLogger().disabled = True
    logging.getLogger(name="jsonrpcclient.client.request").disabled = True
    logging.getLogger(name="jsonrpcclient.client.response").disabled = True
    logging.getLogger(name="jsonrpcserver.dispatcher.request").disabled = True
    logging.getLogger(name="jsonrpcserver.dispatcher.response").disabled = True
    if not cg_debug:
        rpc_logger.setLevel(logging.INFO)
        tcp_logger.setLevel(logging.INFO)
        wst_logger.setLevel(logging.INFO)
    else:
        rpc_logger.setLevel(logging.DEBUG)
        tcp_logger.setLevel(logging.DEBUG)
        wst_logger.setLevel(logging.DEBUG)
    try:
        gateway_singleton.start()
    except KeyboardInterrupt:
        gateway_singleton.clearn()
    except OSError as ex:
        print(ex.args[1])
    else:
        gateway_singleton.close()
        # pass