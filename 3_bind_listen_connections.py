#!/usr/bin/python3
"""
Creates a TCP server. Binds, listens and accepts
the client's request
"""
import socket

"""
create a server socket object
"""
BUFFERSIZE = 4096

if __name__ == "__main__":
    server_obj_sock = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
    hostname = input('Input the hostname: ')
    port = input('Input the port number for the host: ')

    server_obj_sock.bind((hostname, int(port)))
    server_obj_sock.listen(5)
    server_obj_sock.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
            )
    while True:
        print("Server waiting for connection")
        client_sock, addr = server_obj_sock.accept()
        print("Client connected from: ", addr)

        while True:
            data = client_sock.recv(BUFFERSIZE)
            if not data or data.decode('utf-8') == END:
                break
            print("Received from client: %s", data.decode('utf-8'))
            print("Sending the server time to client: %s" % ctime())
            client_sock.send(bytes(ctime(), 'utf-8'))
        client_sock.close()
    server_obj_sock.close()
