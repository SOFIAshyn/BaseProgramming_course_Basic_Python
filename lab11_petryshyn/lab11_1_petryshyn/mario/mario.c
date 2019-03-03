#include <stdio.h>
#include "ctype.h"


int main() {
    int n = 0;
    char checker[100];
    char check;

    printf("Height: ");
    while(1) {
        fgets(checker, 100, stdin);
        if (sscanf(checker, "%d %c", &n, &check) == 1){
            if (n >= 0 && n <= 23)
                break;
            printf("Height: ");
        } else {
            printf("Retry: ");
        }
    }

    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n + 1; ++j) {
            if (abs(j - n) <= i + 1) {
                printf("#");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}
