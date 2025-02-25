#!/usr/bin/env python

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import base64

with open("rsa-key.pub", "rb") as keyfile:
    public_key = serialization.load_pem_public_key(keyfile.read())
with open('test-data/gettysburg.txt', 'r') as f:
    message = f.read().encode()

with open('myfile.sig', 'rb') as f:
    signature = f.read()

public_key.verify(signature, message,
                  padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                              salt_length=padding.PSS.MAX_LENGTH),
                  hashes.SHA256())
