#include <stdio.h>

int main(void){
    char name[30];
    printf("What's your name?: \n");
    scanf("%s", name);
    printf("Hello %s", name);
    return 0;
}