#include<iostream>
#include<map>
using namespace std;
bool isisho(string s,string s1){
    if(s.size()!=s1.size()){
        return false;
    }
    map<char,char> map1;
    map<char,char> map2;
    for(int i=0;i<s.size();i++){
        if(map1.find(s[i])==map1.end() && map2.find(s1[i])==map2.end()){
            //end() function is used to return an iterator pointing to past 
            //the last element of the map container. 
            //Since it does not refer to a valid element
            map1[s[i]]=s1[i];
            map2[s1[i]]=s[i];
        }
        else if(map1[s[i]]!=s1[i] && map2[s1[i]]!=s[i]){
            return false;
        }
    }
    return true;
}
int main()
{
    string s="xxxyyz";
    string s1="aaaccd";
    bool res=isisho(s,s1);
    if(res){
        cout<<"Isomorphic String";
    }
    else{
        cout<<"Not Isomorphic String";
    }
}
