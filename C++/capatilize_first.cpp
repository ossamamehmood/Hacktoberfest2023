#include<iostream>
#include<vector>
using namespace std;
int main(){
    string str="hello  how are you";
    int i;
    for(i=0;i<str.length();i++){
        if(i==0){
            str[i]=toupper(str[i]);
        }
        // else if(str[i]==' ' && str[i+1]!=' '){
        //     str[i+1]=toupper(str[i+1]);
        // }
        else if(str[i-1]==' '){
            str[i]=toupper(str[i]);
        }
    }
    cout<<str;
}