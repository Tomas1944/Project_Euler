"""The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?"""



def Letter_position(letter): #returns position of letter in alphabet, we are working only with upper numbers
    return int(ord(letter)-64)

def ConvertString(string): #returns list of worlds
    string.replace("'","") #dát pryč uvozovky
    string = string.split(",")#vytvoří dvojité uvozovky
    for i in range(len(string)): #odstranění dvojiitých uvozovek
        string[i] = string[i][1:-1]
    return string 
    


Triangle_numbs = [int(n*(n+1)/2) for n in range(1,100)]#array of Triangle numbs

fp = open("words.txt","r") #open file with words
words = []
for line in fp:
    words = ConvertString(line) #convert large string of words in array of worlds

Triangle_count = 0
for nouns in words:
 
    sum_of_letters = 0
    for letter in nouns:    #for every letter in word
        Value_of_let = Letter_position(letter)   #position in alphabet
        sum_of_letters+=Value_of_let
    if  sum_of_letters in Triangle_numbs:   #Sum is trangle num
        Triangle_count+=1


print(Triangle_count)
