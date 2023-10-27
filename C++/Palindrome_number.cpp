// This is a leetcode solution algorithm
class Solution {
public:
    bool isPalindrome(int x) {

        long temp=0,digit=0,sum=0;
        temp=x;
        while(temp>0)
        {
            digit=temp%10;
            sum=(sum*10)+digit;
            temp=temp/10;
        }
        return sum==x;
    }
};
