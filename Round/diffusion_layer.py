import numpy as np
import operation as o


def shiftRow(a):
    matrix = np.array(a).reshape(4, 4)
    k = np.transpose(matrix)
    o.leftRotatebyOne(k[1], 4)
    o.leftRotate(k[2], 2, 4)
    o.leftRotate(k[3], 3, 4)
    return k

def InvShift(a):
    matrix = np.array(a).reshape(4,4)
    o.leftRotate(matrix[1],3,4)
    o.leftRotate(matrix[2],2,4)
    o.leftRotatebyOne(matrix[3],4)
    return np.transpose(matrix)

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
                o = galois_multiplication(int(cons_matrix[j][i], 16),
                                          int(a[i][k], 16))
                add ^= o
            mygod.append(hex(add))
    return mygod
