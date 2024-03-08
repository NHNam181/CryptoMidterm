import lookup

def subByte(a):
    for i in range(0, 16):
        x = a[i]
        a[i] = hex(lookup.sbox[int(x, 16)])[2:]
    return a