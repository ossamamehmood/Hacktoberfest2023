#include<iostream>
#include<vector>
using namespace std;
int main(){
    string str,str1,res="",r="";
    int carry=0,sum=0;
    cout<<"Enter any String ";
    cin>>str;
    cout<<"Enter any String ";
    cin>>str1;
    int i=str.length()-1;
    int j=str1.length()-1;
    while(i>=0 || j>=0){
        sum=carry;
        if(i>=0){
            sum+=(str[i]-'0');
            i--;
        }
        if(j>=0){
            sum+=(str1[j]-'0');
            j--;
        }
        carry=sum/10;
        sum=sum%10;
        res+=(sum+'0');
    }
    if(carry!=0){
        res+=carry+'0';
    }
    for(i=res.length()-1;i>=0;i--){
        r+=res[i];
    }
    cout<<"Add to string = "<<r;
}