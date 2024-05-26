import sys
import os

# Add the pyky directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pyky')))

from ccakem import kem_keygen512, kem_encaps512, kem_decaps512
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Generate Kyber key pairs for the recipient
priv_key, pub_key = kem_keygen512()

# Encrypt the AES session key using the recipient's public key with Kyber
secret1, cipher = kem_encaps512(pub_key)

# Inspect secret1
print("Original secret1:", secret1)

# Ensure secret1 is bytes
if isinstance(secret1, list):
    # Convert each integer to a byte and join them
    secret1 = bytes([x % 256 for x in secret1])

# Inspect the converted secret1
print("Converted secret1:", secret1)

# Define the message
message = "Hello World".encode()

# Encrypt the message using AES-256
def aes_encrypt(message, session_key):
    cipher = AES.new(session_key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_message = cipher.encrypt(pad(message, AES.block_size))
    return iv + encrypted_message

# Decrypt the message using AES-256
def aes_decrypt(encrypted_message, session_key):
    iv = encrypted_message[:16]
    cipher = AES.new(session_key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message[16:]), AES.block_size)
    return decrypted_message

# Encrypt the message
encrypted_message = aes_encrypt(message, secret1)
print("Encrypted Message:", encrypted_message)

# Decrypt the session key using the recipient's private key with Kyber
secret2 = kem_decaps512(priv_key, cipher)

# Ensure secret2 is bytes
if isinstance(secret2, list):
    # Convert each integer to a byte and join them
    secret2 = bytes([x % 256 for x in secret2])

# Decrypt the message
# Resume Tailor
decrypted_message = aes_decrypt(encrypted_message, secret2)
print("Decrypted Message:", decrypted_message.decode())
