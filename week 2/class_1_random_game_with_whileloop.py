guess=0
while True:
    num=int(input("Enter your number: "))
    guess+=1
    if num==5:
        print("Number is,",num,"you guessed it in",guess,"tries")
        break