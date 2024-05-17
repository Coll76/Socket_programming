#!/usr/bin/python3
"""
TCP port forwarding to securely connect local server to remote server
Another way of doing this is creating an SSH to enable even clients to easily connect easily
"""
import sshtunnel
from getpass import getpass

ssh_host = '35.175.65.204'
ssh_port = 22
ssh_user = 'ubuntu'

remote_host = 'www.linux.org'
remote_port = 443

from sshtunnel import SSHTunnelForwarder
ssh_password = getpass('Enter your SSH password: ')

server = SSHTunnelForwarder(
        ssh_address=(ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        allow_agent=False,
        remote_bind_address=(remote_host, remote_port),
        ssh_private_key='/root/.ssh/id_rsa'
        )
server.start()
print("Connect remote service via local port: %s", server.local_bind_port)
try:
    while True:
        pass
except KeyboardInterrupt as err:
    print("Exiting user request.\n")
server.stop()
