#include<iostream>
using namespace std;

int main()
{
    string str;
    int ch=0,word=0;
    cout<<"Enter Line of String ";
    getline(cin,str);
    for(int i=0;str[i]!='\0';i++){
        if(str[i]==' '){
            if(ch!=0){
                word++;
            }
            ch=0;
        }
        else{
            ch++;
        }
    }
    if(ch!=0){
        word++;
    }
    cout<<"Total Words = "<<word;
}
