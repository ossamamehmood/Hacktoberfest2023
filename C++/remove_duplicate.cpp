#include<iostream>
using namespace std;

int main()
{
    string str,res="";
    cout<<"Enter Line of String ";
    getline(cin,str);
    int i,j;
    for(i=0;i<str.length();i++){
        for(j=0;j<str.length();j++){
            if(str[i]== str[j]){
                break;
            }
        }
        if(i==j){
            res+=str[i];
        }
    }
    cout<<"Duplicate char remove str = "<<res;
}
