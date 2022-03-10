# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle_067.txt 
#  a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. 
# It is not possible to try every route to solve this problem, 
# as there are 299 altogether! If you could check one trillion (1012) routes every second
#  it would take over twenty billion years to check them all.
#  There is an efficient algorithm to solve it.)
my_triangle = open("triangle_067.txt")
triangle_matrix = []
#load matrix
for line in my_triangle:
    triangle_matrix.append(list(map(int,line.split(" "))))

#solution using dynamic programming
for i in reversed(range(len(triangle_matrix) - 1)):#go from last row
    for j in range(i+1): 
        #find max of two adjancent numbers below
        triangle_matrix[i][j]+=max(triangle_matrix[i+1][j], triangle_matrix[i+1][j+1])
print(triangle_matrix[0][0])
