"""An irrational decimal fraction is created by concatenating the positive integers:

        0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d-n represents the n-th digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""



Constant_ad = 2 #number added to the constant
cham_const = ".1" #constant
digit = 1 #digit to find in constant

End_sum = 1
while(digit <= int(1e6)): #end of the expresion

     if digit < len(cham_const):      #digit can be in current constant
        End_sum*=int(cham_const[digit])
        print(digit,End_sum,cham_const[digit])
        digit*=10

     else: #constant is short
        cham_const = cham_const + str(Constant_ad) #od number to the constant
        Constant_ad+=1
    

print(End_sum)