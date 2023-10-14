#include <stdio.h>
 //general method
// int main()
// {
//   int n, first = 0, second = 1, next, c;
 
//   printf("Enter the number of terms\n");
//   scanf("%d", &n);
 
//   printf("First %d terms of Fibonacci series are:\n", n);
 
//   for (c = 0; c < n; c++)
//   {
//     if (c <= 1)
//       next = c;
//     else
//     {
//       next = first + second;
//       first = second;
//       second = next;
//     }
//     printf("%d\n", next);
//   }
 
//   return 0;
// }
//recursion type
int fib(int n)
{
 if(n==1 || n==0 )
{
return n;
}
else
{
return fib(n-1) + fib(n-2);
}
}
int main()
{
 printf("%d",fib(4)); //you can enter can number in place of 4 to get series of 4 terms
 return 0;
}
