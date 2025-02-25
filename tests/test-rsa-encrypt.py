#!/usr/bin/env python3
#
# Test that the key pair in the files given on the command line can be used
# be used to encrypt and decrypt a file.

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

import sys

def main():
    pubfile = 'rsa-key.pub'
    privfile = 'rsa-key.priv'
    datafile = 'test-data/short-msg.txt'

    with open(privfile, "rb") as keyfile:
        private_key = serialization.load_pem_private_key(keyfile.read(), password=None)

    with open('encrypted.bin', 'rb') as f:
        encrypted_msg = f.read()

    decrypted_msg = private_key.decrypt(
        encrypted_msg,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None))
    print(decrypted_msg.decode(), end='')

if __name__ == "__main__":
    main()
