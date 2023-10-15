Intuition
In these problem we have to find k elements which appeared most frequantly.

Approach
This code is an implementation of a solution to the "Top K Frequent Elements" problem. Given an array of integers nums and an integer k, the task is to return the top k frequent elements in the array.
The implementation uses a combination of unordered_map, multimap, and a vector to solve the problem efficiently.
The unordered_map mp is used to count the frequency of each element in the nums array. The key represents the element, and the value represents its frequency.
The code then creates a multimap m to store the frequency-element pairs from the mp map. The multimap is used to sort the pairs in descending order of frequency. The key represents the frequency, and the value represents the element.
Next, a vector ans of size k is created to store the top k frequent elements. The initial values of the vector elements are set to 0.
The code iterates over the pairs in the m multimap. It assigns the elements to the ans vector in descending order of frequency. The variable cnt keeps track of the current position in the ans vector. The loop breaks once cnt reaches k.
Finally, the ans vector, containing the top k frequent elements, is returned as the solution to the problem.

Complexity
Time complexity:O(nlogn)O(n log n)O(nlogn)
Space complexity:O(n)O(n)O(n)


Code
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int>ans(k,0);
        unordered_map<int,int>mp;
        for(auto &i:nums){
            mp[i]++;
        }
        multimap<int,int,greater<int>>m;
        for(auto &j:mp){
            m.insert({j.second,j.first});
        }
        int cnt=0;
        for(auto &i:m){
            ans[cnt]=i.second;
            cnt++;
            if(cnt==k)break;
        }
        return ans;
    }
};
