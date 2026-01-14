# to check if the number is even or odd
print("-----Even or Odd Check")
num=int(input("Enter a number: "))
if(num%2==0):
    print("The Number ",num," is Even.")
else:
    print("The Number ",num," is Odd.")
    
# to check voting eligibility
print("\n-----Voting Eligibility Check")
age=int(input("Enter your age: "))
if (age>=18 and age<=70):
    print("You are eligible for voting.")
elif(age>70):
    print("You are long dead bro.")
else:
    print("You are not eligible for voting.")
    
#Student score
print("\n-----Student scoring")
score=int(input("Enter your score: "))
if(score>=50 and score<=100):
    print("You have passed the exams.")
elif(score>100):
    print("pls score should be under 100.")
else: 
    print("You failed bro.")

#    he movie rates

ticket=int(input("Enter your age to know the ticket price: "))
if (ticket<10):
    print("You are free kid.")
elif(ticket>10 and ticket<60):
    print("Your ticket price is $50.")

