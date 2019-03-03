#include <stdio.h>
#include "math.h"
#include "string.h"
#include "ctype.h"

int onlyCoins(float money);
int numOfCoins(int start_coins);

int main() {
    float money_to_give = 0;
    char str[100];
    char not_digit;

    printf("Please, enter a summ of money to give you: ");
    while(money_to_give <= 0){
        fgets(str, 100, stdin);
        if (sscanf(str, "%f %c", &money_to_give, &not_digit) == 1) {
            if (money_to_give <= 0) {
                printf("Please enter > 0: ");
            }
        } else {
            printf("Retry: ");
        }
    }

    int num_of_coins = (int)money_to_give * 4;
    num_of_coins += numOfCoins(onlyCoins(money_to_give));
    printf("The lowest number of coins is: %d", num_of_coins);
}

/*
 * Return sum in coins
 */
int onlyCoins(float money){
    float coins1 = (money - (int)money) * 100;
    int coins = (int)coins1;

    return coins;
}

/*
 * Return number of coins only of coins
 */
int numOfCoins(int start_coins){
    int arr_coins[] = {25, 10, 5, 1};
    int res_num = 0;
    int i = 0;
    while (start_coins){
        if (start_coins >= arr_coins[i]){
            start_coins -= arr_coins[i];
            res_num++;
        } else {
            i++;
        }
    }
    return res_num;
}
