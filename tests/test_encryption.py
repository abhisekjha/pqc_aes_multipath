#test case for encryption.py
import os
import unittest
from Crypto.Cipher import AES
from src.encryption import generate_aes_key, aes_encrypt

class TestEncryption(unittest.TestCase):
    def test_generate_aes_key(self):
        # Arrange
        # Act
        key = generate_aes_key()
        # Assert
        self.assertEqual(len(key), 32)

    def test_aes_encrypt(self):
        # Arrange
        message = b'Hello, World!'
        session_key = os.urandom(32)
        # Act
        encrypted_message = aes_encrypt(message, session_key)
        # Assert
        self.assertNotEqual(encrypted_message, message)
        self.assertEqual(len(encrypted_message), 48)

if __name__ == '__main__':
    unittest.main()

    