#include<iostream>
#include<vector>
#include<set>
using namespace std;

bool checkpan(string str){
    vector<bool> present(26,false);
    int index;
    char c;
    for(int i=0;i<str.length();i++){
        c=(char)tolower(str[i]);
        if('a'<=c && c<='z')
            index=c-'a';
        else
            continue;
        present[index]=true;
    }
    for(int i=0;i<25;i++){
        if(present[i]==false)
            return false;
    }
    return true;
}

int checkpangram(string str){
    set<char> sets;
    char c;
    for(int i=0;i<str.length();i++){
        c=(char)tolower(str[i]);
        if('a'<=c && c<='z')
            sets.insert(c);
        else
            continue;
    }
    return (sets.size());
}
int main(){
    string str="The quick brown fox jumps over the lazy dog";
    // if(checkpan(str)==true)
    //     cout<<"String is Panagram";
    // else
    //     cout<<"String is not Panagram";
    if(checkpangram(str)==26)
        cout<<"String is Panagram";
    else
        cout<<"String is not Panagram";
}