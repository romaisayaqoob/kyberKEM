def encode_message(message, params):
    """Encode a message into polynomial representation."""
    encoded = [ord(c) for c in message]
    return encoded + [0] * (params.KYBER_N - len(encoded))

def decode_message(encoded, params):
    """Decode polynomial representation back into a message."""
    message = ''.join(chr(x) for x in encoded if x != 0)
    return message
