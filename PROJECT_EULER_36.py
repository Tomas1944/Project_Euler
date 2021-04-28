"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""


def IsDecPalindrom(numb):
    if str(numb) == str(numb)[::-1]: #Numb is palindrom
        return True
    else:
        return False


def IsBinPalindrom(binary):
    tmpbin = binary[2::]    #without 0b in front of the bin numb
    if str(binary[2::]) == str(tmpbin)[::-1]: #binary numb is palindrom
        return True
    else:
        return False


End_sum = 0
Max = int(1e6)#maximal value

for i in range(Max):
    if IsDecPalindrom(i) and  IsBinPalindrom(bin(i)): #numb is palindrom in both bases
        End_sum+=i

print(End_sum)


