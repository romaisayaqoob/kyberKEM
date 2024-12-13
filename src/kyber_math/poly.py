# src/kyber_math/poly.py
import random

def poly_add(a, b, q):
    return [(x + y) % q for x, y in zip(a, b)]

def poly_sub(a, b, q):
    return [(x - y) % q for x, y in zip(a, b)]

def poly_mul(a, b, q):
    result = [0] * len(a)
    for i in range(len(a)):
        for j in range(len(b)):
            result[(i + j) % len(a)] = (result[(i + j) % len(a)] + a[i] * b[j]) % q
    return result

def generate_random_poly(n, q): 
    return [random.randint(0, q - 1) for _ in range(n)]