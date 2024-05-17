#!/usr/bin/python3
"""
A non-blocking socket operations return immediately
even if the operation cannot be completed immediately
"""
import socket


if __name__ == "__main__":
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """
    sets socket to non-blocking method
    """
    sock.setblocking(0)
    sock.settimeout(0.5)
    sock.bind(("127.0.0.1", 0))
    """
    Retrieves the address of the socket
    """
    socket_address =sock.getsockname()

    try:
        print("Asynchronous socket server launched on socket: %s", socket_address)
        while(1):
            sock.listen()
    except KeyboardInterrupt:
        print("Exit user")
