from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b'ThisIsA16ByteKey'  # Must be 16, 24, or 32 bytes

def encrypt(message):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    ct = base64.b64encode(ct_bytes).decode()
    return iv + ":" + ct

def decrypt(encrypted):
    iv, ct = encrypted.split(":")
    cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(ct)), AES.block_size)
    return pt.decode()
