from src.kyber_math.poly import poly_add, poly_mul
from src.kyber_math.ntt import ntt
from src.kyber_math.sampling import generate_noise
from src.utils.compression import compress

def encrypt(message, public_key, params):
    """Encrypt a message using the public key."""
    try:
        # Convert the message to string if it's in bytes
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        
        # Encode message into polynomial
        message_poly = [ord(c) % params.KYBER_Q for c in message]
        
        # Ensure the polynomial is of the correct length
        if len(message_poly) < params.KYBER_N:
            message_poly += [0] * (params.KYBER_N - len(message_poly))
        elif len(message_poly) > params.KYBER_N:
            message_poly = message_poly[:params.KYBER_N]

        # Transform public key and message into NTT domain
        public_ntt = ntt(public_key, params)
        message_ntt = ntt(message_poly, params)

        # Generate noise polynomial
        noise_poly = generate_noise(params)
        if len(noise_poly) != params.KYBER_N:
            raise ValueError("Generated noise polynomial has incorrect length.")
        
        # Perform polynomial operations with the modulus q
        encrypted_poly = poly_add(poly_mul(public_ntt, message_ntt, params.KYBER_Q), noise_poly, params.KYBER_Q)
        
        # Compress ciphertext
        ciphertext = compress(encrypted_poly, params.KYBER_Q // 4)
        print(f"Debug: Encrypted poly: {encrypted_poly}")  # Debugging statement
        return ciphertext
    
    except Exception as e:
        print(f"An error occurred during encryption: {e}")
        return None
