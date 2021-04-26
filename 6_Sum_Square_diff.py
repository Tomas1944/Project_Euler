"""The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + 10**2 = 385

The square of the sum of the first ten natural numbers is,
    (1+2+3+...+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is  3025 - 385.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


sum1=0 #sum of squares
sum2=0 #square of the sum

for a in range(1,101):
    sum2+=a
    sum1+=a**2

sum2=sum2**2 #calculate sqare of the sum

End_sum = abs(sum2-sum1)
print(End_sum)
