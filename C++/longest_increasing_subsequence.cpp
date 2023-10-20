#include <iostream>
#include <vector>
using namespace std;

int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(),1);
        int maxi = 1;

        for(int i=0;i<nums.size();i++){
            for(int j=0;j<=i-1;j++){
                if(nums[i]>nums[j])
                dp[i] = max(dp[j]+1,dp[i]);
            }
            maxi = max(dp[i],maxi);
        }
        return maxi;
}

int main(){

    int n;
    cin>>n;

    vector<int> a(n);

    for(int i=0;i<n;i++)
    cin>>a[i];

    cout<<lengthOfLIS(a)<<endl;
}
