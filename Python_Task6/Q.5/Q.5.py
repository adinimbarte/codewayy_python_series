# taking user input as string
string = input("Enter the sentence:").split()

# initializing count to 0
count=0

# countiing number of words
for i in string:
    count=count+1
    
# printing no of words
print("Number of words in the sentence is:", count)
