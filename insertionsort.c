//code for insertion sort
#include<stdio.h>
#define max 50
int main()
{
	int arr[max],i,j,k,n;
	// input the number of elements in the array 
	printf("enter the number of elements\n");
	scanf("%d",&n);

	// input the values 
	for(i=0;i<n;i++)
	{
		printf("enter the element number %d\n ",i+1);
		scanf("%d",&arr[i]);
	}

	//insertion sort
	for(i=0;i<n;i++)
	{
		for(j=0;j<=i;j++)
		{
			if(arr[i]<arr[j])
			{
			k=arr[j];
			arr[j]=arr[i];
			arr[i]=k;
	  		}
		}
	}
	''
	//displaying the sorted array
	for(i=0;i<n;i++)
	printf("%d\t",arr[i]);		
}
