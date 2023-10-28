#include<iostream>
using namespace std;
int partition(int arr[],int low,int high)
{
int pivot=arr[high];
int i = low-1;
for(int j=low;j<high;j++)
{
if(arr[j]<pivot)
{
i++;
swap(arr[j],arr[i]);
}
}
swap(arr[i+1],arr[high]);
return i+1;
}
void quickSort(int arr[],int low,int high)
{
if(low<high)
{
int pi=partition(arr,low,high);
quickSort(arr,low,pi-1);
quickSort(arr,pi+1,high);
}
}
int main()
{
int a[]={25,10,30,15,20,28};
int n=sizeof(a)/sizeof(a[0]);
cout<<"-:Original Array:-"<<endl;
for(int i:a)
cout<<i<<" ";
cout<<endl;
quickSort(a,0,n-1);
cout<<"-:Sorted Array:-"<<endl;
for(int i:a)
cout<<i<<" ";
cout<<endl;
}
