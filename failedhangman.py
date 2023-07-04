import math
import random

str = "hello"
print(str[1])


#Randomly selects a word for the game
wordbank = ["Hello", "Whats up", "Heyyy"]

wordID = random.randint(0,2)
myWord = wordbank[wordID]

#creates empty list 
displayTerms = []

terms = myWord.split(" ")
idi = -1

#creates an array for each word, then changes each letter to be _
for term in terms:
    charNum = 0
    idi += 1
    newTerm = []
    for char in term:
        charNum += 1
        newTerm += "_"
    displayTerms += [newTerm]
    
def display():
    for term in displayTerms:
        statement = ""
        for char in term:
            statement += char + " "
        print(statement)

display()