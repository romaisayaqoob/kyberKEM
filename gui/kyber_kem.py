import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

class MockKyberKEM:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.shared_secret = None

    def generate_keys(self):
        key = RSA.generate(2048)
        self.private_key = key.export_key()
        self.public_key = key.publickey().export_key()

    def encapsulate_key(self):
        recipient_key = RSA.import_key(self.public_key)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        self.shared_secret = get_random_bytes(16)
        ciphertext = cipher_rsa.encrypt(self.shared_secret)
        return ciphertext, self.shared_secret

    def decapsulate_key(self, ciphertext):
        private_key = RSA.import_key(self.private_key)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        self.shared_secret = cipher_rsa.decrypt(ciphertext)
        return self.shared_secret
