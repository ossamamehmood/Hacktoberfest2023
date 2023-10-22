import random

# Initialize the game grid
grid = [["_","_","_"],["_","_","_"],["_","_","_"]]

# Keep track of used positions
bid = []

# Initialize a turn counter
trace = 0

def god(a, b):
    if (trace == 0):
        q = random.randint(0, 2)
        w = random.randint(0, 2)
        return [q, w]
    
    # Define strategies for computer's moves based on player's position
    strategies = {
        (0, 0): [[0, 1], [0, 2], [1, 0], [2, 0], [1, 1], [2, 2]],
        (0, 1): [[0, 0], [0, 2], [1, 1], [2, 1]],
        (0, 2): [[0, 1], [0, 0], [1, 2], [2, 2], [2, 0], [1, 1]],
        (1, 0): [[0, 0], [2, 0], [1, 1], [1, 2]],
        (1, 1): [[0, 1], [0, 0], [0, 2], [1, 0], [1, 2], [2, 2], [2, 0], [2, 1]],
        (1, 2): [[0, 2], [2, 2], [1, 1], [1, 0]],
        (2, 0): [[0, 0], [0, 1], [2, 1], [2, 2], [1, 1], [0, 2]],
        (2, 1): [[1, 1], [2, 0], [2, 2], [0, 1]],
        (2, 2): [[0, 1], [1, 1], [2, 1], [2, 0], [0, 2], [1, 2]]
    }

    return random.choice(strategies[(a, b)])

while True:
    # Display the game grid
    for i in range(0, 3):
        for j in range(0, 3):
            print(grid[i][j], end="  ")
        print("\n")

    # Check for a win or a draw
    if ((grid[0][0] == grid[1][1] == grid[2][2] == "#") or
        (grid[0][2] == grid[1][1] == grid[2][0] == "#")):
        print("You won!")
        break
    elif ((grid[0][0] == grid[1][1] == grid[2][2] == "O") or
          (grid[0][2] == grid[1][1] == grid[2][0] == "O")):
        print("Computer won!")
        break
    for i in range(3):
        if ((grid[i][0] == grid[i][1] == grid[i][2] == "#") or
            (grid[0][i] == grid[1][i] == grid[2][i] == "#")):
            print("You won!")
            break
        elif ((grid[i][0] == grid[i][1] == grid[i][2] == "O") or
              (grid[0][i] == grid[1][i] == grid[2][i] == "O")):
            print("Computer won!")
            break

    if len(bid) == 9:
        for i in range(0, 3):
            for j in range(0, 3):
                print(grid[i][j], end="  ")
            print("\n")
        if ((grid[0][0] == grid[1][1] == grid[2][2] == "#") or
            (grid[0][2] == grid[1][1] == grid[2][0] == "#")):
            print("You won!")
        elif ((grid[0][0] == grid[1][1] == grid[2][2] == "O") or
              (grid[0][2] == grid[1][1] == grid[2][0] == "O")):
            print("Computer won!")
        elif ((grid[0][0] == grid[0][1] == grid[0][2] == "#") or
              (grid[1][2] == grid[1][1] == grid[1][0] == "#") or
              (grid[2][2] == grid[2][1] == grid[2][0] == "#")):
            print("You won!")
        elif ((grid[0][0] == grid[0][1] == grid[0][2] == "O") or
              (grid[1][2] == grid[1][1] == grid[1][0] == "O") or
              (grid[2][2] == grid[2][1] == grid[2][0] == "O")):
            print("Computer won!")
        elif ((grid[0][0] == grid[1][0] == grid[2][0] == "#") or
              (grid[0][1] == grid[1][1] == grid[2][1] == "#") or
              (grid[2][2] == grid[1][2] == grid[0][2] == "#")):
            print("You won!")
        elif ((grid[0][0] == grid[1][0] == grid[2][0] == "O") or
              (grid[0][1] == grid[1][1] == grid[2][1] == "O") or
              (grid[2][2] == grid[1][2] == grid[0][2] == "O")):
            print("Computer won!")
        break

    print("Enter row and column from 1 to 3.")
    print("Enter the location of your move (your symbol is '#').")
    x = int(input("Enter the row position: "))
    y = int(input("Enter the column position: "))
    
    # Check if the position is already used
    if [x-1, y-1] in bid:
        print("Value already used...")
        continue

    # Place the player's move on the grid
    grid[x-1][y-1] = "#"
    bid.append([x-1, y-1])

    # Computer's turn
    while True:
        computer = god(x-1, y-1)
        l = computer[0]
        m = computer[1]
        if [l, m] in bid:
            print("Thinking...")
        else:
            grid[l][m] = "O"
            bid.append([l, m])
            break

    
