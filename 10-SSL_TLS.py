#!/usr/bin/python3
"""
Securing sockets with TLS/SSL
In this case, this code establishes a connection between HTTPS and TCP
"""
import socket
import ssl

"""
First create a TCP socket
"""
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
Create a context
"""
context = ssl.create_default_context()
"""
Wrap the socket with SSL
"""
secure_socket = context.wrap_socket(sock, server_hostname='www.google.com')
"""
connect to the server
"""
secure_socket.connect(('www.google.com', 443))

"""
Possible to send/receive data over secure_socket
"""
secure_socket.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n')
data = secure_socket.recv(40)
print(data.decode('utf-8'))
"""
Close the connection
"""
secure_socket.close()
