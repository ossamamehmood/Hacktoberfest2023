#include<iostream>
#include<vector>
using namespace std;
string printzig(string str,int n){
    if(n==1){
        return str;
    }
    string res="";
    vector<string> arr(n, ""); //for 3 rows{"","",""}
    bool down;
    int row=0;
    for(int i=0;i<str.size();i++){
        arr[row].push_back(str[i]);
        if(row==n-1){
            down=false;
        }
        if(row==0){
            down=true;
        }
        if(down==true){
            row++;
        }
        else{
            row--;            
        }
    }
    for(int i=0;i<n;i++){
        res+=arr[i];
        cout<<arr[i]<<endl;
    }
    return res;
}
int main(){
    string str="PAYPALISHIRING";
    int n=3;
    cout<<"Zigzag string: "<<endl<<printzig(str,n);
}