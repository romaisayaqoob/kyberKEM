import time

def simulate_timing_attack(encrypt_func, message, public_key, params):
    """Simulate a timing attack."""
    start_time = time.time()
    ciphertext = encrypt_func(message, public_key, params)
    elapsed_time = time.time() - start_time
    return ciphertext, elapsed_time
