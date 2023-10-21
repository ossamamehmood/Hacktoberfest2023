#include<iostream>
#include<vector>
using namespace std;

int main()
{
    string str,str1,res="";
    int i=0,j=0,prod=0,carry=0,cur=0;
    str="51";
    str1="61";
    // cout<<"Enter First String ";
    // cin>>str;
    // cout<<"Enter Second String ";
    // cin>>str1;
    int l=str.length();
    int l1=str1.length();
    int s=l+l1;
    //int a[s]={0};
    vector<int> a(s,0);
    for(i=l-1;i>=0;i--){
        for(j=l-1;j>=0;j--){
            prod=(str[i]-48)*(str1[j]-48);
            cur=a[i+j+1]+prod;
            a[i+j+1]=cur%10; //remainder
            a[i+j]+=cur/10;  //Extra
        }
    }  
    int k=0;
    if(a[0]==0)
        k=1;
    else
        k=0;
    for(i=k;i<s;i++){
        res+=a[i]+'0';
    }
    cout<<res;
}
