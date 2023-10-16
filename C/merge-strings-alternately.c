#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 

char* mergeAlternately(char* word1, char* word2) {
	short length1 = strlen(word1); 
	short length2 = strlen(word2); 
	char* a = (char*)malloc(sizeof(char) * (length1 + length2 + 1)); 

	short i, j, k; 
	for(i = 0, j = 0, k = 0; i < length1 || j < length2; i++, j++) {
		if (i < length1) 
			a[k++] = word1[i]; 
		if (j < length2) 
			a[k++] = word2[j]; 
	}
	a[k] = '\0'; 

	return a; 
}

int main(int argc, char **argv) {
	if (argc != 3) {
		printf("usage: %s '<str1>' '<str2>'\n", argv[0]); 
	}

	char* word1 = argv[1]; 
	char* word2 = argv[2]; 

	char* merge = mergeAlternately(word1, word2); 
	printf("%s\n", merge); 
	return 0; 
}
