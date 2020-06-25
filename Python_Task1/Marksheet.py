#taking input from user
fname=input("Enter your First Name:")
lname=input("Enter Your Last Name:")
clg=input("Enter College Name:")
address=input("Enter address:")

# marks of 5 subjects taken individually
english=int(input("enter marks obtained in english:"))
marathi=int(input("enter marks obtained in marathi:"))
maths=int(input("enter marks obtained in maths:"))
science=int(input("enter marks obtained in science:"))
history=int(input("enter marks obtained in history:"))

#all marks are added to find total
total = int(english+marathi+maths+science+history)
per=float(total/5);

#printing output
print("Name:", fname+" "+lname) #concatenation of first and last name
print("College and address: ", clg+ ","  + address) #concatenation of college name and address
print("Total marks:",total)
print("Percentage:",per )



