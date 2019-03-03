#include <stdio.h>
#include "string.h"
#include "ctype.h"

void shyfr_with_vigenere(char* sen, char* k);

int main(int argc, char *argv[]) {
    if (argc != 2){
        printf("You shound enter a key with letters");
        return 1;
    }


    char* key = argv[1];

    for (int i = 0; i < strlen(key); i++){
        if (!isalpha(key[i])){
            return 1;
        }
    }

    char sen[100];
    fgets(sen, 100, stdin);

    shyfr_with_vigenere(sen, key);

    return 0;
}

void shyfr_with_vigenere(char* sen, char* k){
    char shyfred_text[100];
    for (int i = 0, j = 0; i < strlen(sen); i++, j++){
        if (j == strlen(k))
            j = 0;
        if (sen[i] >= 'a' && sen[i] <= 'z') {
            shyfred_text[i] = (sen[i] + tolower(k[j]) - 194) % 26 + 97;
        } else if (sen[i] >= 'A' && sen[i] <= 'Z') {
            shyfred_text[i] = (sen[i] + toupper(k[j]) - 65 * 2) % 26 + 65;
        } else {
            shyfred_text[i] = sen[i];
            j--;
        }
        printf("%c", shyfred_text[i]);
    }
}
