#include<iostream>
#include<vector>  //vector->length()  string->size()
using namespace std;
int main()
{
    string s="Hi This is       Nirmal!  ";
    string temp="",ans="";
    for(int i=0;i<s.size();i++){
        if(s[i]!=' '){
            temp+=s[i];
        }
        else if(s[i]==' ' && temp!=""){
            ans=temp+" "+ans;
            temp="";
        }
        else{
            continue;
        }
    }
    if(temp!=""){
        ans=temp+" "+ans;
    }
    //cout<<ans.substr(0,ans.size()-1)<<endl;
    cout<<ans;
}
