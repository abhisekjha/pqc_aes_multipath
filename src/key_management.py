from pyky.ccakem import kem_keygen512, kem_encaps512, kem_decaps512

def generate_kyber_keypair():
    """Generate a Kyber key pair."""
    return kem_keygen512()

def encrypt_session_key(public_key, session_key):
    """Encrypt a session key using Kyber."""
    return kem_encaps512(public_key)

def decrypt_session_key(private_key, encrypted_session_key):
    """Decrypt a session key using Kyber."""
    return kem_decaps512(private_key, encrypted_session_key)
