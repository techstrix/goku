#include <stdio.h>

int main(){
    int number1, number2, number3;
    printf("Enter the first number: ");
    fflush(stdout);
    scanf("%d", &number1);

    printf("Enter the second number: ");
    fflush(stdout);
    scanf("%d", &number2);

    printf("Enter the third number: ");
    fflush(stdout);
    scanf("%d", &number3);
 


    printf("You entered: %d, %d, and %d", number1, number2, number3);
    return 0;
}