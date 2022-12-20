#test

board = [    
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"]
]
hiddenboard = [    
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"]
]

'''
board = {
    ["0": ]
}
'''

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(hiddenboard, ship_size, board):
    """Plaserer et skip med 'ship_size' på brettet"""
    while True:
        # Printer brettet
        print_board(board)
        # Lar brukeren velge om skipet skal være horisontalt eller vertikalt
        orientation = input("Would you like to place the ship horizontally or vertically? (h/v)")

        if orientation == "h":
            # Skipet vil være horisontalt
            # Brukeren skriver hvor skipets øvest til venstre skal være
            x = int(input("Enter the row number (0-3) for the top-left position of the ship: "))
            y = int(input("Enter the column number (0-3) for the top-left position of the ship: "))
            # Sjekker om skipet passer
            if y + ship_size > len(hiddenboard[0]):
                print("The ship does not fit on the board horizontally. Please try again.")
                continue
            # Plaserer skipet
            for i in range(ship_size):
                hiddenboard[x][y + i] = "X"
            break

        elif orientation == "v":
            # Skipet vil være vertikalt
            # Brukeren skriver hvor skipets øvest til venstre skal være
            x = int(input("Enter the row number (0-3) for the top-left position of the ship: "))
            y = int(input("Enter the column number (0-3) for the top-left position of the ship: "))
            # Sjekker om skipet passer
            if x + ship_size > len(hiddenboard):
                print("The ship does not fit on the board vertically. Please try again.")
                continue
            # Plaserer skipet
            for i in range(ship_size):
                hiddenboard[x + i][y] = "X"
            break

# Plaserer et skip med størrelse 3
place_ship(hiddenboard, 3, board)

def shoot(board, hiddenboard, x, y):
    if board[x][y] != "O":
        print("You already shot here.")
        return False
    elif hiddenboard[x][y] == "X":
        board[x][y] = "H"
        print("Hit!")
        return is_game_won(hiddenboard)
    elif hiddenboard[x][y] == "O":
        board[x][y] = "M"
        print("Miss!")
        return False


def is_game_won(hiddenboard):
    hits = 0
    for row in board:
        hits += row.count("H")
    return hits == 3


# Printer det oppdaterte brettet
print_board(board)

while not is_game_won(hiddenboard):
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    shoot(board, hiddenboard, x, y)
    print_board(board)

print("You won!")