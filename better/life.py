
"""   life.py by David Lang

'life.py' is a basic representation of John Conway's Game of Life using Python's built in functions
and a basic terminal print out.

last update = 19-06-10
"""

"""
John Conway's Game of Life rules:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import random
import time

#####   CONSTANTS   #####
W, H = 12, 8         # Dimensions of grid.
D, A = '-', 'X'     # String representations of dead ('D') or alive ('A') cells.
STARTERS = 20        # Number of alive cells in first display iteration.
UPDATES = 20        # Number of how many display iterations are performed.



# List of coordinates of alive cells in first iteration.
assignments = [ [random.randint(0, H - 1), random.randint(0, W - 1)] for each in range(STARTERS) ]

# Create 'grid' based on constants 'W' and 'H'.  Set all cells within 'grid' to dead.
grid = []
for y in range(H):
    row = [ D for x in range(W) ]
    grid.append(row)

# Set alive cells from 'assignments' into 'grid'.
for each in assignments:  grid[each[0]][each[1]] = A



def getNeighbors(x, y):
    """
    input:  y = Integer representing which 'row' of 'grid' cell to be tested is.
            x = Integer representing which 'item' of 'grid' cell to be tested is.
    output: Return integer representing how many "neighbors" of argued cell are alive.
    """
    # Dictionary of coordinate vectors used to test for neighbors.
    checks =   {'TL': [-1, -1], 'TM': [ 0, -1], 'TR': [+1, -1],
                'ML': [-1,  0],                 'MR': [+1,  0],
                'BL': [-1, +1], 'BM': [ 0, +1], 'BR': [+1, +1]}

    # System check for "grid edges".  With no system check, script would IndexError.
    remove_L, remove_R, remove_T, remove_B = [], [], [], []
    if x == 0:      remove_L = ['TL', 'ML', 'BL']   # Check if coordinate is on left edge.
    if x == W - 1:  remove_R = ['TR', 'MR', 'BR']   # Check if coordinate is on right edge.
    if y == 0:      remove_T = ['TL', 'TM', 'TR']   # Check if coordinate is on top edge.
    if y == H - 1:  remove_B = ['BL', 'BM', 'BR']   # Check if coordinate is on bottom edge.
    remove = remove_L + remove_R + remove_T + remove_B  # Concatanate remove lists.
    # Remove all designated keys based on if coordinates are on an "edge".
    for r in remove:
        try:  del checks[r]
        except KeyError:  continue

    # Neighbor check...  After removing keys from "edge check", test each remaining 'checks' vector
    # from 'grid' for if that cell is alive or dead.  If alive, 'neighbors += 1'.
    neighbors = 0
    for check in dict.values(checks):
        # print(grid[x + check[0]][y + check[1]])
        if grid[y + check[1]][x + check[0]] == A:  neighbors += 1

    return neighbors



def update():
    """
    "Renders" 'grid'.  Goes through each cell in grid, checks how many adjacent alive cells
    (neighbors) there are, and based on number of neighbors, make that cell alive or dead.
    """
    # Because you're not supposed to mutate an array while looping through it, script makes a list
    # of cells to be updated to.
    update_to = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):

            # Get number of neighbors for current cell, designated whether current cell will be made
            # alive or dead based on current state and number of neighbors.  Then append current
            # cell coordinates and new state to 'update_to'.
            neighbors = getNeighbors(x, y)
            if   cell == D and neighbors == 3:                      update_to.append([y, x, A])
            elif cell == A and neighbors <= 1:                      update_to.append([y, x, D])
            elif cell == A and (neighbors == 2 or neighbors == 3):  update_to.append([y, x, A])
            elif cell == A and neighbors >= 4:                      update_to.append([y, x, D])
            else:                                                   update_to.append([y, x, cell])

    # Update 'grid' with new 'update_to' list.
    for each in update_to:  grid[each[0]][each[1]] = each[2]



def display(iter):
    """
    input:  iter = Integer representing which iteration this output is.
    output: Basic print to terminal.
    """
    for index, line in enumerate(grid):
        output = ''.join(line).replace('', ' ')     # Get 'grid' row printout.
        if index != 0:  print(output)
        else:  print(output, "iteration =", iter)   # If first row, add "iteration #" note.



# Simple function calls with iteration timer.
for each in range(UPDATES):
    print("~" * W * 2)
    display(each)
    update(), time.sleep(1)
