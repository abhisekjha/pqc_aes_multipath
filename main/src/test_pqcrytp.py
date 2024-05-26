from pqc import Kyber512

# Generate Kyber key pairs
keypair = Kyber512.generate_keypair()
public_key = keypair.public_key
private_key = keypair.private_key

# Generate a random session key
session_key = b"this is a test session key"

# Encrypt the session key using the public key
ciphertext, encapsulation = Kyber512.encrypt(public_key, session_key)

# Decrypt the session key using the private key
decrypted_session_key = Kyber512.decrypt(private_key, ciphertext)

# Verify the decryption
print("Original session key: ", session_key)
print("Decrypted session key:", decrypted_session_key)
print("Decryption successful:", session_key == decrypted_session_key)
