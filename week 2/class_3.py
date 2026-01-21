# Print even numbers from 1 to 20
print("Even Numbers: ")
for i in range(1,21):
    if i%2==0:
        print(i,end=" ")
print()

# Alternative way to print even numbers

print("Even Numbers: ")
for i in range (2,21,2):
    print (i,end=' ')

# FizzBuzz from 1 to 30
for i in range(1,31):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)

# Nested loops with continue statement

for i in range(1,6):
    for j in range(1,6):
        if j==3:
            continue
        print(j)
    if i==4:
        continue
    print("Outer Loop:",i)

# Pattern printing

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()