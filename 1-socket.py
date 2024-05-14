#!/usr/bin/python3
"""
Creates a TCP Socket object
"""
from socket import socket
import socket
#from socket import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
