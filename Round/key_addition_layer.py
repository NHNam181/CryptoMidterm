import operation as o
import lookup


# Function to perform the g operation
def g(subkey, round):
    w = subkey[12:16]
    o.leftRotatebyOne(w, 4)
    for i in range(0, 4):
        a = w[i]
        w[i] = hex(lookup.sbox[int(a, 16)])[2:]
    x = w[0]
    w[0] = hex(int(x, 16) ^ lookup.RC[round - 1])[2:]
    return w


# Function to perform key addition
def key_generate(subkey, round):
    w0 = subkey[0:4]
    w1 = subkey[4:8]
    w2 = subkey[8:12]
    w3 = subkey[12:16]
    wg = g(subkey, round)
    nk0 = o.xor(w0, wg, 4)
    nk1 = o.xor(nk0, w1, 4)
    nk2 = o.xor(nk1, w2, 4)
    nk3 = o.xor(nk2, w3, 4)
    return nk0 + nk1 + nk2 + nk3


def subKeyLis(init_key):
    pre_subkey = init_key
    subkeys = [init_key]
    # Perform 10 rounds of key expansion
    for i in range(10):
        # the key of next round use the key of the previous round
        pre_subkey = key_generate(pre_subkey, i + 1)
        subkeys.append(pre_subkey)
    return subkeys
