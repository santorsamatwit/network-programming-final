"""
Created by Matthew Santorsa on 9/23/24 at 09:38:07

@author Matthew

"""


import socket
import sys

HOST = ""
PORT = 47152

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket created")

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print("Bind failed. Error code: " + str(msg[0]) + " Message: " + msg[1])
    sys.exit()
print("Bind completed.")

s.listen(10)

print(f"Socket listening on port {PORT}")

while True:
    try:
        sc, address = s.accept()
        print (f"Connected with {address[0]}:{str(address[1])}")
        firstline = sc.recv(50)
        print(firstline)
        sc.sendall(b'Success!')
        sc.close()
    except socket.error as msg:
        print(f"Accept failed. Error code: {str(msg[0])} Message: {msg[1]}")

s.close()