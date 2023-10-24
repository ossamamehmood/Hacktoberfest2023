#include<stdio.h>

int main(){
    int i, i2, i1, j, sum;
    printf("Please enter the range in which you wnat to see the prime number: ");
    scanf("%d, %d",&i2, &i1);

    if(i1 < i2){
        int x;
        x = i2;
        i2 = i1;
        i1 =x;
    }

    printf("All the prime numbers in the given range are as follows :");
    for(i = i2; i < i1; i++){
        sum = 0;
        for(j = 1; j <= i/2; j++){
            if(i%j == 0) sum ++;
        }
        if(sum == 1) printf("%d, ", i);
    }
    return 0 ; 
}

