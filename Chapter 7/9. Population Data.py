"""
Purpose: Write a program that simulates a Magic Ball.
Input: File called 8_ball_responses will be read. User will be asked if they want to continue
       with the program. User will enter 'true' to continue with the program and to quit, input anything else. They will then input a question

Output: The computer will randomly generate an answer to the question. User will be asked
        if they want to continue.
Algorithm:
        1. import the random library
        2. Create a list called magicBall
        3. Open the text file
        4. Read data into list
        5. Ask if the user wants to continue
        6. Prompt user to enter a question
        7. Program will randomly display a response
        8. Program will ask user if he/she wants to continue
Test Data:
        Enter 'true'  if you wish to continue: true
        Please enter a question here: Do you live in PA?
        I’m not sure.
        Enter 'true'  if you wish to continue: no
        
"""

#Import the random library
import random

#Create a list called magicBall
magicBall = []

#Open the text file 
infile = open(r"E:\CMPSC121\8_ball_responses.txt", "r")

#Read data into list
for line in infile:
        line = line.rstrip('\n')
        magicBall.append(line)
        
#Ask if the user wants to continue        
ans = input ("Enter 'true'  if you wish to continue: ")


while ans == 'true':
    #Prompt user to enter a question
    question = input("Please enter a question here: ")
    #Program will randomly display a response
    print(magicBall[random.randint(0,len(magicBall)-1)])
    #Program will ask user if he/she wants to continue
    ans = input ("Enter 'true'  if you wish to continue: ")
    if ans != 'true':
        infile.close() 
    

