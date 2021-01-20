# Welcome Function
def welcome_player() -> list:
    """Welcomes player to  Tic Tac Toe game, returns player's name"""

    welcome_message = '''
Welcome to Tic Tac Toe!
'''
    players = []
    for pos in '12':
        player = input(f'Player {pos}, enter your name! ')
        players.append(player)


    print(f'{players[0]} and {players[1]}, good luck and have fun! ')

    return players


def how_to_play(player_1_name:str, player_2_name:str) -> None:
    """Explains how to play."""
    print(f'''
Player 1 always starts first, and is automatically assigned to X.
Player 2 goes next, and is assigned to O.

Player 1 -> {player_1_name}: X
Player 2 -> {player_2_name}: O

This is your grid:

    1   2   3

A   - | - | -
   -----------
B   - | - | -
   -----------
C   - | - | -

To place your marker at a certain spot, please reference the row number, then choose a column.

For example, a move to A1 would be represented like this:

    1   2   3

A   X | - | -
   -----------
B   - | - | -
   -----------
C   - | - | -


    ''')

def find_win_combo(grid_pos:list) -> str:

    if grid_pos[0] != '-' and (grid_pos[0] == grid_pos[1] == grid_pos[2]):
        return grid_pos[0]

#########################################

    elif grid_pos[3] != '-' and grid_pos[3] == grid_pos[4] == grid_pos[5]:
        return grid_pos[3]

########################################
    elif grid_pos[6] != '-' and grid_pos[6] == grid_pos[7] == grid_pos[8]:
        return grid_pos[6]

#########################################

    elif grid_pos[0] != '-' and grid_pos[0] == grid_pos[3] == grid_pos[6]:
        return grid_pos[0]

########################################

    elif grid_pos[1] != '-' and grid_pos[1] == grid_pos[4] == grid_pos[7]:
        return grid_pos[1]

#########################################

    elif grid_pos[2] != '-' and grid_pos[2] == grid_pos[5] == grid_pos[8]:
        return grid_pos[2]

#########################################

    elif grid_pos[6] != '-' and grid_pos[6] == grid_pos[4] == grid_pos[2]:
        return grid_pos[6]

#########################################
    elif grid_pos[0] != '-' and grid_pos[0] == grid_pos[4] == grid_pos[8]:
        return grid_pos[0]

#########################################

    else:
        return ''

def get_user_input(player_name:str,player_marker:str) -> str:
    return input(f"{player_name} ").upper()

def get_winner_name(player_1_marker:str, player_2_marker:str, player_1_name:str, player_2_name:str, res:str) -> str:
    if res == player_1_marker:
        return f'{player_1_name}, you win!'
    else:
        return f'{player_2_name}, you win!'
