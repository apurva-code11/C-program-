//         //  ARRAY
// int size,numbers;
// data_type array_name[size];
// int numbers[5];  // declares an array of 5 integers
// int numbers[5] = {10, 20, 30, 40, 50};
// printf("%d", numbers[2]);  // prints 3rd element → 30


#include <stdio.h>

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};
    int i;

    for (i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }

    return 0;
}
