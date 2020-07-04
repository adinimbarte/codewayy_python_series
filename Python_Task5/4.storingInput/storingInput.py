list1 = []
n = int(input("enter the no of line:"))
for i in range(n):
    line = input("line %d:" %(i+1))
    list1.append(line)
f = open("fileHandling4.txt","w+")
for i in list1:
    f.write(i)
    f.write("\n")
contents=f.read()
print(contents)
f.close()

with open('fileHandling4.txt', 'r') as f:

    # intializing size to read as 10
    sizeToRead =10


    fContents = f.read(sizeToRead)

    # printing 10 character per read
    while len(fContents) > 0:
        print(fContents, end="")
        fContents = f.read(sizeToRead)
