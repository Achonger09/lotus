#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from src.server.server import *
import sys
sys.path.append("../server/")
from server import Server

class testServer:
    if __name__ == '__main__':
        host = "lotus_chatserver_1"
        port = 20013
        server = Server(host,port)
        server.runServer()
