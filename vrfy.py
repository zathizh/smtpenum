#! /usr/bin/python

import sys
import socket

if len(sys.argv) !=3:
    print("Usage : vrfy.py <remote ip> <filename>")
    sys.exit(0)

host = sys.argv[1]
port = 25
_size = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
banner = sock.recv(_size)
print(banner.strip())
with open (sys.argv[2]) as f:
    for l in f:
        sock.send( "VRFY " + l.strip() + "\r\n")
        result = sock.recv(_size)
        print(result.strip())

sock.close()
