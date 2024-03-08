import lookup
import numpy as np
import operation as o
from Round import diffusion_layer as d
from Round import byte_substitude_layer as bs
from Round import key_addition_layer as k


# Ensure the length of input is a multiple of 16 bytes (128 bits)
def padding(text):
    check = len(text) % 16
    if check == 0:
        return text
    else:
        add = 16 - check
        for i in range(add):
            text.append(str(add))
        return text


cons_matrix = np.array(lookup.fixed_matrix)


def encrypt(plaintext, init_key):
    key = k.subKeyLis(o.text_to_hex(init_key))
    cipher = o.xor(o.text_to_hex(plaintext),
                       key[0], 16)
    for i in range(10):
        cipher = bs.subByte(cipher)
        cipher = d.shiftRow(cipher)
        if i != 9:
            cipher = d.mixColumn(cons_matrix, cipher)
        cipher = o.xor(cipher,key[i], 16)
    return cipher


init_key = "Thats my Kung Fu"
plaintext = "Two One Nine Two"
plaintext = padding(plaintext)
print(k.subKeyLis(o.text_to_hex(init_key)))
ciphertext = encrypt(plaintext, init_key)
print(ciphertext)
