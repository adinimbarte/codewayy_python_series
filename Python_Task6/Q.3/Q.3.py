# Taking user input and storing it in a list
string = input("Enter any string:").split()

# declaring list to store alphabets
list1=[]

# appending each alphabet from string
for i in string:
    for j in i:
        list1.append(j)
        
 # upper and lower are initialize to 0
lower=upper=0
for j in list1:
    
    # checking if j is lower or not
    if(j.islower()):
        lower=lower+1
        
    # checking j is upper or not
    elif(j.isupper()):
        upper=upper+1
        
print("upper:",upper)
print("Lower", lower)
