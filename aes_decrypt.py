import lookup
import operation as o
import runKey as k
from Round import diffusion_layer as d
from Round import byte_substitude_layer as bs


def divideRow(block):
    r1 = block[0:4]
    r2 = block[4:8]
    r3 = block[8:12]
    r4 = block[12:16]
    return [r1, r2, r3, r4]


def firstDecrypt(ciphertext, lastkey):
    matrix_y = d.splitBlock(ciphertext)
    matrix_lask_key = d.splitBlock(lastkey)
    inv_1 = []
    for i in range(4):
        r = o.xor(matrix_y[i], matrix_lask_key[i], 4)
        inv_1.append(r)
    inv_2 = d.InvShift(inv_1)
    inv_3 = bs.InvsubByte(inv_2)
    return inv_3


def decrypt(pre_cipher, key):
    matrix_k = d.splitBlock(key)
    inv_1 = []
    for i in range(4):
        r = o.xor(pre_cipher[i], matrix_k[i], 4)
        inv_1.append(r)
    inv_2 = d.mixColumn(lookup.mixColArrInv, inv_1)
    inv_3 = d.InvShift(divideRow(inv_2))
    inv_4 = bs.InvsubByte(inv_3)
    return inv_4


ciphertext = ['29', 'C3', '50', '5F', '57', '14', '20', 'F6', '40', '22', '99',
              'B3', '1A', '02', 'D7', '3A']
key_add = k.runKey()
pre = firstDecrypt(ciphertext, key_add[10])
for i in range(9, 0, -1):
    pre = decrypt(pre, key_add[i])

init = d.splitBlock(key_add[0])
plain = []
for i in range(4):
    r = o.xor(pre[i], init[i], 4)
    plain.append(r)
print(plain)
