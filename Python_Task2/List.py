# Some methods of lists in python

# list declaration
list = [10, 54, 69, 78, 32, 45]
# printing the list
print('list:', list)

# adding elements to the last position of List.
list.append(47)
print('appended list:', list)

# prints the index of element
print('47 is at index:', list.index(47))

List2 = [89, 37]
# Adds contents of List2 to the end of list
list.extend(List2)
print('after extending list:', list)

# Inserts an elements at specified position
list.insert(2, 56)
print("56 is inserted at 2nd position:", list)

# Calculates sum of all the elements of List
print('sum of all elements', sum(list))

# removes the last element of the list
print('removed element:', list.pop())

# prints minimum element in the list
print('minimum element in list:', min(list))

# prints maximum element in the list
print('maximum element in list:', max(list))
