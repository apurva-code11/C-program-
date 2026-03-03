#include <stdio.h>

int main() {
    int a, b;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    a = a + b;
    b = a - b;
    a = a - b;

    printf("Name:apurva \n");
    printf("After swap: %d %d\n", a, b);
    printf("Name:apurva \n");

    return 0;
}
