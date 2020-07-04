
# speed limit function declared with speed as parameter
def speedLimit(speed):
    extra=0

    # checking speed is greater than 70 or not
    if(speed>70):
        extra=speed-70
        point=extra/5

        # Printing de-merit points
        print("De-Merit Point:",int(point))

        #if point exceed than 12 licence suspended
        if point>=12:
            print("Licence suspended")
    else:
        print("OK")
        
# storing user input
speed = int(input("Enter the speed:"))

#calling function
speedLimit(speed)
