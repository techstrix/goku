# Tool to automate word document creation
Yes I know its stupid but you dont know the pain of copy pasting six different tasks from c files to word and then word starts acting up😭😭😭😭😭😭
If it helps you ok if it doesnt???Spotted an unhandled exception???? Make a pull request and stop yapping

Are you a uon comp science student sick of copy pasting all your code into a word document one by one?? Then goku is for you. You just get the tool and once installed on your system
all you have to do is type goku on your terminal in your current directory.(The one with the tasks e.g. Task1.c,Task2.c,Task3.c). Make sure that when you run goku you have an **output.gok** file in your editor. The output.gok file contains  all the output from your code. So after running your code just copy the output and paste it into the output.gok file.
Example of use 
```
  task1.c
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
```
```
task2.c
#include <stdio.h>

int main(){
    printf("Enter a number");
    int num;
    scanf("%d",&num);
    printf("Num *10 is %d",num*10);
    
    return 0;
}
```

```
output.gok
TASK 1
Enter the first number: 12
Enter the second number: 12
Enter the third number: 12
You entered: 12, 12, and 12
TASK 2
Enter a number1
Num *10 is 10
``` 
Please note the **TASK 1** and **TASK 2** these are special and have to be there. Make sure the output for all tasks is given. So if there are five tasks there should be task 1 to task 5.
Its easy when you get output just add it to the gok file. This workflow will greatly save you time. 
And to create a submission file(submission.docx) having followed the above format simply type into your terminal:
> goku
