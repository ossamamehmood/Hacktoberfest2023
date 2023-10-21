#include <iostream>
using namespace std;
int main()
{
	char val='z';
    cout<<"The ASCII value of "<<val<<" is "<<(int)val<<endl;
    
    char ch='9';
    if( (ch>='a' && ch<='z') || (ch>='A' && ch<='Z'))
    //if( (ch>=97 && ch<=122) || (ch>=65 && ch<=90))
        cout<<"The inserted character " <<ch<<" is an Alphabet";
   
    else
        cout<<"The inserted character " <<ch<<" is not an Alphabet";
}