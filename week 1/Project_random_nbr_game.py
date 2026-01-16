# A simple random number guessing game
import random
secret_number= random.randint(1,100)
print("I have selected a random number betwen 1 to 100. Can you guess it?")
attempts=0
while True:
    guess = int(input("Enter your Guess: "))
    attempts +=1
    if guess < secret_number:
        print("The number is higher than your guess. Try again.\n")
    elif(guess>secret_number):
        print("The number is lower than your guess. Try again.\n")
    else:
        print("Congratulations! You've guessed the correct number in",attempts,"attempts.")
        break
    