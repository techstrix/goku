# Tool to automate word document creation
Yes I know its stupid but you dont know the pain of copy pasting six different tasks from c files to word and then word starts acting up😭😭😭😭😭😭
If it helps you ok if it doesnt???Spotted an unhandled exception???? Make a pull request and stop yapping

Are you a uon comp science student sick of copy pasting all your code into a word document one by one?? Then goku is for you. You just get the tool and once installed on your system
all you have to do is type goku on your terminal in your current directory.(The one with the tasks e.g. Task1.c,Task2.c,Task3.c). Make sure that when you run goku you have an **output.gok** file in your editor. The output.gok file contains  all the output from your code. So after running your code just copy the output and paste it into the output.gok file.
Example of use 
`main.c
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
` 


