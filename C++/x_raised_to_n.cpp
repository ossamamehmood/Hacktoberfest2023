#include <bits/stdc++.h>
using namespace std;


// Calculates the power of a number raised to an integer
// Leetcode Problem number - 50

double myPow(double x, int n)
{
    if (n == 0)
        return 1.0;
    if (n == 1)
        return x;
    if (n == -1)
        return 1.0 / x;

    double half = myPow(x, n / 2);

    if (n % 2 == 0)
        return half * half;
    else if (n > 0)
        return half * half * x;
    else
        return half * half / x;
}
