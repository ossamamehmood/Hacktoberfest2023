#include<stdio.h>
int main()
{
    float TA, I, SL, HL, VL, ML;
    int WL;
    printf("What Loan do you want?\n 1.) Press 1 for Student Loan \n 2.) Press 2 for Home Loan \n 3.) Press 3 for Vehicle Loan \n 4.) Press 4 for Medical Loan \n ");
    scanf("%d",&WL);
    
    switch(WL)
    {
        case 1 :{
            I = 5;
            printf("How much Student Loan do you want? : \n");
            scanf("%f",&SL);
            TA = (SL*I/100 + SL)/12;
            printf("At the end of every month for a year you have to pay: %f\n",TA);
            break;
        }
        case 2 :{
            I = 10;
            printf("How much Home Loan do you want? : \n");
            scanf("%f",&HL);
            TA = (HL*I/100 + HL)/36;
            printf("At the end of every month for 3 years you have to pay: %f\n",TA);
            break;
        }
        case 3 :{
            I = 12;
            printf("How much Vehicle Loan do you want? : \n");
            scanf("%f",&VL);
            TA = (VL*I/100 + VL)/12;
            printf("At the end of every month for a year you have to pay: %f\n",TA);
            break;
        }
        case 4 :{
            I = 8;
            printf("How much Medical Loan do you want? : \n");
            scanf("%f",&ML);
            TA = (ML*I/100 + ML)/12;
            printf("At the end of every month for a year you have to pay: %f\n",TA);
            break;
        }
        default :{
            printf("Invalid Input \n ");
        }
    }
    return 0;
}
