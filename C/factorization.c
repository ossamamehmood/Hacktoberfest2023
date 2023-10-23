// This program to find the factorization of a number
#include<stdio.h>

int main(){
    int i, j, num, sum, *arr, x = 0, div;
    
    printf("Please enter a number for factorial :");
    scanf("%d", &num);
    div = num;
    
    for(i = 2; i<num; i++){
        sum = 0; 
        for(j = 2; j <= i/2; j++){
            if(i%j == 0) sum++;
        }
        if(div == 1) break;
        while(sum == 0 && div%i == 0 && div != 1){
            printf("%d x ", i);
            arr[x] = i;
            x++;
            div = div/i;
        }
    }
    printf("\b\b= %d", num);
    
    printf("\nThe  Prime number by which %d is divisible those are : %d", num, arr[0]);
    for(i = 1; i < x ; i++) if(arr[i] != arr[i-1]) printf(", %d", arr[i]);
    
    getchar();
    return 0;
}
