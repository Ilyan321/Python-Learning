matrix=[[1,2,3],[4,5,6],[7,8,9]]
colomn_sum=0
row_sum=0
for row in matrix:
   print (row)
    
row_sum=0
for row in matrix:
    print("sum:",sum(row))
    
col1=0
col2=0
col3=0
for row in matrix:
    col1+=row[0]
    col2+=row[1]
    col3+=row[2]
print("Column 1 sum:",col1)
print("Column 2 sum:",col2)
print("Column 3 sum:",col3)