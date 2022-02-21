"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""



from collections import Counter
import math

def divisorGenerator(n): #generator of divisors of a number
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        if divisor != n: 
            yield divisor


def Sum_of_div(array):
    suma = 0
    for i in array:
        suma+=i
    return suma


MAX = 10000

Sum_of_divizors = [int(Sum_of_div(divisorGenerator(n))) for n in range(MAX)]
Sum_of_divizors_count = Counter(Sum_of_divizors)
array = []

for i in Sum_of_divizors_count:

    if Sum_of_divizors_count[i] == 2:
        array.append(i)

#print(array)

End_sum=0
for i in range(MAX):
    if Sum_of_divizors[i] in array:
        End_sum+=i
        #print(i)

print(End_sum)

