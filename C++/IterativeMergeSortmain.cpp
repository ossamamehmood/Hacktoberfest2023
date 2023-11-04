#include <iostream>
using namespace std;

 
void merge(int arr[], int low, int mid, int high){
     int i= low;
     int j=mid+1;
     int k= low;
     int b[100];
     
     while(i<=mid && j<=high){
         if(arr[i]<arr[j]){
             b[k++]=arr[i++];
        }
         
         else{
         b[k++]=arr[j++];
        }
    }
    
    for(; i<=mid; i++){
        b[k++]=arr[i];
    }
    
    for(; j<=high; j++){
        b[k++]=arr[j];
    }
    
    for(int u=low; u<=high; u++){       
        arr[u]=b[u];
    }

 }
 
 void iMergeSort(int arr[], int n){
     int p;
     int i, l, h, mid;
     for(p=2; p<=n; p=p*2){
        for(i=0; i+p-1<n; i=i+p){
             l=i;
             h= i+p-1;
             mid=(l+h)/2;
             
             merge(arr, l, mid, h);
        }
    
    
    if(n-i>p/2) { 
 l = i; 
 h = i+p-1; 
 mid = (l+h)/2; 
 merge(arr, l, mid, n-1); 
 } 
     }
     
if((p/2) < n){
         merge(arr, 0, p/2-1, n-1);
    }
 }
 
 void printArray(int array[],int n){
    for(int i=0; i<n; i++){
        cout<<array[i]<<"\t";
    }
    cout<<endl;
}

 
int main() {
     int array[]={23,3,19,8,14,12,12,12,0,12,24,68,32,9856,69};
    int size= sizeof(array)/sizeof(array[0]);
    
    cout<<"Iterative Merge Sort:"<<endl;
    iMergeSort(array, size);
    printArray(array, size);
    
    return 0;
}
