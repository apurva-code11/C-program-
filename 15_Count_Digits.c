#include <stdio.h>

int main() {
    int n, count = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    int temp = n;
    while (temp != 0) {
        count++;
        temp = temp / 10;
    }

    printf("Name: apurva \n");
    printf("Digits = %d\n", count);
    printf("Name:apurva \n");

    return 0;
}
