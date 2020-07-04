import math as m

# taking no of element in list as input
n = int(input("enter number of elements in the list:"))

# initializing an empty list
list1 = []
for i in range(n):
    num = float(input("enter value:"))
    list1.append(num)
print("This is Sorting of List")
print("Orignal List :", list1)

# Printing sorted list
sList = sorted(list1)
print("Sorted List: sList:", sList)

# Printing sorted list in reverse order
sList.sort(reverse=True)
print("Sorted List in reverse order:", sList)
print()

# tuple function containing sorting methods
def tupleSorting(List):
    print("This is Sorting of Tuple")

    # converting list to tuple
    tuple1 = tuple(List)
    print("Orignal tuple :", tuple1)
    
    # printing sorted tuple
    sTuple = tuple(sorted(tuple1))
    print("Sorted Tuple: ", sTuple)

    # printing sorted tuple in reverse order
    sTuple = tuple(sorted(tuple1,reverse=True))
    print("Sorted tuple in reverse order:", sTuple)
    print()


def setSorting(List):
    print("This is Sorting of Sets")

    # converting list to set
    set1 = set(List)
    print("Orignal set:", set1)
    
    # printing the sorted set
    s_set = set(sorted(set1))
    print("Sorted Set:", s_set)
    
    # printing the sorted set in reverse order
    s_set = set(sorted(set1, reverse=True))
    print("Sorted set in reverse order:", s_set)
    print()

# calling tuple sorting and set sorting functions
tupleSorting(list1)
setSorting(list1)

print("==================================================================")
print("Using Math functions\n")
for i in list1:

    # using sqrt() and floor() to find square root and floor value(i.e nearest small integer)
    print("Square Root %.2f: %.2f\t floor value:%d" % (i, m.sqrt(i), m.floor(i)))


# using pow() function to find power
print("2 to the power 3:", m.pow(2, 3))

# printing standard values
print("Pi=%f\te=%f\t" % (m.pi, m.e))


# printing the greatest common divisor of 12 and 64.
print("Greatest Common Divisor of 12 and 64:", m.gcd(64, 12))

# Printing value of sine 30
print("The value of sin(30 degree): " + str(m.sin(m.pi/3)))
