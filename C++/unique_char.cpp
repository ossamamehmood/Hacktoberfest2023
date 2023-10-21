#include<iostream>
using namespace std;
int main(){
    string str,st="";
    int i,j,f=0,c=0,index=-1,l,cc=0;
    cout<<"Enter Line of String ";
    getline(cin,str);
    l=str.length();
    for(i=0;i<l;i++){
        c=0;
        for(j=0;j<l;j++){
            if(str[i]==str[j]){
                c++;
            }
        }
        if(c==1){
            st=str[i];
            index=i;
            f=1;
            cc++;
            //break;
        }
    }
    if(f==0){
        cout<<"Unique Char Not found";
    }
    else{
        cout<<st<<" Unique char found at "<<index<<endl;
        cout<<"Number of unique characters is "<<cc;
    }
}