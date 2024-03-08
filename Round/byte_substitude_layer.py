import lookup


def subByte(a):
    for i in range(0, 16):
        x = a[i]
        a[i] = hex(lookup.sbox[int(x, 16)])
    return a


def InvsubByte(a):
    for row in a:
        for i in range(len(row)):
            x = row[i]
            row[i] = hex(lookup.sboxInv[int(x, 16)])
    return a
