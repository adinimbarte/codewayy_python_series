#function for and operator
def andOperator(x,y):
    print(" %d and %d are greater than 100? Ans="%(x,y),end=" ")
    if ( x > 100 and y > 100 ):
        print("True")
    else:
        print("False")
        
#function for or operator
def orOperator(u,v):
    print("%d or %d are greater than 100? Ans="%(u,v),end=" ")
    if ( u > 100 or u >100):
        print("True")
    else:
        print("False")
       

#function for not operator
def notOperator(num):
    if(num):
        print("num value is changed to",not num)
