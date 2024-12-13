import sys
import os

# Ensure the project root directory is included in the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.insert(0, root_dir)

from params.kyber512 import Params
from src.core.keygen import generate_keys
from src.core.encrypt import encrypt
from src.core.decrypt import decrypt

def encrypt_file(input_file, output_file, public_key, params):
    print(f"Debug: Current working directory is {os.getcwd()}")  # Print current working directory
    if not os.path.exists(input_file):
        print(f"Debug: {input_file} does not exist.")
    with open(input_file, "r") as f:
        message = f.read()
    ciphertext = encrypt(message, public_key, params)
    with open(output_file, "w") as f:
        f.write(str(ciphertext))

def decrypt_file(input_file, output_file, secret_key, params):
    with open(input_file, "r") as f:
        ciphertext = eval(f.read())  # Convert string back to list
    message = decrypt(ciphertext, secret_key, params)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(message)

def decrypt_message(input_file, output_file):
    """Decrpt message directly from input_file to output_file."""
    with open(input_file, "r", encoding="utf-8") as f:
        message = f.read()
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(message)

def main():
    params = Params()
    print("Generating keys...")
    public_key, secret_key = generate_keys(params)
    
    encrypt_file("input.txt", "ciphertext.txt", public_key, params)
    decrypt_file("ciphertext.txt", "decrypted.txt", secret_key, params)
    decrypt_message("input.txt", "decrypt.txt")
    print("File encryption and decryption complete. Check 'decrypted.txt'.")
    

if __name__ == "__main__":
    main()
