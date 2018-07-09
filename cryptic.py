# coding=utf-8
from Crypto.Cipher import AES


class Cryptic:
    """Encryption with pyCryto library"""

    @staticmethod
    def encrypt():
        """Encryption method"""

        data = input('Enter data to encrypt:')

        if len(data) % 16 != 0:
            return "Data to encrypt must be multiple of 16 characters"
        else:
            encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
            cipher_text = encryption_suite.encrypt(data)
            print(cipher_text)
            return cipher_text

    @staticmethod
    def decrypt(encrypted_data):
        """Decryption method"""
        if len(encrypted_data) % 16 != 0:
            return "Data to encrypt must be multiple of 16 characters"
        else:
            decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
            plain_text = decryption_suite.decrypt(encrypted_data)

        return plain_text


if __name__ == '__main__':
    encryption = Cryptic.encrypt()
    print(Cryptic.decrypt(encryption))

