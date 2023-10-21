

#include<iostream>
#include<vector>
using namespace std;

int main()
{
    string s="nibin";
    int flag=1;
    int l=0,r=s.length()-1;
    while(l<r || l!=r){
        if(s[l]!=s[r]){
            flag=0;
            break;
        }
        l++;
        r--;
    }
    if(flag==1){
        cout<<"Palindrome";
    }
    else{
        cout<<"Not a Palindrome";
    }
    return 0; 
}
