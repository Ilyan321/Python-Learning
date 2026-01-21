# maximum value in list
num=[1,2,3,4,5,0.5,4,3,2,1]

max_num=num[0]
for i in num:
    if i>max_num:
        max_num=i
print("maximum: ",max_num)

# minimum value in list

min_num=num[0]
for i in num:
    if i<min_num:
        min_num=i
print("minimun: ",min_num)




