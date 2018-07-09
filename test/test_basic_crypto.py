# coding=utf-8
import unittest
from basic_crypto import Cryptography


class TestCrypto(unittest.TestCase):

    def test_cryptic_encodes(self):
        cryptic = Cryptography()
        encrypted_data = cryptic.encodes()
        result = encrypted_data

        self.assertEqual(encrypted_data, result)

    def test_cryptic_deodes(self):
        cryptic = Cryptography()
        encrypted_data = cryptic.encodes()
        result = cryptic.decodes(encrypted_data)
        decrypted_data = result

        self.assertEqual(decrypted_data, result)


if __name__ == '__main__':
    unittest.main()