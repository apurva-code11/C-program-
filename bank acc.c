#include <stdio.h>
int main() {
    char name;
    int age,mobile,accountNumber,balance;

    // Input customer details
        printf("\nEnter Name :  ");
        scanf("%s", &name);

        printf("\nEnter Age :  ");
        scanf("%d", &age);

        printf("\nEnter Mobile Number :  ");
        scanf("%d", &mobile);

        printf("\nEnter Account Number :  ");
        scanf("%d", &accountNumber);

        printf("\nAccount created successfully!\n");
        printf("\ninitial details are: rs.00\n");


        printf("\ninitial balance: rs.");
        scanf("%d", &balance);
       

    // Perform deposit
        int depAmount;
        printf("\n\nEnter amount to be deposit: ");
        scanf("%d", &depAmount);
        balance =balance + depAmount;
        printf("\nAmount deposited successfully!\n", balance);

    // Perform withdraw
        int withdrawAmount;
        printf("\nEnter amount to withdraw: ");
        scanf("%d", &withdrawAmount);
        printf("\nAmount withdraw successfully!\n", balance);

    // Show remaining balance
        int nbalance;
        nbalance = balance - withdrawAmount;
        printf("\n\nRemaining Balance in Account: Rs.%d\n", nbalance);

    return 0;
}
