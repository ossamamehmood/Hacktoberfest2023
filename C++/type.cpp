#include<iostream>
#include<typeinfo>

using namespace std;
int main()
{
    char str[20];
    int i,c=0,sum=0,num=0,sum1=0;
    cout<<"Enter any String "<<endl;
    str[0]='7';
    cout<<"Type of str[0] is "<<typeid(str[0]).name()<<endl;
    cout<<"Type of str[0]-'0' is "<<typeid(str[0]-'0').name()<<endl;
}
