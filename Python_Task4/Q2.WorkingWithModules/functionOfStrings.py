#A python file which should have a function to find the middle character of a string,count the number of vowels in a string, calculate the length of the string,calculate the number of words in a string

#declaring a functionto find middle character of string
def middleCharacterOfString(String):
        length=lengthOfString(String)
        middle=int(length/2)
        if(length%2==0):
            print("As length is even there are two middle character:'%s%s'" %(String[middle-1],String[middle]))
        else:
            print(String[middle])

#created a function to calculate number of vowels in string
def calculateNoOfVowels(String):
    numberOfVowels=0
    for char in String:
        if(char =="a" or char =="e" or char=="i" or char=="o" or char=="u"):
            numberOfVowels=numberOfVowels + 1
    print("Number of vowels in %s is: %d"%(String,numberOfVowels))


#created a function to find the length of the string
def lengthOfString(String):
    count = 0
    for i in String:
        count=count+1
    print(count)
    return(count)

#created a function to find number of words in the string
def numberOfWords(String):
    word=1
    for i in String:
        if(i==" "):
            word+=1
    print("word:",word)

