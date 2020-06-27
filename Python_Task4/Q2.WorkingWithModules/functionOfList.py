#A python file which should have a function to calculate the square of a number, find the maximum of a number in a list, minimum of a number in a list.Sum of all numbers in a list. (Not allowed to use default python function)


#created a function to calculate the square of number
def calculateSquare ( number ) :
    squareOfNumber = number**2
    print("Square of",number,"is :",squareOfNumber)

#created a function to find maximum number in the list
def findMax(List) :
    max = 0
    for i in List :
        if ( max < i ) :
            max = i
    print("The maximum number in the list is: ", max)

#created a function to find minimum number in the list
def findMin(List):
    min = List[0]
    for i in List:
        if ( min > i ) :
            min = i
    print("The minimum number in the list is: ", min)

#created a function to find sum of numbers in the list
def sumOfNumberList(List):
   Sum = 0
   for number in List:
        Sum = Sum + number
   print("Sum Of all the numbers in the list is :",Sum)
