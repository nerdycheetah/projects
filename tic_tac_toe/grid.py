def create_grid(grid_pos:list) -> None:
    """Takes in a list of grid positions and prints them out in the traditional tic-tac-toe format."""
    pretty_grid = f'''
      1   2   3

A     {grid_pos[0]} | {grid_pos[1]} | {grid_pos[2]}
     -----------
B     {grid_pos[3]} | {grid_pos[4]} | {grid_pos[5]}
     -----------
C     {grid_pos[6]} | {grid_pos[7]} | {grid_pos[8]}
'''
    print(pretty_grid)


def edit_grid(grid_pos:list, marker:str, move_idx:int) -> bool:
    moved = False

    if grid_pos[move_idx] == '-':
        grid_pos[move_idx] = marker
        moved = True

    return moved
