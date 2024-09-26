#include <stdio.h>

void hi(char name[]){
        printf("Hello %s! \n", name);
}

int main(void){
    hi("Emily");
    hi("George");
    hi("Jason");
    hi("Audrey");
    hi("Ashlynn");
    return 0;
}