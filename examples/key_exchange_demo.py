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

def encrypt_message(message, public_key, params):
    ciphertext = encrypt(message, public_key, params)
    return ciphertext

def decrypt_message(ciphertext, secret_key, params):
    message = decrypt(ciphertext, secret_key, params)
    return message

def main():
    params = Params()
    
    # Alice generates her keys
    print("Alice generates her keys...")
    alice_public_key, alice_secret_key = generate_keys(params)
    print(f"Alice's Public Key: {alice_public_key}")
    print(f"Alice's Secret Key: {alice_secret_key}\n")
    
    # Bob generates his keys
    print("Bob generates his keys...")
    bob_public_key, bob_secret_key = generate_keys(params)
    print(f"Bob's Public Key: {bob_public_key}")
    print(f"Bob's Secret Key: {bob_secret_key}\n")
    
    # Alice shares her public key with Bob
    print("Alice shares her public key with Bob...")
    shared_public_key_from_alice = alice_public_key
    
    # Bob shares his public key with Alice
    print("Bob shares his public key with Alice...")
    shared_public_key_from_bob = bob_public_key
    
    # Bob encrypts a shared secret using Alice's public key
    print("Bob encrypts a shared secret using Alice's public key...")
    shared_secret_message = "shared_secret"
    ciphertext_from_bob = encrypt_message(shared_secret_message, shared_public_key_from_alice, params)
    print(f"Ciphertext from Bob: {ciphertext_from_bob}\n")
    
    # Alice decrypts the shared secret using her secret key
    print("Alice decrypts the shared secret using her secret key...")
    decrypted_message_from_bob = decrypt_message(ciphertext_from_bob, alice_secret_key, params)
    print(f"Decrypted message from Bob: {decrypted_message_from_bob}\n")
    
    # Alice encrypts a shared secret using Bob's public key
    print("Alice encrypts a shared secret using Bob's public key...")
    alice_shared_secret_message = "alice_shared_secret"
    ciphertext_from_alice = encrypt_message(alice_shared_secret_message, shared_public_key_from_bob, params)
    print(f"Ciphertext from Alice: {ciphertext_from_alice}\n")
    
    # Bob decrypts the shared secret using his secret key
    print("Bob decrypts the shared secret using his secret key...")
    decrypted_message_from_alice = decrypt_message(ciphertext_from_alice, bob_secret_key, params)
    print(f"Decrypted message from Alice: {decrypted_message_from_alice}\n")
    
    # Verify shared secrets
    # print("Verifying shared secrets...")
    # if decrypted_message_from_bob != shared_secret_message:
    #     print("Shared secret decrypted by Alice matches the original secret sent by Bob.")
    # else:
    #     print("Shared secret decrypted by Alice does NOT match the original secret sent by Bob.")
    
    # if decrypted_message_from_alice != alice_shared_secret_message:
    #     print("Shared secret decrypted by Bob matches the original secret sent by Alice.")
    # else:
    #     print("Shared secret decrypted by Bob does NOT match the original secret sent by Alice.")
    print("Key exchange demonstration complete.")

if __name__ == "__main__":
    main()
