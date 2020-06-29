with open('fileHandling.txt', 'r') as f:

    # intializing size to read as 10
    sizeToRead =10


    fContents = f.read(sizeToRead)

    # printing 10 character per read
    while len(fContents) > 0:
        print(fContents, end="")
        fContents = f.read(sizeToRead)
