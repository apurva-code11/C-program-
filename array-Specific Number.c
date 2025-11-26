#include <stdio.h>

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int i, target, found = 0;

    printf("Enter number to search: ");
    scanf("%d", &target);

    for(i = 0; i < 5; i++) {
        if(arr[i] == target) {
            printf("Number found at index %d\n", i);
            found = 1;
            break; // Stop loop once found
        }
    }

    if(found == 0) {
        printf("Number not found in the array.\n");
    }

    return 0;
}
