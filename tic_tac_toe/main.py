# Import modules
import helpers
import grid

# Empty grid
grid_pos = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-',
]

grid_map = {
    'A1':0, 'A2':1, 'A3':2,
    'B1':3, 'B2':4, 'B3':5,
    'C1':6, 'C2':7, 'C3':8,
}


# grid_pos_win = [
#     '0', '0', 'x',
#     '-', '0', 'x',
#     '-', '-', 'x',
# ]




# Welcome Function, assigns two players
player_1_name, player_2_name = helpers.welcome_player()
player_1_marker, player_2_marker = 'X', 'O'

grid.create_grid(grid_pos)

helpers.how_to_play(player_1_name, player_2_name)
# Main Game

count = 0
foundWinner = False
while count < 9 and not foundWinner:
    # ask user1 input

    user1Input = helpers.get_user_input(player_1_name,player_1_marker)
    # mark grid
    grid.edit_grid(grid_pos, player_1_marker, grid_map[user1Input])
    grid.create_grid(grid_pos)
    # increment count

    count += 1
    if (count >= 5):
        res = helpers.find_win_combo(grid_pos)
        if len(res):
            print(helpers.get_winner_name(player_1_marker, player_2_marker, player_1_name, player_2_name, res))
            foundWinner = True
            break

    # ask user 2 input
    if (count == 9):
        print('Its a tie!')
        break
    user2Input = helpers.get_user_input(player_2_name, player_2_marker)
    # mark grid
    grid.edit_grid(grid_pos, player_2_marker, grid_map[user2Input])
    grid.create_grid(grid_pos)
    # increment count
    count += 1
    if (count >= 5):
        res = helpers.find_win_combo(grid_pos)
        if len(res):
            print(helpers.get_winner_name(player_1_marker, player_2_marker, player_1_name, player_2_name, res))
            foundWinner = True
            break



# Test Run
# grid.create_grid(grid_pos)
#
# print('Player 1 Move: ')
# move = input('Enter a Move: ').upper()
#
# mapped_move = grid_map[move]
#
# grid.edit_grid(grid_pos, 'X', mapped_move)
#
# grid.create_grid(grid_pos)



# 9/5/2020 HW
'''
The next part of our game is the hardest part, this is when the player interactions begin, and actual gameplay start.

Thinking about the logical flow of the game, it makes sense that it goes p1 -> p2 -> ... so on and so forth.

To me, this sounds like it calls for a WHILE loop, in which the game should NOT end and keep looping until someone wins, or the board is filled up.

We dont want to hard code each turn by turn, think about the while loop for this, and think about which parts of the player turn process we can repeat.

Kind of like... a player makes a move, we take in their move, then check if it was a valid move, and if it is, we commit their move to the board. If it is NOT valid, then we have them keep trying until they enter a valid spot.
'''
