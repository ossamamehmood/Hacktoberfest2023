#include<iostream>
using namespace std;
int main()
{
    char str[20];
    int i,c=0,sum=0,num=0,sum1=0;
    cout<<"Enter any String ";
    gets(str);
    for(i=0;str[i]!='\0';i++){
        if((str[i]>='0') && (str[i]<='9')){
            c++;
            sum+=(str[i]-'0');
            num=num*10+(str[i]-'0');
        }
        else{
            sum1+=num;
            num=0;
        }
    }
    sum1=sum1+num;
    cout<<"Total Number of Digit "<<c<<endl;
    cout<<"Sum of Digit "<<sum;
    
}
