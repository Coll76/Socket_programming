#!/usr/bin/python3
"""
UDP client to send some data to the UDP server
"""
import socket

BUFFSIZE = 4096
port = 12345

if __name__ == "__main__":
    client_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = "Hello, we are sending some message to UDP server"
    client_soc.sendto(msg.encode('utf-8'), ('', port))
    data, addr = client_soc.recvfrom(BUFFSIZE)
    print("Server says")
    print(str(data))
