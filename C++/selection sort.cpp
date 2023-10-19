#include<iostream>

using namespace std;
	
void selection_sort(int a[],int n){
	for(int i=0;i<n-1;i++){
		int min_idx=i;
		for(int j=i;j<=n-1;j++){
			if (a[j]<a[min_idx]){
				min_idx=j;
			}
		}
		swap(a[i],a[min_idx]);        //swap is pre defined in c++
	
	}
}
int main(){
	int n;
	cin>>n;
	int a[100];
	for(int i=0;i<=n-1;i++){
		cin>>a[i];
	}
	selection_sort(a,n);
	for(int i=0;i<=n-1;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}

