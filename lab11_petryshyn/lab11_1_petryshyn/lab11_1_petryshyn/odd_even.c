#include <stdio.h>

int main() {
    int a, b;
    char* num_names[10] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    do{
        printf("Print a: ");
        scanf("%d", &a);
        printf("Print b: ");
        scanf("%d", &b);
    } while (a > b);

    for (int i = a; i <= b; ++i) {
        if (i < 10) {
            printf("%s", num_names[i]);
            printf("\n");
        } else {
            switch (i % 2) {
                case 0:
                    printf("even\n");
                    break;
                default:
                    printf("odd\n");
            }
        }
    }
    return 0;
}
