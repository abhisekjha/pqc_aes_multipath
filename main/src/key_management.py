from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt

def generate_kyber_keypair():
    return generate_keypair()

def encrypt_session_key(public_key, session_key):
    encrypted_session_key, encapsulation = encrypt(public_key, session_key)
    return encrypted_session_key

def decrypt_session_key(private_key, encrypted_session_key):
    return decrypt(private_key, encrypted_session_key)
