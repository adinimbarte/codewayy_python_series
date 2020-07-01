# function is declared
def findType(n):
    sum=0
    
    # addition of all divisors
    for i in range (1,n):
        if (n % i)==0 :
            sum=sum+i
    print("the sum of divisors is:", sum) 

    # checking the condition     
    if  sum<n:
        z=1
    elif sum>n:
        z=-1
    else:
        z=0
    return(z)

# calling function findType
n=int(input("enter the number you wanted to check is perfect or not: "))
result=findType(n)
if(result==1):
    print("Deficient")
elif(result==0):
    print("perfect")
elif(result==-1):
    print("abundant")
