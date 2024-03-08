import operation as o
from Round import key_addition_layer as k

# Initial key
ini_key = "Thats my Kung Fu"
subkey = o.text_to_hex(ini_key)

r = k.subKeyLis(subkey)
print(r)
    
