#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print (data)