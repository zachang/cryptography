# coding=utf-8


class Cryptography:
    """Implement basic encryption and decryption"""

    def __init__(self, encoding='utf-16'):
        self.encoding = encoding

    def encodes(self):
        """Encode data"""
        data_to_encode = input("Enter data to encode:")
        encoded_data = data_to_encode.encode(self.encoding)
        print("encoded:", encoded_data)
        return encoded_data

    def decodes(self, value):
        """Decodes data"""
        choose_to_decode = input("Please enter (Yes/No) to decode data:")
        if choose_to_decode.lower() == "yes":
            decoded_data = value.decode(self.encoding)
            print("decoded:", decoded_data)
        elif choose_to_decode.lower() == "no":
            return None
        else:
            return self.decodes(value)


if __name__ == '__main__':
    crypto = Cryptography()
    encoding = crypto.encodes()
    crypto.decodes(encoding)
