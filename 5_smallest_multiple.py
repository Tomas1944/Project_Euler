"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""


from fractions import gcd

end_number = 0 #smallest multiple

numb_1 = 1
numb_2 = 2

def smallest_multiple(number1,number2): #return smallest multiple of 2 numbers
    return number1*number2//gcd(number1,number2) #function gcd returns greatest divisor

for i in range(20):
    end_number = smallest_multiple(numb_1,numb_2)
    numb_2 +=1 #we need to find smallest multiple of numbers 1-20
    numb_1 = end_number 

print(end_number)#smallest multiple of numbers 1-20