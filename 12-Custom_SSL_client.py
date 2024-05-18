#!/usr/bin/python3
"""
Creates a custom SSL client
"""
import socket
import ssl
from pprint import pprint

HOSTNAME = 'localhost'
TARGET_PORT = 8000
CA_CERT = 'server.crt'

if __name__ == "__main__":
    client_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
            )
    ssl_sock = ssl.wrap_socket(client_sock, cert_reqs=ssl.CERT_REQUIRED,
            ssl_version=ssl.PROTOCOL_TLSv1_2, ca_certs=CA_CERT)
    target_host = HOSTNAME
    target_port = TARGET_PORT
    ssl_sock.connect((target_host, int(target_port)))
    """
    Get the remote/peer/server cert
    """
    cert = ssl_sock.getpeercert()
    pprint(cert)
    print("Checking server certificate")

    if not cert or ssl.match_hostname(cert, target_host):
        raise Exception("Invalid SSL cert for host %s. checkif man-in-the-middle attack", target_host)
    print("Server socket OK")
    ssl_sock.write('GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'.encode())
    print(ssl_sock.read())
    ssl_sock.close()
    client_sock.close()
