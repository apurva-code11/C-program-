#include <stdio.h>

int main() {
    int n, i;

    printf("Enter N: ");
    scanf("%d", &n);

    printf("Name: apurva \n");

    for (i = 2; i <= n; i += 2) {
        printf("%d ", i);
    }

    printf("\nName: apurva \n");

    return 0;
}
