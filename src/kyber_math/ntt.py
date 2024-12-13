def ntt(poly, params):
    """Forward Number Theoretic Transform."""
    n = len(poly)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] = (result[i] + poly[j] * pow(params.KYBER_ROOT, i * j % n, params.KYBER_Q)) % params.KYBER_Q
    return result

def inv_ntt(poly, params):
    """Inverse Number Theoretic Transform."""
    n = len(poly)
    n_inv = pow(n, params.KYBER_Q - 2, params.KYBER_Q)  # Modular multiplicative inverse
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] = (result[i] + poly[j] * pow(params.KYBER_ROOT, (n - i) * j % n, params.KYBER_Q)) % params.KYBER_Q
        result[i] = (result[i] * n_inv) % params.KYBER_Q
    return result
