#include <stdio.h>

int main() {
    int a, b;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    printf("Name: apurva\n");

    if (a > b)
        printf("Largest = %d\n", a);
    else
        printf("Largest = %d\n", b);

    printf("Name: apurva\n");

    return 0;
}
