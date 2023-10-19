#include<iostream>
using namespace std;
#define ll long long
void merge(ll int a[],int s,ll int e){
	ll int mid=(s+e)/2;
	ll int i=s;
	ll int j=mid+1;
	ll int k=s;
	ll int temp[e+1];
	while(i<=mid && j<=e){
		
	
	    if(a[i]<a[j]){
		    temp[k++]=a[i++];
	    }
	    else{
		    temp[k++]=a[j++];
	    }
	}
	while(i<=mid){
		temp[k++]=a[i++];
	}
	while(j<=e){
		temp[k++]=a[j++];
	}
	
	for(ll int i=s;i<=e;i++){
		a[i]=temp[i];
	}
}
void merge_sort(ll int a[],int s,ll int e){
	
	if(s>=e){
		return;
	}
	//follow 3 steps
	//1. divide
	ll int mid=(s+e)/2;
	//2. recursively sort two arrays - s,mid and mid+1,e
	merge_sort(a,s,mid);
	merge_sort(a,mid+1,e);
	//3. merge the two parts
	merge(a,s,e);
	
	
}
int main(){
	ll int n;
	cin>>n;
	ll int a[n];
	for(ll int i=0;i<n;i++){
		cin>>a[i];
	}
	merge_sort(a,0,n-1);
	for(ll int i=0;i<n;i++){
		cout<<a[i]<<" ";
	}
	return 0;
}
