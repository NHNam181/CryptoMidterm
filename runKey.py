import operation as o
from Round import key_addition_layer as k

# Initial key
def runKey():
    init = "Thats my Kung Fu"
    subkey = o.text_to_hex(init)
    r = k.subKeyLis(subkey)
    return r


    
