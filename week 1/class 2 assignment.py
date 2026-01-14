name=input("Enter your name: ")
age=int(input("Enter your age: "))
hobby=input("Enter your favourite hobby: ")
year=int(input("Enter your Birth year: "))

print("\n")
left=100-age

print("Welcome, Mr.",name+".")
print("You have",left,"years left until you turn into 100.")
print("Your age in dog years is",str(age*7)+".")
print("You were born in",year,"and love",hobby+".")
