#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int binary_search(int arr[],int n,int key){
    int start = 0;
    int end = n-1;
    
    while(start<=end){
        int mid = start + ((end - start)/2);
        if(arr[mid] == key){
            return mid;
        }
        if(key > arr[mid]){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        } 
        
        
    }
    return -1;
}
// void printarray(int arr[],int n){
//     for (int i=0;i<n;i++){
//         cout<<arr[i];
//     }
// }
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int key;
    cout<<"enter the element : ";
    cin>>key;
    int index = binary_search(arr,n,key);
    cout<<"element found in index = "<<index;

}