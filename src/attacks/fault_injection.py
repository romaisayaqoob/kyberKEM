import random

def simulate_fault_injection(secret_key):
    """Simulate a fault injection attack by flipping random bits."""
    faulty_key = bytearray(secret_key)
    for i in range(random.randint(1, 5)):  # Flip 1 to 5 bits
        index = random.randint(0, len(faulty_key) - 1)
        faulty_key[index] ^= 1 << random.randint(0, 7)
    return bytes(faulty_key)
