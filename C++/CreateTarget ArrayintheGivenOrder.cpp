class Solution {
public:
    vector<int> createTargetArray(vector<int>& nums, vector<int>& index) {
        int n=nums.size();
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(index[j]<=index[i])
                index[i]++;
            }
        }
        vector<int>v(n,0);
        for(int i=0;i<n;i++)
        {
           v[index[i]]=nums[i];
        }
        return v;
    }
};
