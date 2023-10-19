#include<iostream>
using namespace std;
void counting_sort(int a[],int n){
	//first find the largest element of the array to find range
	int largest=-1;      //assume a array of positive numbers
	for(int i=0;i<n;i++){
		largest=max(largest,a[i]);
		
	}
	//create a frequency array
	int *freq=new int[largest+1]{0};    //create a frequency array and initialize it with 0;
	for(int i=0;i<n;i++){
		freq[a[i]]++;
	}
	//put the elements back into the array a[i] by reading frequency array
	int j=0;
	for(int i=0;i<=largest;i++){          //iterate over the freq array
	    while(freq[i]>0){
	    	a[j]=i;
	    	freq[i]--;
	    	j++;
	    	
		}
	
		
	}
}
int main(){
	int a[]={88,97,10,12,15,1,5,6,12,5,8};
	int n=sizeof(a)/sizeof(int);
	counting_sort(a,n);
	for(int i=0;i<n;i++){
		cout<<a[i]<<endl;
	}
	return 0;
}
