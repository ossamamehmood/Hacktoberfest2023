class Solution {
public:
    
    int countofSubsetSum(vector<int>& nums, int sum)
    {
        int n=nums.size(); 
        int dp[n+1][sum+1];
        
        for(int j=0; j<sum+1; j++)
        {
            dp[0][j]=0;
        }
        
        for(int i=0; i<n+1; i++)
        {
            dp[i][0]= 1;   
        }
        
        for(int i=1; i<n+1; i++)
        {
            for(int j=0; j<sum+1; j++)
            {
               if(nums[i-1] <= j)
                   dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
                else dp[i][j]= dp[i-1][j];
            }
        }
        
        return dp[n][sum];
        
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum_arr=0; 
        for(int x: nums)
        {
            sum_arr+= x;
        }
        
        
        int sum= (target+ sum_arr)/2;
        
        if( (target+ sum_arr) % 2 != 0 || sum_arr < target) return 0; 
        
        
        return countofSubsetSum(nums, sum); 
    }
};
