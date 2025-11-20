#include <stdio.h>
int main() {
    int a,b,c,d,s,m,sum;
    float e,f;
 // Case 1: User input
        printf("Enter no. a :  ");
        scanf("%d", &a);
        printf("Enter no. b :  ");
        scanf("%d", &b);
        sum=a+b;
        printf("value of sum = %d\n",sum);

    // case 2: use only two variables
        //Optimazation
        printf("\nEnter no. s & m:    ");
        scanf("%d%d", &s,&m);

        printf("value of sum = %d",a+b);
        
        
    // case 3:predefined values
        //Optimazation
        c=5,d=10;
        e=5.0,f=10.0;
        printf("\nvalue of sum1 = %d",c+d);
        printf("\nvalue of subt = %d",c-d);
        printf("\nvalue of mult = %d",c*d);
        printf("\nvalue of divi = %f",e/f);

    return 0;
}
