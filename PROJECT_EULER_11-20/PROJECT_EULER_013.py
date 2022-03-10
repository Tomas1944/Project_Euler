#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

f=open("largesum.txt","r")

suma=0

for line in f:
    suma+=int(line)
print(str(suma)[:10])
