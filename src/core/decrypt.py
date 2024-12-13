from src.kyber_math.poly import poly_add, poly_sub, poly_mul
from src.kyber_math.ntt import inv_ntt,ntt
from src.utils.compression import decompress

def decrypt(ciphertext, secret_key, params):
    """Decrypt ciphertext using the secret key."""
    try:
        # Decompress the ciphertext
        encrypted_poly = decompress(ciphertext, params.KYBER_Q // 4)
        print(f"Debug: Decompressed poly: {encrypted_poly}")  # Debugging statement
        
        # Transform secret key into NTT domain
        secret_ntt = ntt(secret_key, params)
        print(f"Debug: Secret NTT: {secret_ntt}")  # Debugging statementsae
        
        # Perform polynomial operations
        decrypted_ntt = poly_sub(encrypted_poly, poly_mul(secret_ntt, encrypted_poly, params.KYBER_Q), params.KYBER_Q)
        print(f"Debug: Decrypted NTT: {decrypted_ntt}")  # Debugging statement
        
        # Transform back from NTT domain
        decrypted_poly = inv_ntt(decrypted_ntt, params)
        print(f"Debug: Decrypted poly: {decrypted_poly}")  # Debugging statement
        
        # Decode polynomial back into message
        message = ''.join(chr(v % params.KYBER_Q) for v in decrypted_poly)
        
        return message.strip('\x00')  # Remove padding zeros
    
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None
