#Guess the Number Game

#The program will have to select random numbers
#So we need to import the random module
#This is done by using the import keyword
#Other useful modules include 'import math' or 'import time'
import random

#Create the starting variables
minValue=1
maxValue=20
numOfGuesses=6
guessesTaken=0

#randint() from the random module choses an integer between the first parameter and
#the last parameter. Used like this random.randint(minimum, maxiumum)
chosenNum=random.randint(minValue,maxValue)

#Introduction
#print is used to display a message
print("Hello, this is the Guess The Number Game")
print("What is your name")

#Input keyword is used to get input from the user
playerName=input("My name is ")

#str() is used to convert integers(and all other data types too) to strings
# + is used to concatenate (combine) different strings
print(playerName + ", I have chosen a number between "+ str(minValue) +" and " +str(maxValue))
print("Guess my number, You have "+ str(numOfGuesses) +" guesses")

#Start the game

#while the number of guessesTaken is less than the num of guess available, the game goes on
while guessesTaken<numOfGuesses:
    #int() is used to convert a string to an integer
    currentGuess=int(input("Guess " + str(guessesTaken+1) +": "))
    
    #Note that == is used here and not =. == is for comparing two things
    #while = is for assigning a value to a variable
    #If the current guess is right
    if currentGuess==chosenNum:
        print("You are correct!")
        print("You have won the game")
        #Break is used to leave the loop. In this case, the while loop
        break
    #If the current guess is too low
    if currentGuess<chosenNum:
        print("Your guess is too low")
    #if current guess is too high
    if currentGuess>chosenNum:
        print("Your guess is too high")
        
    #After the loop, increase the number of guessesTaken by one
    # += is a shorthand for addition to itsrlf
    #For example a += 1 is the same thing as a = a + 1
    #The same thing can be done for -, * and /
    guessesTaken +=1

#Print a message if the number of tries is used up
if guessesTaken==numOfGuesses:
    print("Your guesses have been used up")
    print("The game is over")
    
print("Thanks for playing")
print("Try to adapt this game so that a player can choose to try again with a different chosen number")
print("For an extra challenge, ensure that the players are forced to put in integers")
print("For example, if the players type in 'w' as their guess, the program says 'Please input a number, letters are not allowed' and re prompts them for their input")

    
    
    