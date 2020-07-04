# taking string input
string = input("Enter the string from which you want to count number of 'at': ")


# counting occurence of "at" and printing
count=string.count("at")+ string.count("At")+ string.count("At") + string.count("AT")
print("'at'occured %d times in string." % count )
