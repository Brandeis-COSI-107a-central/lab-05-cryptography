#!/usr/bin/env python3

import sys
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

filename = sys.argv[1]
keyfile = sys.argv[2]

with open(keyfile, 'rb') as f:
     keydata = f.read()
     key = keydata[0:32]
     ivec = keydata[32:]

with open(filename, 'rb') as f:
    encrypted_data = f.read()

unpadder = padding.PKCS7(128).unpadder()
unpadded_data = unpadder.update(encrypted_data)

cipher = Cipher(algorithms.AES(key), modes.CBC(ivec))
decryptor = cipher.decryptor()
data = decryptor.update(unpadded_data) + decryptor.finalize()
print(data.decode(), end='')
