list=[1,2,3,4,5,6,7,8,9]
list.append(10)         #add element at end
print(list)       #print whole list
print(sum(list)) #sum of all elements
print(len(list))    #length of list
print(type(list))   #type of list
print(list[-1])     #print last element
print(list[2:5])    #print elements from index 2 to 4

if(5 in list):
    print("5 is present in list")    #to check if element is present in list
list.insert(10,11)      #insert 11 at index 10

list2=[12,13,16,17,18,14,15]
list.extend(list2)   #extend list by all all elements of list 2

list.remove(11)        #remove 11 from list
print(list)
list.pop(0)      #remove element at index 0 no index removes last element

list.sort()     #sort the list
print(list)

