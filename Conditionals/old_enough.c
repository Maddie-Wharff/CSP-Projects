#include <stdio.h>
#include <stdbool.h>

int main(void){
    int age;
    printf("How old are you?: ");
    scanf("%d", &age);
    if (age >= 18){
        printf("You are old enough to vote!");
    }else if (age >= 16){
        printf("You are old enough to drive!");
    }else if (age >= 15){
        printf("You are old enough to get a learner's permit!");
    }else if (age >= 5){
        printf("You are old enough to go to shcool!");
    }else{
        printf("You are too young to go to school.");
};

    return 0;
}