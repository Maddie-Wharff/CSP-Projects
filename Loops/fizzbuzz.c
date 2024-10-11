#include <stdio.h>
#include <string.h>
#include <time.h>

int i, usr;
char one[50], two[50], three[50];

void delay(int sec){
    int milli = 1000*sec;

    clock_t start = clock();

    while(clock()< start+milli);
}

int main(void){
    printf("Give me a number: \n");
    scanf("%d", &usr);
    printf("Give me a word: \n");
    scanf("%s", one);
    printf("Give me another word: \n");
    scanf("%s", two);
    strcat(three, one);
    strcat(three, two);
    //create a loop that counts to 50 
        for(i=1; i<=usr; i++){
        
    //replace divisible by both with fizzbuzz
    if(i%3==0 && i%5==0){
        printf("%s\n", three);

    //replace numbers divisable by 3 with fizz
}else if (i%3==0){
        printf("%s\n", one);

    //replace numbers divisible by 5 with buzz
}else if(i%5==0){
    printf("%s\n", two);

    //print all other numbers
    }else{
        printf("%d\n", i);
    }
    delay(10);
}
    return 0;
}