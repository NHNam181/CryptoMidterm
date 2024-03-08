def text_to_hex(text):
    hex_array = []
    for char in text:
        hex_value = hex(ord(char))[2:]
        hex_array.append(hex_value)
    return hex_array


def xor(w1, w2, length):
    nk = [None] * length
    for i in range(length):
        a = w1[i]
        b = w2[i]
        nk[i] = hex(int(a, 16) ^ int(b, 16))[2:]
    return nk


# Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


# Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
