#include <stdio.h>

int main() {
    int arr[5], i;

    printf("Enter 5 numbers: ");
    for(i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
    }

    printf("\nArray in Reverse Order:\n");
    // Loop starting from last index (4) down to 0
    for(i = 4; i >= 0; i--) {
        printf("%d ", arr[i]);
    }

    return 0;
}
