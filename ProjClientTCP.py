# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:29:06 2024

@author: olivi
"""

import socket

HOST = '10.220.88.192'
PORT = 8080
FILENAME = ( )  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(FILENAME.encode('utf-8'))

f = open(FILENAME, 'rb')
while True:
   

