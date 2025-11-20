#include <stdio.h>
int main ()
{
    // while lopping syntax 
    int n=1;
    while(n<= 5)
    {
        printf("HI\n");
        n++;
    }
    // write a program to print table of 2 by using while loop
    int i=1;
    while(i<=10)
    {
        printf ("%d\n", 2*i);
        i++;
    }
    int a=1;
    while(a<=10)
    {
        printf ("3 x %d= %d\n",a,3*a);
        a++;
    }
    // write a program to print addition of first 5 no.s using while loop
    int b=1, sum=0;
    while(b<=5)
    {
        printf("Sum of first 5 no.s is %d\n",sum=sum+ b);
        b++;
    }

    return 0;
}
