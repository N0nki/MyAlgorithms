# coding; utf-8

"""
PythonのモジュールでBase64
"""

import binascii
import struct

img_binary = open("mygithubicon.png", "rb").read()
# print(img_binary)
# print(struct.unpack("c", img_binary))
base64_encoded = binascii.b2a_base64(img_binary)
base64_decoded = binascii.a2b_base64(base64_encoded)
print(base64_encoded)
print(base64_decoded)
