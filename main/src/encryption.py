import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

AES_KEY_SIZE = 32  # 256 bits

def generate_aes_key():
    return os.urandom(AES_KEY_SIZE)

def aes_encrypt(message, session_key):
    cipher = AES.new(session_key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))
    return iv + encrypted_message
