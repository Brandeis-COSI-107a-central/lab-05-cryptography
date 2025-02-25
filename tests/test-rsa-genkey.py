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

    with open(pubfile, "rb") as keyfile:
        public_key = serialization.load_pem_public_key(keyfile.read())

    with open(privfile, "rb") as keyfile:
        private_key = serialization.load_pem_private_key(keyfile.read(), password=None)

    with open(datafile, 'r') as f:
        message = f.read().encode()

    encrypted_msg = public_key.encrypt(
        message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None))

    decrypted_msg = private_key.decrypt(
        encrypted_msg,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(),
                     label=None))

    if message == decrypted_msg:
        sys.exit(0)
    else:
        print(sys.stderr, "Can't use key to encrypt and decrypt test message")

if __name__ == "__main__":
    main()
