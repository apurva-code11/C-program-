#include <stdio.h>

int main() {
    int n, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    int temp = n;
    while (temp != 0) {
        sum = sum + (temp % 10);
        temp = temp / 10;
    }

    printf("Name: apurva \n");
    printf("Sum of digits = %d\n", sum);
    printf("Name: apurva /n");

    return 0;
}
