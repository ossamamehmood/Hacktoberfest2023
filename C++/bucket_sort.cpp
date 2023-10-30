#include<iostream>
#include<algorithm>
using namespace std;
void print(int arr[],int n){
    for(int i=0;i<n;i++){
    cout<<arr[i]<<" ";
    }
}
int getmax(int arr[],int n){
    int M=arr[0];
    for(int i=1;i<n;i++){
        if(arr[i]>M){
            M=arr[i];
        }
    }
    return M;
}
void bucket_sort(int arr[],int n){
    int M=getmax(arr,n);
    int bucket[M];
    for(int i=0;i<=M;i++){
        bucket[i]={0};
    }
    for(int i=0;i<n;i++){
        bucket[arr[i]]++;
    }
    for(int i=0,j=0;i<=M;i++){
        while(bucket[i]>0){
            arr[j++]=i;
            bucket[i]--;
        }
    }
}
int main()
{
    int arr[10]={0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68};
    bucket_sort(arr,10);
  print(arr,10);
 return 0 ;
}