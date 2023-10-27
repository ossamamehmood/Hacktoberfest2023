public class NumberOfIslands  
{  
//function that find the number of islands       
public int findIslands(char[][] matrix)   
{  
//finds and stores the length of the matrix or grid      
int h = matrix.length;  
if (h == 0)  
//if matrix has no elements, returns 0  
return 0;  
int l = matrix[0].length;  
//variable to store result  
int result = 0;  
//loop iterates over rows  
for (int i = 0; i < h; i++)   
{  
//loop iterates over columns      
for (int j = 0; j < l; j++)   
{  
//  
if (matrix[i][j] == '1')   
{  
//if the above condition returns true, calls the dfs() function and increments the result  
dfs(matrix, i,  j);  
result++;  
}  
}  
}  
return result;  
}  
//function performs the depth first search over the matrix  
public void dfs(char[][] matrix, int row, int col)   
{  
int H = matrix.length;  
int L = matrix[0].length;  
//returns true if any of the condition returns true  
if (row < 0 || col < 0 || row >= H || col >= L || matrix[row][col] != '1')  
return;  
//marking element as visited  
matrix[row][col] = '0';   
//moves in right direction  
dfs(matrix, row+ 1, col);   
//moves in left direction  
dfs(matrix, row- 1, col);   
//moves in downward direction  
dfs(matrix, row, col + 1);   
//moves in upward direction  
dfs(matrix, row, col - 1);   
}  
//driver code  
public static void main(String args[])   
{  
//creating an instance of teh class      
NumberOfIslands noi = new NumberOfIslands();  
//grid in which we have to find number of islands  
char[][] islandGrid = new char[][]   
{  
                {'1', '1', '0', '0', '0'},  
                {'1', '1', '0', '0', '0'},  
                {'0', '0', '1', '0', '0'},  
                {'0', '0', '0', '1', '1'}};  
//prints the result  
System.out.println("Number of Islands: " + noi.findIslands(islandGrid));  
}  
}  
