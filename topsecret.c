
#include <stdio.h>
int main()
{
    char key[8] = "\xFF\x08\xA0\x04\xFA\xB4\xE9\x78";
    char secret[8] = "topsec";
    char ct[8] = {0};
    int i;
    printf("testo cifrato(hex)");

    for(i=0; i<8; i++) {
        ct[i] = secret[i] ^ key[i];
        printf("%X", ct[i]);

    }

    for (i=0; i<8; i++) {
        ct[i] = ct[i] ^ key[i];
    }
        printf("\nTest decifrato: %s\n", ct);
        return 0;
}
