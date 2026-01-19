#write a python program that skips the number 5 while counting down from a given number to 1.

# # countdown from num to 0
# print("Countdown Timer")
# num=int(input("Enter a number: "))

# while num>0:
#   if(num==5):
#         num-=1
#         continue
#   print(num)
#   num-=1
# print("Hurrah you reached the countdown end")


# #matrix
# i=1
# while i<6:
#     j=1
#     while j<6:
#         print(i*j, end="\t")
#         j+=1
       
#     i+=1
#     print()

# # infinite loop
num1=1
while (num1<10000):
  if(num1==1000):
     break
  print("This is infinite loop",num1)
  num1+=1