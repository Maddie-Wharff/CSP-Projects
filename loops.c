#include <stdio.h>
char siblings[3][20] = {"Zak", "Teagan", "Rory"};
int i;
int main(){
    while (i < 3){
        printf("%s\n", siblings[i]);
        i+1;
        break;
    }
    return 0;
}