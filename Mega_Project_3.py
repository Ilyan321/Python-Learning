import random
score=int(0)
guess=random.randint(1,10)

print("---------------Number Guessing Game---------------")
for i in range (3):
    print("The computer guessed:",guess)

    num=int(input("Enter a number between 1 and 10: "))
    
    if num==guess:
        print("You guessed correctly!  10 Score added.")
        score+=10
        print("Your total score is:",score)
    else:
        print("You guessed incorrectly!")
    print()  
print("----------Your final score is:",score)