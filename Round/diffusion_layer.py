import operation as o
from Round import diffusion_layer as d


def splitBlock(block):
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    for i in range(4):
        r1.append(block[4 * i])
        r2.append(block[4 * i + 1])
        r3.append(block[4 * i + 2])
        r4.append(block[4 * i + 3])
    all = [r1, r2, r3, r4]
    return all


def shiftRow(block):
    all = splitBlock(block)
    o.leftRotatebyOne(all[1], 4)
    o.leftRotate(all[2], 2, 4)
    o.leftRotate(all[3], 3, 4)
    return all


def InvShift(block):
    o.leftRotate(block[1], 3, 4)
    o.leftRotate(block[2], 2, 4)
    o.leftRotatebyOne(block[3], 4)
    return block


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
    for k in range(4):
        for j in range(4):
            add = 0
            for i in range(4):
                o = galois_multiplication(int(cons_matrix[j][i], 16),
                                          int(a[i][k], 16))
                add ^= o
            mygod.append(hex(add))
    return mygod
