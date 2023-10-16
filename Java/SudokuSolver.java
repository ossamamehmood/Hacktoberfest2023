import java.util.Scanner;
public class SudokuSolver {
	public static void display(int[][] sudoku) {
		for(int i=0;i<sudoku.length;i++) {
			for(int j=0;j<sudoku[0].length;j++) {
				System.out.print(sudoku[i][j]+" ");
			}
	System.out.println();	
	}
}
	public static void solution(int[][] sudoku, int i,int j) {
		if(i==sudoku.length) {
			display(sudoku);
			return;
		}
	
		int nr=0;
		int nc=0;
		if(j == sudoku.length-1) {
	           nr = i + 1;
	           nc = 0;
	       } 
		else {
	           nr = i;
	           nc = j + 1;
	       }

	       if(sudoku[i][j] != 0) {
	           solution(sudoku,nr,nc);
	           }
	       else {
	          for(int k=1; k<=9; k++) {
	               if(allowed(sudoku, i, j, k)) {
	            	   sudoku[i][j] = k;
	                   solution(sudoku, nr, nc);
	                   sudoku[i][j] = 0;
	               }    
	                   
	               }
	           }
	}
	     public static boolean allowed(int[][] sudoku,int r,int c,int number) {
	    	 for(int i=0;i<sudoku[0].length;i++) {
	   			if (sudoku[i][c]==number) {
	   				return false;
	   			}
	    	 }
	   			for(int i=0;i<sudoku[0].length;i++) {
	   			if (sudoku[r][i]==number) {
	   				return false;
	   			}
	   			}
	   		int smr= 3*(r/3);
	   		int smc= 3*(c/3);
	   		for(int i=smr;i<smr+3;i++) {
	   			for(int j=smc;j<smc+3;j++) {
	   				if(sudoku[i][j]==number) {
	   					return false;
	   				}
	   			}
	   		}
	   		return true;
	   	}       
	                     
	public static void main(String[] args) throws Exception {
	Scanner sc=new Scanner(System.in);
		int [][] arr=new int[9][9];
		System.out.println("Sample format: \r\n"
				+ "3 0 6 5 0 8 4 0 0  			 \r\n"
				+ "5 2 0 0 0 0 0 0 0 \r\n"
				+ "0 8 7 0 0 0 0 3 1\r\n"
				+ "0 0 3 0 1 0 0 8 0\r\n"
				+ "9 0 0 8 6 3 0 0 5\r\n"
				+ "0 5 0 0 9 0 6 0 0 \r\n"
				+ "1 3 0 0 0 0 2 5 0 \r\n"
				+ "0 0 0 0 0 0 0 7 4 \r\n"
				+ "0 0 5 2 0 6 3 0 0\r\n"
				+ "");
		System.out.println("Enter your sudoku");
		for(int i=0;i<9;i++) {
			for(int j=0;j<9;j++) {
				arr[i][j]=sc.nextInt();
			}
	}
		System.out.println("Voila!Here's the solution:");
solution(arr,0,0);
	}
} 