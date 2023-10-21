#include<stdio.h>
#include<math.h>

//Checking whether a number is Armstrong Number. 

int main()
{
    int num, sum = 0, a, t;

    printf("Enter a number:  ");
    scanf("%d", &num);

    t = num;  // storing into another variable for comparision
    while(num != 0)
    {
        a = n%10;
        sum += a*a*a;
        num = num/10;
    }

    printf("\nsum of cubes of its digits = %d", sum);

    if(sum == t)
        printf("\n%d is an armstrong number !\n", t);
    else
        printf("\n%d is not an armstrong number !\n", t);
    return 0;
}
