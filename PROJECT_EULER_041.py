"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""
import math

def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def permutations(string):
    #vytvoří všechy permutace
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, "", 1))]
    return permutation_list

#sum of digits 1-9 == 45, that means its divisible by 3, so every 9 digit num is divisible by 3
#sum of digits 1-8 == 36, same problem 
#when we have digits 1-7, then their sum is 28, so its possible to find a prime

pandigital_num = permutations("7654321")
max_num = 0

for num in pandigital_num:

    int_num = int(num)
    if int_num > max_num and isprime(int_num) :
        max_num = int_num
    
print(max_num)
