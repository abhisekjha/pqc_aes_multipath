from ccakem import kem_keygen512, kem_encaps512, kem_decaps512

# Generate Kyber key pairs
private_key, public_key = kem_keygen512()

# Generate a random session key
session_key = b"this is a test session key"

# Encrypt the session key using the public key
ciphertext, encapsulation = kem_encaps512(public_key, session_key)

# Decrypt the session key using the private key
decrypted_session_key = kem_decaps512(private_key, ciphertext)

# Verify the decryption
print("Original session key: ", session_key)
print("Decrypted session key:", decrypted_session_key)
print("Decryption successful:", session_key == decrypted_session_key)
