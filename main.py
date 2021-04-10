# This is a simple command-line Tic-Tac-Toe game

from computer import com_move

# Setup a blank board using the dictionary
board = {1: "   ", 2: "   ", 3: "   ",
         4: "   ", 5: "   ", 6: "   ",
         7: "   ", 8: "   ", 9: "   "}

# Print the current board to command line
def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("---+---+---")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("---+---+---")
    print(board[7] + '|' + board[8] + '|' + board[9])

# Allow user input
def get_user_move():
    while True:
        try:
            position = int(input())
        except ValueError:
            print("Value must be a whole number between 1 and 9")
            continue
        except:
            print("Input error. Try again")
            continue

        if not 1 <= position <= 9:
            print("Value out of range. Please select a number between 1 to 9")
            continue
        else:
            break
    return position

def winner(X_pos, O_pos):
    winning_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    for sets in winning_sets:
        if sets.issubset(X_pos):
            return "X WINS"
        if sets.issubset(O_pos):
            return "O WINS"
    return 0

def play_game():
    opponent = int(input("Select your opponent:\n1 = Another player\n2 = Computer\n"))

    print_board(board)

    # List of available board positions
    avail_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Record moves of both players in sets
    x_pos = set()
    o_pos = set()

    # Initialize player
    player = 'X'

    count = 0
    while count < 9:
        print(f'{player}\'s move: ', end="")
        if player == 'X' or (player == 'O' and opponent == 1):
            pos = get_user_move()
        else:
            pos = com_move(avail_pos, x_pos, o_pos)

        if pos not in avail_pos:
            print("Invalid move. Position already taken.")
            continue

        if player == 'X':
            board[pos] = " X "
            x_pos.add(pos)
            avail_pos.remove(pos)
            count += 1
            player = 'O'
        else:
            board[pos] = " O "
            o_pos.add(pos)
            avail_pos.remove(pos)
            count += 1
            player = "X"

        print("\n")
        print_board(board)

        if count >= 5:
            win = winner(x_pos, o_pos)
            if win != 0:
                print(win)
                break

    else:
        print("No winner")

if __name__ == "__main__":
    print("WELCOME TO TIC-TAC-TOE")

    while True:
        play_game()
        play_again = input("Play again? Y/N --- ")
        if play_again.upper() == "Y":
            print("\n")

            # Reset board
            board = {1: "   ", 2: "   ", 3: "   ",
                     4: "   ", 5: "   ", 6: "   ",
                     7: "   ", 8: "   ", 9: "   "}
            continue
        else:
            break

