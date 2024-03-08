import Key_addition_layer.S_box as s
import Key_addition_layer.rotate as r
import numpy as np
import Key_addition_layer.keyyyy as key

# https://braincoke.fr/blog/2020/08/the-aes-decryption-algorithm-explained/#inverse-transformations

C = np.array([[0xBA, 0x84, 0xe8, 0x1b],
              [0x75, 0xa4, 0x8d, 0x40],
              [0xf4, 0x8d, 0x06, 0x7d],
              [0x7a, 0x32, 0x0e, 0x5d]])
mixColArr = np.array([[0x0e, 0x0b, 0x0d, 0x09],
                      [0x09, 0x0e, 0x0b, 0x0d],
                      [0x0d, 0x09, 0x0e, 0x0b],
                      [0x0b, 0x0d, 0x09, 0x0e]])


def galois_multiplication(a, b):
    """Galois multiplication of 8 bit characters a and b."""
    p = 0
    for counter in range(8):
        if b & 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        # keep a 8 bit
        a &= 0xFF
        if hi_bit_set:
            a ^= 0x1b
        b >>= 1
    return p


def mixColumn(cons_matrix, a):
    mygod = []
    for j in range(4):
        for k in range(4):
            add = 0
            for i in range(4):
                r = galois_multiplication(int(cons_matrix[j][i], 16),
                                          int(a[i][k], 16))
                add ^= r
            mygod.append(hex(add))
    return mygod
