#declaring matrix
matrix=[]
element=0

# taking input from user of row and column
row=int(input("enter the value of row: "))
column=int(input("enter the value of column: "))
print("Note:enter element row wise")

#getting elements of matrix from user
for i in range (row):
    a=[]
    for j in range (column):
        element=int(input("enter the element:"))
        a.append(element)
    matrix.append(a)
 
#printing user entered matrix
print("Entered Matrix is: ")
for i in range (row):
    for j in range (column):
        print("  " ,matrix[i][j], end=" ")
    print("")

#printing length of the matrix
print("elements in matrix:",sum(len(x) for x in matrix ))
print()

#printing prime numbers of matrix
print("prime numbers in matrix are:",end=" ")


for list in matrix:
    for subList in list:
        if subList>1:
            for v in range(2,subList):
                if(subList % v)==0 :
                    break
            else:
                print(subList,end=" ")
