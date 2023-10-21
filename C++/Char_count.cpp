#include<iostream>
#include<map>
using namespace std;
int main()
{
    string str;
    int count=0;
    cout<<"Enter Line of String "<<endl;
    getline(cin,str);
    for(int i=0;i<str.length();i++){
        count=0;
        for(int j=0;j<str.length();j++){
            //If a match is found before the current position 
            if(j<i && str[i]==str[j]){ 
                break;
            }
            if(str[i]==str[j]){
                count++;
            }
        }
        if(count!=0){
            cout<<str[i]<<" Used Number of Time "<<count<<endl;
        }
    }
    return 0;
}
