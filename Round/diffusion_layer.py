import operation as o


def shiftRow(block):
    r1 = []
    r2 = []
    r3 = []
    r4 = []

    # Split up block into rows
    for i in range(4):
        r1.append(block[4 * i])
        r2.append(block[4 * i + 1])
        r3.append(block[4 * i + 2])
        r4.append(block[4 * i + 3])
    o.leftRotatebyOne(r2, 4)
    o.leftRotate(r3, 2, 4)
    o.leftRotate(r4, 3, 4)
    return [r1, r2, r3, r4]

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
