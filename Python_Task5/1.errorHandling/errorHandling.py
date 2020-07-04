# using try,raise and except for exception handling
try:
    
    # taking inputs from user
    num1 = int(input("Enter any number:"))
    num2 = int(input("enter any number:"))
    
    z = num1 + num2
    print(z)
    
    # created raise just to check working 
    raise ValueError("Error:try is executed succesfully")

# if above code failed exception will be printed
except ValueError as e:
    print(e)
finally:
    print("program is finally executed")
