from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#from src.key_management import generate_kyber_keypair
from pyky.ccakem import kem_keygen512, kem_encaps512, kem_decaps512
from src.encryption import generate_aes_key, aes_encrypt
from src.decryption import aes_decrypt

def generate_kyber_keypair():
    """Generate a Kyber key pair."""
    return kem_keygen512()

def test_encryption():
    # Generate Kyber key pair
    
    priv_key, pub_key = generate_kyber_keypair()
    print("Kyber key pair generated.")

    # Generate AES session key
    aes_key = generate_aes_key()
    print("AES session key generated.")

    # Encrypt AES session key with Kyber public key
    encrypted_session_key, _ = kem_encaps512(pub_key)
    print("AES session key encrypted with Kyber public key.")

    # Encrypt a sample message with AES
    message = b"Hello, this is a test message!"
    encrypted_message = aes_encrypt(message, aes_key)
    print("Message encrypted with AES.")

    # Decrypt AES session key with Kyber private key
    decrypted_aes_key = kem_decaps512(priv_key, encrypted_session_key)
    print("AES session key decrypted with Kyber private key.")

    # Decrypt the message with the decrypted AES key
    decrypted_message = aes_decrypt(encrypted_message, decrypted_aes_key)
    print("Message decrypted with AES.")

    # Check if the original message and decrypted message are the same
    assert message == decrypted_message, "Decryption failed: original and decrypted messages do not match!"
    print("Encryption and decryption test passed!")

if __name__ == "__main__":
    test_encryption()
