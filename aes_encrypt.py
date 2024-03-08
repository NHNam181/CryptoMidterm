import lookup
import numpy as np
import operation as o
from Round import diffusion_layer as d 
from Round import byte_substitude_layer as bs
from Round import key_addition_layer as k

#ensure the input having enough 16 bytes
def padding(array):
    check = len(array)%16
    if check == 0:
        return array
    else:
        add = 16 - check
        temp = "0"+ str(add)
        for i in range(add):
            array.append(temp)
        return array

cons_matrix = np.array(lookup.fixed_matrix)

def encryp(plaintext, init_key):
    key_add = k.subKeyLis(o.text_to_hex(init_key))
    t1 = o.xor(o.text_to_hex(plaintext),key_add[0],16)
    print(t1)
    t2 = bs.subByte(t1)
    print(t2)
    t3 = d.shiftRow(t2)
    print(t3)
    t4 = d.mixColumn(cons_matrix, t3)
    return t4
    

init_key = "Thats my Kung Fu"
plaintext = "Two One Nine Two"

r = encryp(plaintext, init_key)
print(r)




        