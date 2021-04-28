"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included."""

# 9! = 362880 -> 6 digits can have maximal value cca 2e6 --> 7 digits can have maximal value cca 2,5mil 
# ==> maximal potencial value that can have factorial digit sum == number  is 7*9!

import math

def Factorial_digit(number):
    
    Factorial_sum = 0
    for i in str(number):#for digit in number
        Factorial_sum+= math.factorial(int(i)) #factorial sum
    return Factorial_sum

MAX = 7* math.factorial(9) #max potencial value
End_sum = 0

for i in range(3,MAX + 1):

    if i == Factorial_digit(i):
        End_sum+=i  

print(End_sum)
