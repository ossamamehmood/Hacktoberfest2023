#include <iostream>
using namespace std;
int main(){
    int l=0,r;
    string name="hi this is nirmal";
    r=name.length()-1;
    while(l<r){
        swap(name[l],name[r]);
        l++;
        r--;
    }
    cout<<name;
}