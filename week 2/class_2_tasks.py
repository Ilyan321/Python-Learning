# task 1   print only even numbers from a list
numlist=[1,2,3,4,5,6,7,8,9,10]
print("Even numbers: ",end=" ")
for i in numlist:
    if i%2==0:
        print(i,end=" ")
print()

# task 2   print only odd numbers from a list
numlist=[1,2,3,4,5,6,7,8,9,10]
print("Odd numbers: ",end=" ")
for i in numlist:
    if i%2!=0:
        print(i, end=" ")
print()
# task 3 pattern printing

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    

