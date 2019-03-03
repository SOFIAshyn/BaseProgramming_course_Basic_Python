#include <stdio.h>
#include "stdlib.h"
#include "string.h"
#include "ctype.h"

int main(int argc, char* argv[]) {
    if (argc == 1 || argc > 2)
        return 1;
    char *k = argv[1];
    for (int i = 0; i < strlen(k); i++) {
        if (!isdigit(k[i]))
            return 1;
    }
    int key = atoi(argv[1]);

    char sen[100];
    char l;
    l = getchar();
    sen[0] = l;
    int i = 1;
    while (l != '\n'){
        l = getchar();
        sen[i] = l;
        i++;
    }

    char shyfr[100];
    for (int j = 0; j < strlen(sen); j++){
        if (sen[j] >= 'A' && sen[j] <= 'Z')
            shyfr[j] = (sen[j] - 65 + key) % 26 + 65;
        else if (sen[j] >= 'a' && sen[j] <= 'z')
            shyfr[j] = (sen[j] - 97 + key) % 26 + 97;
        else
            shyfr[j] = sen[j];
        printf("%c", shyfr[j]);
    }

    return 0;
}
