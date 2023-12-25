import random
from time import sleep
import sys

print("Hello, Whats your name?")

name = input("Myname is: ")

print("Well " + name + ", I am thinking of a number between 1 and 20!")

secretNumber = random.randint(1,20)

    
  

for guessesTaken in range(1,7):
  print("What is your guess?")
  guess = int(input())

  if guess < 1 or guess > 20:
    print("Your number is out of range, Play by the rules!!!")
    sys.exit(1)
  elif guess < secretNumber:
    print("Your guess is to low, try again!")
  elif guess > secretNumber: 
    print("Your guess is to high, try again!")
  else:
    break

if guess == secretNumber:
  print("WOW " + name + " you guessed it in " + str(guessesTaken) + " guesses!")
else:
  print("Nope, the secret number I was thinking of was " + secretNumber)
