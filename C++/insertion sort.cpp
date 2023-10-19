#include<iostream>
using namespace std;
void insertion_sort(int arr[],int n){
	for(int i=1;i<=n-1;i++){
		int e=arr[i];
		//place the current element at 'right' position in the sorted part.
		int j=i-1;
		while(j>=0 and arr[j]>e){
			arr[j+1]=arr[j];
			j=j-1;
		}
		arr[j+1]=e;
	}
}
int main(){
	int n;
	cin>>n;
	int arr[100];
	for(int i=0;i<=n-1;i++){
		cin>>arr[i];
	}
	insertion_sort(arr,n);
	for(int i=0;i<=n-1;i++){
		cout<<arr[i]<<endl;
	}
	return 0;
}
