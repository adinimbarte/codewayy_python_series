class Student:
    # defining constructor
    def __init__(self, first, last, lMarks):
        self.first = first
        self.last = last
        self.lMarks = lMarks
    
    # method to return fullname
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    # method to calculate total marks
    def calculateMarks(self):
        totalMarks = sum(self.lMarks)
        return totalMarks
    
    # method to calculate percentage
    def calculatePercentage(self, totalMarks):
        percentage = totalMarks / len(self.lMarks)
        return percentage

    # function to calculate grade
    def calculateGrade(self, Percentage):
        if Percentage >= 95:
            return 'A'
        elif 85 <= Percentage <= 95:
            return 'B'
        elif 75 <= Percentage <= 85:
            return 'C'
        elif 65 <= Percentage <= 75:
            return 'D'
        else:
            return "F"

    # function to display all the details
    def displayDetails(self):
        # calling concatName function
        print("Name: ", self.fullname())

        # calling calculateMarks Function
        totalMarks = self.calculateMarks()
        print("Total Marks:", totalMarks)

        # calling calculatePercentage function
        Percentage = self.calculatePercentage(totalMarks)
        print("Score in Percentage:", Percentage)

        # calling calculateGrade function
        Grade = self.calculateGrade(Percentage)
        print("Grade: ", Grade)


# providing data to constructor
stud1 = Student("aditi", "Nimbarte", [78, 78, 78, 78])
stud2 = Student("sakshi", "Nimbarte", [60, 60, 60, 60])

# displaying detail of student 1
print("\nDetails of Student 1")
stud1.displayDetails()

# displaying detail of student 1
print("\nDetails of student 2")
stud2.displayDetails()
