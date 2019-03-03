#include <stdio.h>
#include "math.h"

char* PrepText(char l, char* text);
int TextLenght(char* text);
void PrintShyfrText(char* text, int col, int len);


int main() {
    char l;
    char text[81];

    PrepText(l, text);
    int len = TextLenght(text);
    int row, col;
    row = sqrt(len);
    if (row * row != len)
        col = row + 1;
    else
        col = row;

    PrintShyfrText(text, col, len);

    return 0;
}

char* PrepText(char l, char* text){
    l = getchar();
    text[0] = l;
    int i = 1;
    while (l != '\n') {
        l = getchar();
        if (l != ' ') {
            text[i] = l;
            ++i;
        }
    }
    return text;
}

int TextLenght(char* text){
    int i = 0;
    while (text[i] != '\n'){
        i++;
    }
    return i;
}

/*
 * Print shyft text
 *
 * input : "apps ucu student me and my friends"
 * output: "aunde pstmn ptmyd suefs udar ceni "
 *
 * */
void PrintShyfrText(char* text, int col, int len){
    int i = 0, prev;
    while (i < col) {
        prev = i;
        for (i; i < len; i = i + col) {
            putchar(text[i]);
        }
        putchar(' ');
        i = prev + 1;
    }
}
