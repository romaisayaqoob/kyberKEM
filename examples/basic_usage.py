import sys
import os
import argparse

# Ensure the project root directory is included in the system path
script_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.insert(0, root_dir)

def main(params_class):
    """
    Main function to initialize the Params object and demonstrate key generation, encryption, and decryption.
    Args:
        params_class: The Params class to initialize.
    """
    try:
        # Initialize the Params object
        params = params_class()
        
        # Example Parameters
        print("Kyber Algorithm Demonstration")
        print("============================")
        print(f"Parameters: KYBER_N={params.KYBER_N}, KYBER_Q={params.KYBER_Q}, KYBER_K={params.KYBER_K}")

        # Step 1: Key Generation (Dummy Example)
        public_key = [i % params.KYBER_Q for i in range(params.KYBER_N)]
        secret_key = [i % params.KYBER_Q for i in range(params.KYBER_N)]
        print("\nStep 1: Key Generation")
        print(f"Public Key: {public_key}")
        print(f"Secret Key: {secret_key}")

        # Step 2: Encryption
        message = "test message".encode()  # Ensure it is in bytes
        try:
            from src.core.encrypt import encrypt
            from src.core.decrypt import decrypt
            ciphertext = encrypt(message, public_key, params)
            if ciphertext:
                print("\nStep 2: Encryption")
                print(f"Ciphertext: {ciphertext}")
                
                # Step 3: Decryption
                decrypted_message = decrypt(ciphertext, secret_key, params)
                print("\nStep 3: Decryption")
                print(f"Decrypted Message: {decrypted_message}")
                
                # Validate if decryption is correct
                # if decrypted_message == message.decode('utf-8'):
                #     print("Decryption successful! The decrypted message matches the original message.")
                # else:
                #     print("Decryption failed. The decrypted message does not match the original message.")
                    
        except Exception as e:
            print(f"An error occurred during the encryption or decryption: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Print Kyber parameter details.")
    parser.add_argument('--params', type=str, default='kyber512', help='Specify the params to use (kyber512, kyber768, kyber1024)')
    args = parser.parse_args()
    
    # Import the Params class from the appropriate location
    if args.params == 'kyber512':
        from params.kyber512 import Params
    elif args.params == 'kyber768':
        from params.kyber768 import Params
    elif args.params == 'kyber1024':
        from params.kyber1024 import Params
    else:
        raise ValueError("Unsupported params type")

    # Get the Params class from the argument
    selected_params_class = Params

    main(selected_params_class)
