#Find the sum of the digits in the number 100!
import math

factorial_sum = math.factorial(100) #sum of factorial 100
vysledek=0

for i in str(factorial_sum):
    vysledek+=int(i)#sum of digits

print(vysledek)
print(factorial_sum)


