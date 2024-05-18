#!/usr/bin/bash
#Generate a Certificate Signing Request (CSR):
openssl req -new -key server.key -out server.csr
