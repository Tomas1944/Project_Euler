"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

def SieveOfEratosthenes(n):
      
    # Create a boolean array "prime[0..n**(1/2)+1]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n+1):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2,n+1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    return prime


suma=0
primes = SieveOfEratosthenes(int(2e6)) #create array of primes bellow 2e6
for x in range(int(2e6+1)):
    if primes[x]:
        suma+=x
    
  
print(suma)
