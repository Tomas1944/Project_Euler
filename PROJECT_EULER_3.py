"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def SieveOfEratosthenes(n):
      
    # Create a boolean array "prime[0..n**(1/2)+1]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.

    prime = [True for i in range(int(n**(1/2)+1))]
    p = 2
    while (p * p <= int(n**(1/2)+1)):
          
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
              
            # Update all multiples of p
            for i in range(p * 2,int(n**(1/2)+1), p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

    return prime


x=int(input()) #input number

numbers=[] #prime factors
primes = SieveOfEratosthenes(x)

for a in range(2,x):
    if x%a==0 and primes[a]: # 'a' is divisor of 'x' and is a prime
        x=(x/a) #update input number
        numbers.append(a)
    elif(x<a):
        break
    else:
        continue
    

print(numbers[-1]) #largest prime factor



    


    
