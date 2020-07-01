#creating check marks function
def check_marks(marks):
    try:
        if(marks>=90):
            return True
        else:

        #raised the exception
            raise Exception("Marks are Less.Your not Eligible")
    except Exception as e:
        print(e)
n = int(input("Enter marks: "))  
z= check_marks(n)     
if(z):
    print("You are eligible.Congrats")
