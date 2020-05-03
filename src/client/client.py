#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

class Client:

    def __init__(self,server_host,server_port):
        self.server_host = server_host
        self.server_port = server_port

    def runClient(self):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.server_host,self.server_port))

        client.send("hello".encode("utf-8"))

        rec_mesage = client.recv(1024)
        print("Client receive:%s" %rec_mesage)

        client.close()
