#!/usr/bin/env python
import socket, sys, struct
filename = 'C:/Users/zja/Desktop/log_file.txt'
with open(filename, 'rb') as f:
    data_to_send = f.read()
# data_to_send = 'this is data'
HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting...')
s.connect((HOST, PORT))
print('sending config...')
s.send(struct.pack('>L', len(data_to_send)))
s.send(data_to_send)
s.close()
print('complete')