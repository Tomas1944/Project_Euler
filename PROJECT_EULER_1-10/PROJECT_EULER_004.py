# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.




nejvetsi_palindrom=0
for a in range(100,1000):
    for b in range(100,1000):
        suma = a*b
        string= str(suma)
     
        if string[0]==string[-1] and string[1]==string[-2] and string[2]==string[-3]:
            palindrom=int(string)
            if palindrom>=nejvetsi_palindrom:
                nejvetsi_palindrom=palindrom
            else:
                pass  
        else:
            pass
print(nejvetsi_palindrom)
