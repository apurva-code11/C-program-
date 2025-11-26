#include <stdio.h>

int main() {
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int i, even = 0, odd = 0;

    for(i = 0; i < 10; i++) {
        if(arr[i] % 2 == 0) {
            even++;
        } else {
            odd++;
        }
    }

    printf("Total Even numbers: %d\n", even);
    printf("Total Odd numbers: %d\n", odd);

    return 0;
}
