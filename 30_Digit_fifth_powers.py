"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

#The number connot be bigger than 6*(9**5), because than the value of the sum of the digits cannot be bigger than the number itself

def Digit_fifth_power(number):
    Digit_sum = 0
    for i in str(number): #every digit
        Digit_sum+= int(i)**5 #fifth power of the digit

    return Digit_sum


MAX = 6*(9**5)
suma = 0

for i in range(2,MAX +1):
    if i == Digit_fifth_power(i):
        suma+=i

print(suma)