#Find the sum of the digits in the number 100!

a=100
suma=1
vysledek=0
while a > 1:
    suma*=a
    a+=-1
for i in str(suma):
    vysledek+=int(i)
print(vysledek)
print(suma)