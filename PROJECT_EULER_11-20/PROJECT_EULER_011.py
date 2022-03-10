#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?#


#works only on square matrix
def get_diagonals(grid, direction = True): #get list of diagonals, if direction == True --> left to right diag, else right to left diagonals
    dim = len(grid)
    assert dim == len(grid[0])
    return_grid = [[] for total in range(2 * len(grid) - 1)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if direction: 
                return_grid[row + col].append(grid[col][row])
            else:    
                return_grid[col - row + (dim - 1)].append(grid[row][col])
    return return_grid

def solve_diag(diagonals,big_sum): #finds sum of 4 adjacent digits in diagonals and if sum > big_sum it overwrites big_sum
    suma = 1
    for i in range(len(diagonals)):
        for j in range(len(diagonals[i])):
            
            if j+3 >= len(diagonals[i]): #list is out of range
                break
            else:
                for n in range(4): #4 adjancent numbers
                    suma*=diagonals[i][j+n]
                if suma > big_sum:
                    big_sum = suma
                suma = 1
    return big_sum              

def solve_rows(matrix,big_sum):#finds sum of 4 adjacent in rows digits and if sum > big_sum it overwrites big_sum

    suma = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j+3 >= len(matrix[i]):
                break
            else:
                for n in range(4): #4 adjancent numbers
                    suma*=matrix[i][j+n]
                if suma > big_sum:
                    big_sum = suma
                suma = 1
        suma = 1
    return big_sum

def solve_columns(matrix, big_sum):#finds sum of 4 adjacent digits in columns and if sum > big_sum it overwrites big_sum
    suma = 1
    for i in range(len(matrix[1])):
        for j in range(len(matrix)):

            if i+3 >= len(matrix):
                break
            else:
                for n in range(4): #4 adjancent numbers
                    suma*=matrix[j][i+n]
                if suma > big_sum:
                    big_sum = suma
                suma = 1
        suma = 1
    return big_sum

def main():
    grid = open("matice.txt","r")
    Matrix=[]
    for line in grid:
        nums = list(map(int, line.split()))
        Matrix.append(nums)
    #máme matici
    big_sum = 0
    
    
    big_sum = solve_columns(Matrix, big_sum)
    big_sum = solve_rows(Matrix, big_sum)
    big_sum = solve_diag(get_diagonals(Matrix, direction=True), big_sum) #left diagonals
    big_sum = solve_diag(get_diagonals(Matrix, direction=False),big_sum) #right diagonals
    print(big_sum)

main()

