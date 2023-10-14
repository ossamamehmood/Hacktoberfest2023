"""The N-Queens problem is a classic combinatorial puzzle that 
involves placing N chess queens on an N×N chessboard so that 
no two queens threaten each other. This algorithm will find and 
print all possible solutions for the N-Queens problem."""

def is_safe(board, row, col, n):
    # Check the left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        solution = [''.join(['Q' if cell == 1 else '.' for cell in row]) for row in board]
        solutions.append(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = 0

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

def print_solutions(solutions):
    for idx, solution in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    n = 8  # Change the value of 'n' to solve for different board sizes
    solutions = solve_n_queens(n)
    print_solutions(solutions)
