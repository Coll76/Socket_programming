#!/usr/bin/python3
import os

# Get the path to the id_rsa file in the user's home directory
id_rsa_path = os.path.expanduser('~/.ssh/id_rsa')

# Print the full path
print(id_rsa_path)

