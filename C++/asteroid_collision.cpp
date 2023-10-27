class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> ans;
        int n=asteroids.size();
        for(int i=0;i<n;i++){
            int curr=asteroids[i];
            if(ans.empty() || curr>0 ){
                ans.push_back(curr);
            }
            else{
                while(!ans.empty() && ans.back()>0 && ans.back()<abs(curr)){
                    ans.pop_back();
                }
               if(!ans.empty() && ans.back()+curr==0){
                   ans.pop_back();
               }
               else if(ans.empty() || ans.back()<0){
                   ans.push_back(curr);
               }
            }  
        }
        return ans;
    }
};
