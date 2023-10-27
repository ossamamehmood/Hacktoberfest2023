#include <iostream>
#include <vector>

/*<----- function to print the Tic-Tac-Toe board ----->*/
void printBoard(const std::vector<std::vector<char>>& board) {
    std::cout << "\n\n " << board[0][0] << " | " << board[0][1] << " | " << board[0][2] << std::endl;
    std::cout << "-----------\n";
    std::cout << " " << board[1][0] << " | " << board[1][1] << " | " << board[1][2] << std::endl;
    std::cout << "-----------\n";
    std::cout << " " << board[2][0] << " | " << board[2][1] << " | " << board[2][2] << std::endl;
}

/*<----- function to check if the game has been won ----->*/
bool checkWin(const std::vector<std::vector<char>>& board, char player) {
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
            return true; // row win
        }
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player) {
            return true; // column win
        }
    }
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player) {
        return true; // diagonal win (top-left to bottom-right)
    }
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player) {
        return true; // diagonal win (top-right to bottom-left)
    }
    return false;
}

/*<----- function to check if the game is a draw ----->*/
bool checkDraw(const std::vector<std::vector<char>>& board) {
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i][j] == ' ') {
                return false; // there are still empty cells
            }
        }
    }
    return true; // all cells are filled
}

int main() {
    std::vector<std::vector<char>> board(3, std::vector<char>(3, ' '));
    char currentPlayer = 'X';

    std::cout << "Welcome to Tic-Tac-Toe!" << std::endl;

    while (true) {
        // print the current board with the improved appearance
        printBoard(board);

        int row, col;
        std::cout << "\n\nPlayer " << currentPlayer << ", enter your move (row [space] column): ";
        std::cin >> row >> col;

        // check if the input is valid
        if (row < 1 || row > 3 || col < 1 || col > 3 || board[row - 1][col - 1] != ' ') {
            std::cout << "\n\nInvalid move. Try again." << std::endl;
            continue;
        }

        // update the board
        board[row - 1][col - 1] = currentPlayer;

        // check if the current player has won
        if (checkWin(board, currentPlayer)) {
            printBoard(board);
            std::cout << "\n\nPlayer " << currentPlayer << " wins! Congratulations!" << std::endl;
            break;
        }

        // check if the game is a draw
        if (checkDraw(board)) {
            printBoard(board);
            std::cout << "\n\nIt's a draw! The game is over." << std::endl;
            break;
        }

        // switch to the next player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
