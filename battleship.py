from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print "".join(row)

def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(5):
    print "Potez", turn + 1
    guess_row = int(raw_input("Pogodite red: "))
    guess_col = int(raw_input("Pogodite kolonu: "))
    if guess_row == ship_row and guess_col == ship_col:
        print "Cestitamo! Pogodili ste brod."
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print "To mesto se ne nalazi u okeanu."
        elif board[guess_row][guess_col] == "X":
            print "Vec ste upotrebili to mesto."
        else:
            print "Promasili ste moj brod."
            board[guess_row][guess_col] = "X"
        if (turn == 4):
            print "Igra je zavrsena!"
        print_board(board)
            
