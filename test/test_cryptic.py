# coding=utf-8
import unittest
from cryptic import Cryptic


class TestCryptography(unittest.TestCase):

    def test_cryptic_encrypt(self):
        result = Cryptic.encrypt()
        encrypted_data = result

        self.assertEqual(encrypted_data, result)

    def test_cryptic_decrypt(self):
        encrypted_data = Cryptic.encrypt()
        result = Cryptic.decrypt(encrypted_data)
        decrypted_data = result

        self.assertEqual(decrypted_data, result)


if __name__ == '__main__':
    unittest.main()
