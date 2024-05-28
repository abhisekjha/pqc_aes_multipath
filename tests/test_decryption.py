#Test case for decryption.py
import os
import unittest
from src.decryption import aes_decrypt

class TestDecryption(unittest.TestCase):
    def test_aes_decrypt(self):
        # Arrange
        message= b'Hello, World!'
        encrypted_message = b'\x'
        session_key = os.urandom(32)
        # Act

        decrypted_message = aes_decrypt(encrypted_message, session_key)
        # Assert
        self.assertEqual(decrypted_message, message)

if __name__ == '__main__':
    unittest.main()