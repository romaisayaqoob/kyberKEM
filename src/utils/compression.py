# src/utils/compression.py

def compress(poly, factor):
    """Compress polynomial by reducing its coefficients."""
    compressed_poly = [(coeff // factor) for coeff in poly]
    return compressed_poly

def decompress(compressed_poly, factor):
    """Decompress polynomial by restoring its coefficients."""
    decompressed_poly = [(coeff * factor) for coeff in compressed_poly]
    return decompressed_poly
