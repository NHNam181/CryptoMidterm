#include <stdio.h>

int modExp(int x, int y, int z) {
    int result = 1;
    x = x % z; 
    
    while (y > 0) {
        if (y % 2 == 1) {
            result = (result * x) % z;
        }
        x = (x * x) % z;
        y /= 2;
    }
    return result;
}

int modInverse(int x, int y) {
    int i;
    for (i = 1; i < y; i++) {
        if ((x * i) % y == 1) {
            return i;
        }
    }
    return -1;  
}

int main() {
    int p,q,d,C;
    printf("Input p: ");
    scanf("%d", &p);

    printf("Input q: ");
    scanf("%d", &q);
    
    printf("Input decryption exponent: ");
    scanf("%d", &d);

    printf("Input ciphertext C: ");
    scanf("%d", &C);

    int N = p * q;
    int r = (p - 1) * (q - 1);
    int inverse = modInverse(d, r);
    
    if (inverse == -1) {
        printf("Decryption failed");
        return 1;
    } else {
        int decrypted = modExp(C, inverse, N);
        printf("Decrypted number is %d", decrypted);
        return 0;
    }
}

