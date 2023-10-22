import Pyro4

@Pyro4.expose
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
        return None

    def is_full(self):
        return ' ' not in self.board

    def get_board(self):
        return self.board

    def get_current_player(self):
        return self.current_player

if __name__ == "__main__":
    with Pyro4.Daemon() as daemon:
        uri = daemon.register(TicTacToe)
        print("Server URI:", uri)
        daemon.requestLoop()
