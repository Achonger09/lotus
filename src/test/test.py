#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.client.client import *
from src.server.server import *

class TestCon:

    if __name__ == '__main__':
        server_host = "127.0.0.1"
        server_port = 20013
        server = Server(server_host,server_port)
        server.runServer()
        client = Client(server_host,server_port)
        client.runClient()