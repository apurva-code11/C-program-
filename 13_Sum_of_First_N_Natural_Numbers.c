#include <stdio.h>

int main() {
    int n, i;
    int sum = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        sum = sum + i;
    }

    printf("Name: apurva \n");
    printf("Sum = %d\n", sum);
    printf("Name: apurva \n");

    return 0;
}
