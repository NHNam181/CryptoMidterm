import lookup
import operation as o
from Round import diffusion_layer as d
from Round import byte_substitude_layer as bs
from Round import key_addition_layer as ka


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


def encrypt(plaintext, init_key):
    key = ka.subKeyLis(o.text_to_hex(init_key))
    cipher = o.xor(o.text_to_hex(plaintext), key[0], 16)
    for i in range(10):
        cipher = bs.subByte(cipher)
        cipher = d.shiftRow(cipher)
        if i != 9:
            cipher = d.mixColumn(lookup.fixed_matrix, cipher)
        else:
            temp = []
            for k in range(4):
                for j in range(4):
                    temp.append(cipher[j][k])
            cipher = temp
        cipher = o.xor(cipher, key[i + 1], 16)
    return cipher


init_key = "Thats my Kung Fu"
plaintext = "Two One Nine Two"
plaintext = padding(plaintext)
cipher_hex = encrypt(plaintext, init_key)
print(d.splitBlock(cipher_hex))

print("\nAter convert to text: ")
# Convert each inner list to a text string
text_list = [''.join([chr(int(hex_value, 16)) for hex_value in inner_list]) for inner_list in d.splitBlock(cipher_hex)]

# Print the resulting text strings
for text in text_list:
    print(text)