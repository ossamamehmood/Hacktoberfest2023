#include<iostream>
#include<map>
#define ASCII 256
using namespace std;

char getmax(string str){
    int arr[ASCII]={0};
    int len=str.length();
    int m=0;
    char result;
    for(int i=0;i<len;i++){
        arr[str[i]]++;
        if(m<arr[str[i]]){
            m=arr[str[i]];
            result=str[i];
        }
    }
    return result;
}
char getmaxmap(string str){
    map<char,int> mp;
    int len=str.length();
    char result;
    int m=0;
    for(int i=0;i<len;i++){
        mp[str[i]]++;
        if(m<mp[str[i]]){
            m=mp[str[i]];
            result=str[i];
        }
    }
    return result;
}
int main()
{
    string str="hello world";
    cout<<"MAX CHAR = "<<getmax(str)<<endl;
    cout<<"MAX CHAR = "<<getmaxmap(str);
}
