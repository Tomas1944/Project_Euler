#najít prvočíslo s indexem 10001 - program běží dlouho - chtělo by ho zrychlit
import math

def SieveOfEratosthenes(n):
      
    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.

    prime = [True for i in range(n)]
    p = 2
    while (p * p <= n):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2,n, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return prime


primes = SieveOfEratosthenes(int(1e6))
place = 10001
b=0


for i in range(len(primes)):

    if primes[i]:
        b+=1
    if b == place:
        print(i)
        break

print(b)