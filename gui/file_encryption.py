from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class FileEncryptor:
    def encrypt_file(self, input_file, output_file, shared_secret):
        cipher = AES.new(shared_secret, AES.MODE_CBC)
        iv = cipher.iv
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        with open(output_file, 'wb') as f:
            f.write(iv + ciphertext)

class FileDecryptor:
    def decrypt_file(self, input_file, output_file, shared_secret):
        with open(input_file, 'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()
        cipher = AES.new(shared_secret, AES.MODE_CBC, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        with open(output_file, 'wb') as f:
            f.write(plaintext)
