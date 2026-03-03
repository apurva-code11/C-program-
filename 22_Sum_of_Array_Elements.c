#include <stdio.h>

int main() {
    int n, i;
    int arr[100];
    int sum = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
        sum = sum + arr[i];
    }

    printf("Name: apurva \n");
    printf("Sum of array elements = %d\n", sum);
    printf("Name:apurva \n");
    return 0;
}
