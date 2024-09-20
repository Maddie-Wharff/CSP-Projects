#include <stdio.h>
#include <string.h>

int main(void){
    char product[26], name[20];
    printf("What's your name?: ");
    scanf("%s", name);
    strcat(product, "~~~");
    strcat(product, name);
    strcat(product, "~~~");
    strcat(product, "\n");
    printf("%s", product);
    return 0;
}