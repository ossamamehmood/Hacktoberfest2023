#include <stdio.h>
float taylorSeries(int x,int n)
{
	static float power=1,fact=1;
	float res;
	if (n==0){
		return 1;
	}
	res=taylorSeries(x,n-1);
	power=power*x;
	fact=fact*n;
	return (res+power/fact);
}
int main()
{
	int x,num;
	scanf("%d%d",&x,&num);
	printf("%lf\n",taylorSeries(x,num));
	return 0;
}
