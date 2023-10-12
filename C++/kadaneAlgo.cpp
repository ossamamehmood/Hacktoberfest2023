#include<iostream>
#include<vector>
#include<limits.h>

using namespace std;

int maxSubArray(vector<int>& nums) {
  int maxSum = INT_MIN;
  int cSum = 0;
  for(int i=0;i<nums.size();i++){
    cSum += nums[i];

    if(cSum > maxSum){
      maxSum = cSum;
    }

    if(cSum < 0){
      cSum = 0;
    }

  }
  return maxSum;
}

int main(){

  vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};

  cout << maxSubArray(nums) << endl;
  
  return 0;
}