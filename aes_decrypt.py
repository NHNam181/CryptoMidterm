import lookup 
import operation as o
import numpy as np
import aes_encrypt as en
from Round import key_addition_layer as k
from Round import diffusion_layer as d
from Round import byte_substitude_layer as bs

# https://braincoke.fr/blog/2020/08/the-aes-decryption-algorithm-explained/#inverse-transformations

# def xorCipherKey(ciphertext, init_key):
#     subkeys = k.subKeyLis(o.text_to_hex(init_key))
#     #we xor the ciphertext with subkey of the last round
#     result = o.xor(ciphertext, subkeys[10],16)
#     return result

y = ['58', '47', '08', '8B', '15', 'B6', '1C', 'BA', '59', 'D4', 'E2', 'E8', 'CD', '39', 'DF', 'CE']
lastkey = ['e2', '32', 'fc', 'f1', '91', '12', '91', '88', 'b1', '59', 'e4', 'e6', 'd6', '79', 'a2', '93']
init_key = "Thats my Kung Fu"
s1 = o.xor(y,lastkey,16)
print(s1)
matrix = np.array(s1).reshape(4,4)
tran_matrix = np.transpose(matrix)
print(tran_matrix)
inv_cons = np.array(lookup.mixColArrInv)
inv_MC = d.mixColumn(inv_cons, tran_matrix)

inv_shift = d.InvShift(inv_MC)

my_arr = np.array(inv_shift)
mylist = my_arr.flatten().astype(str).tolist()

inv_sub = bs.InSubByte(mylist)

i = o.text_to_hex(init_key)
print("Initial: ",i)

ori = o.xor(inv_sub,o.text_to_hex(init_key),16)

text = ''.join([chr(int(hex_value, 16)) for hex_value in inv_sub])


print(inv_MC)
print(inv_shift)
print(inv_sub)
print(ori)

#
#print(invSubList)



# C = np.array([[0xBA, 0x84, 0xe8, 0x1b],
#               [0x75, 0xa4, 0x8d, 0x40],
#               [0xf4, 0x8d, 0x06, 0x7d],
#               [0x7a, 0x32, 0x0e, 0x5d]])

# def galois_multiplication(a, b):
#     """Galois multiplication of 8 bit characters a and b."""
#     p = 0
#     for counter in range(8):
#         if b & 1: p ^= a
#         hi_bit_set = a & 0x80
#         a <<= 1
#         # keep a 8 bit
#         a &= 0xFF
#         if hi_bit_set:
#             a ^= 0x1b
#         b >>= 1
#     return p


# def mixColumn(cons_matrix, a):
#     mygod = []
#     for j in range(4):
#         for k in range(4):
#             add = 0
#             for i in range(4):
#                 r = galois_multiplication(int(cons_matrix[j][i], 16),
#                                           int(a[i][k], 16))
#                 add ^= r
#             mygod.append(hex(add))
#     return mygod
