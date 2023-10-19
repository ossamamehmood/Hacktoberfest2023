#include<iostream>
using namespace std;
int partition(int a[],int s,int e){
	
	int i=s-1;
	int j=s;
	int pivot=a[e];
	for( ;j<=e-1;){
		if(a[j]<=pivot){
			
			i=i+1;
			swap(a[i],a[j]);
			
		}
		j=j+1;
	}
	
	swap(a[i+1],a[e]);
	return i+1;
	
}
void quick_sort(int a[],int s,int e){
	//base case
	if(s>=e){
		return;
	}
	//recursive case
	int p=partition(a,s,e);
	//left part
	quick_sort(a,s,p-1);
	//right part
	quick_sort(a,p+1,e);
}
int main(){
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	quick_sort(a,0,n-1);
	for(int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}
