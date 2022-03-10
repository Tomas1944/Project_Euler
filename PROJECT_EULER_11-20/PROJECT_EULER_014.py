"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


biggest_seq = 0
current_seq = 0
biggest_num = 0

for i in range(1,int(1e6)+1): #for numbers 1-1e6
    current_num = i

    while (i != 1):#end of sequence

        if i%2==0: #i is even
            i = i/2
        else: #i is odd
            i = 3*i +1
        current_seq+=1

    if(current_seq>biggest_seq):
        biggest_seq = current_seq
        biggest_num = current_num
    current_seq = 0  #reset sequence

print(biggest_num)

    

