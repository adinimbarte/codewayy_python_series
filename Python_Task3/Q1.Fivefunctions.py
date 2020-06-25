#Function to return full name by concatenating
def concatName(firstName,lastName):
    fullName = firstName+ " " + lastName
    return(fullName)

#Function to calculate total marks
def calculateMarks(listOfSubjects):
    totalMarks=sum(listOfSubjects)
    return(totalMarks)

#Function to calculate percentage
def calculatePercentage(numberOfSubject,totalMarks):
    percentage = totalMarks/numberOfSubject
    return(percentage)

#function to calculate grade
def calculateGrade (Score):
     if(Score >= 95):
        return('A')
     elif(Score >= 85 and Score <= 95):
        return('B')
     elif(Score >= 75 and Score <= 85):
        return('C')
     elif(Score >= 65 and Score <= 75):
        return('D')
     else:
        return("F")

#function to display all the details
def displayDetails (firstName,lastName,numberOfSubject,listOfSubjects):
    #calling concatName function
    print("Full Name:", concatName(firstName,lastName))
    
    #calling calculateMarks Function
    totalMarks= calculateMarks(listOfSubjects)
    print("Total Marks:",totalMarks)
    
    #calling calculatePercentage function
    Score=calculatePercentage(numberOfSubject,totalMarks)
    print("Score in Percentage:",Score)
    
    #calling calculateGrade function
    Grade=calculateGrade(Score)
    print("Grade: ", Grade)
    
    
# Taking first and lastname as inputs      
firstName = input("Enter your Name: ")
lastName = input ("Enter your Surname:")

#declaring an empty list
listOfSubjects=[]

#taking input of number of subject
numberOfSubject=int(input("enter number of subjects:"))

#adding marks to the list
for n in range(numberOfSubject):
    mark=int(input("enter mark : "))
    listOfSubjects.append(mark)

#calling displayDetails function
displayDetails (firstName,lastName,numberOfSubject,listOfSubjects)
