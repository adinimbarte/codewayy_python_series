#printing numbers using for loop
def usingWhile():
    number=0
    print("printing numbers using while loop:")
    while(number<=10):
        if(number==3 or number==7):
            number+=1
            continue;
        else:
            print(number)
            number+=1

#printing numbers using for loop
def usingFor():
    print("printing numbers using for loop:")
    for number in range (0,11):
        if(number==3 or number==7):
            continue;
        else:
            print(number)

#calling function usingWhile
usingWhile()

#calling function usingfor  
usingFor()
