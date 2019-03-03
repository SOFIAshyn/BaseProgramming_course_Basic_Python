#include <stdio.h>

int main() {
    char l[200];
    char g = 0;
    while (g != '\n'){
        scanf("%s", &l);
        if (l[0] >= 'a' && l[0] <= 'z')
            l[0] -= ('a' - 'A');
        printf("%c", l[0]);
        g = getchar();
    }
    printf("\n");
    return 0;
}