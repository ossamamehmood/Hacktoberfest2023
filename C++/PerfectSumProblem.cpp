#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{

	public:
	int mod = 1000000007;

	int helper(int arr[],int n,int ind,int sum,int sample,vector<vector<int>> &dp){
	    if(sample > sum)
	        return 0;
	        
	    if(sum == sample)
	        return 1;
	        
	    if(ind == n){
            if(sum == sample)
                return 1;
	        return 0;
	    }
	    
	    if(ind>n){
	        return 0;
	    }
	    
	    if(dp[ind][sample] != -1)
	        return dp[ind][sample];
	        
	    int nottake = helper(arr, n, ind+1, sum, sample, dp);
	    int take = helper(arr, n, ind+1, sum, sample+arr[ind], dp);
	    return dp[ind][sample] = (take+nottake) % mod;
	}
	int perfectSum(int arr[], int n, int sum)
	{
        // Your code goes here
        int sample = 0;
        sort(arr, arr + n);
        vector<vector<int>> dp(n, vector<int> (sum,-1));
        int ans = helper(arr, n, 0, sum, sample, dp);
        return ans % mod;
	}
	  
};

//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        int n, sum;

        cin >> n >> sum;

        int a[n];
        for(int i = 0; i < n; i++)
        	cin >> a[i];

       

	    Solution ob;
	    cout << ob.perfectSum(a, n, sum) << "\n";
	     
    }
    return 0;
}

// } Driver Code Ends
