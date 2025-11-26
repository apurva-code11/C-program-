#include <stdio.h>

int main() {
    int arr[5] = {12, 56, 3, 99, 24}; // Hardcoded input for simplicity
    int i, max, min;

    // Initialize max and min with the first element
    max = arr[0];
    min = arr[0];

    for(i = 1; i < 5; i++) {
        if(arr[i] > max) {
            max = arr[i];
        }
        if(arr[i] < min) {
            min = arr[i];
        }
    }

    printf("Maximum value: %d\n", max);
    printf("Minimum value: %d\n", min);

    return 0;
}
