// LOOPS

#include <stdio.h>
int main () 
{
    // use of i++ operator
   for (int i = 1; i <= 10; i++) 
      printf("%d\n", i);
    // use of i-- operator
   for (int i = 10; i >= 1; i--) 
      printf("%d\n", i);
    
    // add all numbers from 1 to 10
    int sum = 0;
    for (int i = 1; i <= 10; i++) 
        sum += i;
    printf("Sum from 1 to 10 is %d\n\n", sum);

    // add all no. 1 to 10 in row
    int sum1 = 0;
    for (int i = 1; i <= 10; i++) 
    printf("Sum1 from 1 to 10 is %d\n\n", sum1=sum1+i);

    return 0;
}
