#!/usr/bin/python3
"""
It's possible to obtain properties of the TCP socket-HTTPS
connection where SSL-TCP has been used
"""
import socket

from ssl import PROTOCOL_TLSv1, CERT_NONE, wrap_socket, SSLError
from ssl import SSLContext
import ssl
from ssl import HAS_SNI

from pprint import pprint

TARGET_HOST = 'www.google.com'
SSL_PORT = 443
CA_CERT_PATH = '/usr/lib/python3/dist-packages/requests/certs.py'

def ssl_wrap_socket(sock, keyfile=None, certfilepath=None, ca_certs=None,
        cert_reqs=None, ssl_version=None, server_hostname=None):
    """
    Parameters:
        sock - The socket to wrap with SSL
        keyfile - Path to the private key file
        certfilepath - path to the certificate file
        ca_certs - Path to a file containing CA certificate for verifying peer's certificate
        server_hostname - Hostname of the server(used for SNI)
        cert_reqs - Specifies whether a certificate is required from the
        other side, and whether it will be validated if provided
        ssl_version - The TLS/SSL protocole to use
    """
    context = SSLContext(ssl_version)
    context.verify_mode = cert_reqs

    if ca_certs:
        try:
            context.load_verify_locations(ca_certs)
        except Exception as e:
            raise SSLError(e)

    if certfilepath:
        context.load_cert_chain(certfilepath, keyfile)

    if HAS_SNI:
        return context.wrap_socket(sock, server_hostname=server_hostname)
    return context.wrap_socket(sock)

if __name__ == "__main__":
    hostname = input("Enter hostname: ") or TARGET_HOST
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hostname, 443))
    ssl_socket = ssl_wrap_socket(client_socket,
            ssl_version=PROTOCOL_TLSv1,
            cert_reqs=ssl.CERT_REQUIRED,
            ca_certs=CA_CERT_PATH,
            server_hostname=hostname
            )

    """
    Extracting remote host certificate details
    """
    print("Extracting remote host certificate details")
    cert = ssl_socket.getpeercert()
    pprint(cert)

    if not cert or ('commonName', TARGET_HOST) not in cert['subject'][4]:
        raise Exception("Invalid SSL cert for host %s. Check if this is a man in the middle attack", TARGET_HOST)

    req = f'GET / HTTP/1.1\r\nHost: {TARGET_HOST}\r\n\r\n'
    ssl_socket.write(request.encode('utf-8'))

    """
    Receive the response
    """
    response = ssl_socket.recv(50)
    print(response.decode('utf-8'))

    ssl_socket.close()
    client_socket.close()
