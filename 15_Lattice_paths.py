"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""



gridsize = 40
paths = 1

#we can use Binomial Coefficient --> (n k)T
# --> paths == (n*(n-1)*(n-2) * .... (n-k+1)) / k(k-1)(k-2)...1

#this program calculate all routes
for i in range(gridsize):
    paths *=(2*gridsize) - i    #n
    paths /= i + 1              #k

print(paths)