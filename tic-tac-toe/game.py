"""
 Tic Tac Toe Game
 First Player get X And other get O
"""

from IPython.display import clear_output

def find_symbol(index=0):
    """
     Convert Symbol to a Character
    """
    if index not in [0, 1, 2]:
        index = 3
    return [' ', 'X', 'O', '?'][index]

def print_line(arr):
    """
     Print Game Line
    """
    print(' {} | {} | {} '.format(find_symbol(arr[0]), find_symbol(arr[1]), find_symbol(arr[2])))


def print_dash():
    """
     Print dash Line
    """
    print('-'*(11))


def print_board(arr):
    """
     Print Game Board
    """
    if len(arr) < 9:
        print(f"Board is invalid. Array {arr} size is {len(arr)} but should be 9")
        return
    print('\nCurrent:\n')
    print_line(arr[6:])
    print_dash()
    print_line(arr[3:6])
    print_dash()
    print_line(arr[:3])

def take_input(player):
    """
      Take user input
    """
    valid_input = False
    while not valid_input:
        i = input(f"\nPlayer{player} Select Cell? ")
        valid_input = i.isnumeric() and int(i) in range(1, 10)
        if not valid_input:
            print(f"Input {i} is not valid. Please select number between {range(1,10)}")
        else:
            return int(i)

def is_same(first, second, third):
    """
     Check all first, third, and third are equals
    """
    return first if first == second and second == third else 0


def find_winner(game):
    """
     Find Winner
    """
    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9)
                            , (1, 5, 9), (3, 5, 7)
                            , (1, 4, 7), (2, 5, 8), (3, 6, 9)]
    winner = [game[a-1] for a, b, c
              in winning_combinations if is_same(game[a-1], game[b-1], game[c-1])]
    return winner[0] if len(winner) is not 0 else 0



def start_game():
    """
      Starts a new Game
    """
    game_on = True
    print('\nWelcome to Tic-Tac-Toe\n')
    game = [0]*9
    player = 0
    while game_on:
        print_board(game)
        i = take_input(player + 1) - 1
        if game[i] is not 0:
            print(f"Cell {i} is Aready Selected")
            continue
        game[i] = player + 1

        player += 1
        player %= 2
        game_on = len(list(filter(lambda a: a == 0, game))) is not 0
        winner = find_winner(game)

        clear_output()

        if winner is not 0:
            print("-"*10)
            print(f"Player{winner} Won The Game!!!")
            print_board(game)

            break

    else:
        print("No Winner :( ")
        print_board(game)
    print("\n{:*^20}\n".format("The End"))


if __name__ == "__main__":
    start_game()
