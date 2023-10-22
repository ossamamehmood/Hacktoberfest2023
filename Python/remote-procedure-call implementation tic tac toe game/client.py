import Pyro4

def connect_to_server(uri):
    return Pyro4.Proxy(uri)

if __name__ == "__main__":
    uri = input("Enter the server URI: ")
    game = connect_to_server(uri)

    while True:
        print("Current Board:")
        board = game.get_board()
        for i in range(0, 9, 3):
            print(board[i], board[i + 1], board[i + 2])
        print(f"Current Player: X")  # Player X's turn

        position = int(input("Enter a position (0-8): "))

        if game.make_move(position):
            winner = game.check_winner()
            if winner:
                print(f"Player {winner} wins!")
                break
            if game.is_full():
                print("It's a draw!")
                break
        else:
            print("Invalid move. Try again.")
