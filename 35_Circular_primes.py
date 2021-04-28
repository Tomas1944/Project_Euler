"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

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
    prime[1]= True

    return prime


def All_rot_prime(prime,primes): #return True if all numbers rotation are primes

    digit = len(str(prime))
    powTen = pow(10, digit - 1)
      
    for i in range(digit - 1):
          
        firstDigit = prime // powTen
          
        #calculate left shift from previous number
        left = (prime * 10 + firstDigit - 
               (firstDigit * powTen * 10))
        # Update the original number
        prime = left
        if not primes[prime]:   #rotation isnt prime
            return False 

    return True #all rot are primes



primes = SieveOfEratosthenes(int(1e6))
count = 0

for i in range(2,int(1e6)):
    if primes[i] and All_rot_prime(i,primes): #number and all his rotations are primes
        count+=1

print(count)
