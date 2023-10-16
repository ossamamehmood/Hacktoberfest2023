#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFF 25

int main(int argc, char *argv[]){
    FILE *arq;
    arq = fopen(argv[1], "r");

    char senha[BUFF + 50];
    char salt[BUFF];
    char comp[BUFF + 75];
    char *result;

    printf("hash complete\n");
    scanf("%s", comp);

    printf("salt digit\n");
    scanf("%s", salt);

    int f = 0;

    while (fscanf(arq, "%s", &senha) != EOF){
        result = (char *) crypt(senha, salt);
                if (strcmp(comp, result)==0){
                    printf("senha found: %s \n", senha);
                    int f = 1;
                    return(0);
                } else {
                    printf("Testing %s \n", senha);
                }

    }
    {
        /* code */
        if (f==0){
            printf("senha not found\n");
        }
    }
    
}