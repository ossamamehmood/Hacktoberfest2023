#include<stdio.h>
#include<time.h>
void delay(float number_of_seconds);
int main()
{
    int a, b, card_number, pin, amount, acc_number;
    printf("Welcome the ATM of XYZ Bank ^_^\n");
    printf("\n");
    printf("Please Choose Service !\n");
    printf("\n");
    printf("1. Cash Withdrawal\n2. Balance enquiry : ");
    scanf("%d", &a);
    float i;
    for(i=0; i<10; i++)
    {
      delay(0.2);
    }

    if (a==1)
    {
        printf("Choose Account type\n");
        printf("1. Domestic\n 2. Savings :  ");
        scanf("%d", &b);
        if (b ==1 || b==2)
        {
            printf("Enter Card Number : ");
            scanf("%d", &card_number);
            for (float j =0;  j<10; j++)
            {
                delay(0.2);
            }
            printf("Enter your pin : ");
            scanf("%d", &pin);
            printf("Wait for a while\n Don't PRESS any Button\n");
            for(float k = 0; k<10; k++)
            {
                delay(0.2);
            } 
            printf("Enter the Amount(In the multiple of 100) : ");
            scanf("%d", &amount);
            for(float l=0; l<10; l++)
            {
                delay(0.5);
            } 
            printf("COLLECT YOUR MONEY ! \n");
            for (float y = 0; y<10; y++)
            {
                delay(0.01);
            }
            printf("Thank you for using the ATM ^_^\n");
        }
    }
    if(a==2)
    {
        printf("Enter Account number : ");
        scanf("%d", &acc_number);
        printf("Enter the ATM Pin : ");
        scanf("%d", &pin);
        for(float h =0; h<10; h++)
        {
            delay(0.5);
        }
        printf("Your Account Balance = ********");
        printf("Thanks for Using ATM of XYZ Bank\n");
    }
    return 0;
}

void delay(float number_of_seconds)
{
    //Converting time into milliseconds
    float milli_seconds= 1000*number_of_seconds;
    //Storing start time 
    clock_t start_time = clock();
    //looping till required time is not achieved
    while (clock() < start_time + milli_seconds);
}

