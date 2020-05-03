#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

class Server:
    def __init__(self,host,port):
        print("init server with host:%s,port:%d" % (host,port))
        self.host = host
        self.port = port

    def runServer(self):
        isRun = True
        tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpSock.bind((self.host,self.port))
        print("Start Server success")
        tcpSock.listen(5)
        while isRun:
            conn,addr = tcpSock.accept()
            print(conn)
            print("Client Addr :", addr)
            print("Ready to accept message!")
            client_message = conn.recv(1024)
            print("client message : %s" % client_message)
            conn.send(str.encode('k'))
            isRun = False
        conn.close()
        tcpSock.close()


