#!/usr/bin/python3
"""
Exchanges data with the server
Also curl -L -i "http://linux.org:80" can work
"""
import socket

HOST = 'www.linux.org'
PORT = 80
BUFFERSIZE = 4096
addr = (HOST, PORT)

if __name__ == '__main__':
    client_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
    client_socket.connect(addr)

    while True:
        data = 'GET / HTTP/1.0\r\n\r\n'
        if not data:
            break
        client_socket.send(data.encode('utf-8'))
        data = client_socket.recv(BUFFERSIZE)
        
        if not data:
            break
        print(data.decode('utf-8'))

    client_socket.close()
