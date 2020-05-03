#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from src.client.client import *
import sys
sys.path.append("../client/")
from client import Client

class start_client:

    if __name__ == '__main__':
        server_host = "lotus_chatserver_1"
        #server_host = "172.18.0.2"
        server_port = 20013
        client = Client(server_host,server_port)
        client.runClient()
