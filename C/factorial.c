#include <stdio.h>
int main()
{
    int i,n ,fact;
    printf("\n\t Enter the value of n : ");
    scanf("%d", &n);
    fact = 1;
    for(i=1 ; i<=n ; i++)
    {
        fact = fact*i;
    }
        printf("\n\tFactorial of %d is : %d",n ,fact);
    
    return 0;
}
