#include <stdio.h>

// Program to check whether a two-dimensional array is a Sparse Matrix

int main() {
    int rows, columns, counter = 0;
    printf("Enter the number of rows and columns of the matrix: ");
    scanf("%d %d", &rows, &columns);

    int matrix[rows][columns];

    printf("Enter the elements of the matrix (%d elements in total): \n", rows * columns);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            scanf("%d", &matrix[i][j]);
            if (matrix[i][j] == 0) {
                counter++;
            }
        }
    }

    // Printing the matrix
    printf("\nThe entered matrix is: \n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    // Checking if the matrix is sparse or not
    if (counter > (rows * columns) / 2) {
        printf("\nThe entered matrix is a sparse matrix\n");
    } else {
        printf("\nThe entered matrix is not a sparse matrix\n");
    }
    return 0;
}
