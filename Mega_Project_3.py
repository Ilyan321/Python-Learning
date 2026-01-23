import random
i=1
print("---------------Number Guessing Game---------------")
while True:
    guess=random.randint(1,10)
    score=int(0)
    print("Round ",i)
    for i in range (3):
        print("The computer guessed:",guess)
        num=int(input("Enter a number between 1 and 10: "))
        if num==guess:
            print("You guessed correctly!  10 Score added.")
            score+=10
            print("Your total score is:",score)
            i+=1
            break
        else:
            print("You guessed incorrectly!")
        print()  
    print("----------Your final score is:",score)
    print()
    i+=1
