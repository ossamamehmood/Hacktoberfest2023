#include<iostream>
using namespace std;
class Solution {
public:
    string ans = "";
    void expand(string &s , int left ,int right)
    {
        while(left >= 0 &&  right < s.size())
        {
            if(s[left] != s[right])
                break;
            left--,right++;
        }
        if(ans.size() < right - left )
            ans = s.substr(left + 1 , right - left -1); 
            //eliminate left--(left+1)
            //eliminate right++(right-1)
    }
    string longestPalindrome(string s) {
        for(int i = 0 ; i < s.size() ; i++)
        {
            expand(s , i , i);  //odd palindrome
            expand(s , i , i+1); //even palindrome
        }
        return ans;
    }
};
int main(){
    string input="mithunnibinfazil";
    Solution sol;
    cout<<sol.longestPalindrome(input)<<endl;
    
}