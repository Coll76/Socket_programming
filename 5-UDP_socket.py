#!/usr/bin/python3
"""
Working with UDP sockets
"""
import socket

BUFFSIZE = 4096

if __name__ == "__main__":
    udp_server_soc_obj = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
            )
    udp_server_soc_obj.bind(('', 12345))

    while True:
        data, addr = udp_server_soc_obj.recvfrom(BUFFSIZE)
        print("The data received from client is: ", data)
        print("Sender address: ", addr)

        """
        Data to send
        """
        resp = "UDP server sending data"
        udp_server_soc_obj.sendto(resp.encode('utf-8'), addr)
