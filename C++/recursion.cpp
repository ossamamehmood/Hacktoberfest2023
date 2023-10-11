#include <bits/stdc++.h>

using namespace std;

void oneToN(int n)
{
    if (n == 0)
        return;
    oneToN(n - 1);
    cout << ' ' << n;
}

void nToOne(int n)
{
    if (n == 0)
        return;
    cout << n << ' ';
    nToOne(n - 1);
}

int main()
{
    int n;
    cin >> n;
    oneToN(n);
    cout << endl;
    nToOne(n);
    return 0;
}