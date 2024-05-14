#!/usr/bin/python3
"""
Connecting a TCP client socket to server socket
"""
import socket
import sys
"""
AF_INET represents the socket family in this IPv4
SOCK_STREAM represents the socket type in this case TCP
"""
if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print("Failed to create a socket object")
        print("Reason: %s", str(err))
        sys.exit()

    print("Socket object created")

    target_host = input("Enter the target hostname to connect to: ")
    target_port = input("Enter the target port to connect to: ")

    try:
        s.connect((target_host, int(target_port)))
        print(f"Socket connected to {target_host} on port {target_port}")
        s.shutdown(2)

    except socket.error as err:
        print("Failed to connect to {} on port {}".format(target_host, target_port))
        print("Reason: %s", str(err))
        sys.exit()
