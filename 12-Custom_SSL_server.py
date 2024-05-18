#!/usr/bin/python3
"""
A simple SSL server
"""
import socket
import ssl
from ssl import PROTOCOL_TLSv1_2

SSL_SERVER_PORT = 8000

if __name__ == "__main__":
    server_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
    server_socket.bind(('', SSL_SERVER_PORT))
    server_socket.listen(5)
    print("Waiting for ssl client on port %s", SSL_SERVER_PORT)
    client_sock, addr = server_socket.accept()
    ssl_conn = ssl.wrap_socket(client_sock, server_side=True,
            certfile='server.crt',
            keyfile='server.key',
            ssl_version=PROTOCOL_TLSv1_2
            )
    data = ssl_conn.recv(60)
    print(data)
    ssl_conn.write('200 OK\r\n\r\n'.encode('utf-8'))
    print("Served SSL client. Exiting")
    ssl_conn.close()
    server_socket.close()

