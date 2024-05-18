#!/usr/bin/bash
#Generate a Self-Signed Certificate:
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
