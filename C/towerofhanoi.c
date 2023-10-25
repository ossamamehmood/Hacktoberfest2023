//TOWER OF HANOI 
#include <stdio.h>
void hanoi (char first, char mid, char dest, int n){
if (n==1){ 
    printf("Move disk 1 from %c to %c ", first, dest);
    return;
}
else{
    hanoi(first, dest, mid, n-1 );
    printf("\n");
    printf("\n Move disk %d from rod %c to rod %c", n, first, dest);
    printf("\n");
    hanoi(mid, dest, first, n-1);
}
}
int main(){
    int n=3;
    hanoi('A', 'B', 'C', n);
}