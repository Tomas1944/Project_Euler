"""1000-digit Fibonacci number. The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

F1=0
F2=1
suma=0
count = 0
while True:
    suma=F1+F2
    count+=1
    F1=F2
    F2=suma
    if len(str(F2))==1000:
        break
print(count)    
