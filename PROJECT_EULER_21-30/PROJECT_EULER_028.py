"""tarting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import numpy as np

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction

def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # center
    dx, dy = NORTH # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visited
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go




matrix = np.array(spiral(1001,1001)) #get spiral matrix as numpy object
left_diagonal = matrix.diagonal()  #get left diagonal
matrix = np.fliplr(matrix) #flip matrix
right_diagonal = matrix.diagonal() #get right diagonal

suma = 0
for i in range(len(left_diagonal)): #diagonal sum calculation
    suma+=left_diagonal[i] + right_diagonal[i]

print(suma - 1)#sum -1 --> we calculate center 2x
