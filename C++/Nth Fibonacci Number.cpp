/*

                                                Nth Fibonacci Number

Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

Example 1:

Input: 
n = 2
Output: 
1 

Explanation: 
1 is the 2nd number of fibonacci series.



Example 2:

Input: 
n = 5
Output: 
5

Explanation: 
5 is the 5th number of fibonacci series.


*/





#include <bits/stdc++.h>
using namespace std;


class Solution {
  public:
  
   const long long mod = 1e9+7;
    long long int nthFibonacci(long long int n)
    {
        //prestoring
        long long int dp[n+5];
        //initializing dp[0] as 0
        dp[0]=0;
        //initializing dp[1] as 1
        dp[1]=1;
        for(int i=2;i<=n;i++)
        {
            //as same as fibonacci formula f(i)=f(i-1)+f(i-2)
            dp[i]=(dp[i-1]%mod + dp[i-2]%mod)%mod;
        }
        //returning nth value
        return dp[n];
    }
};


int main() {
    int t;
    cin >> t;
    while (t--) {
        long long int n;
        cin >> n;
        Solution ob;
        cout << ob.nthFibonacci(n) << endl;
    }
    return 0;
}
