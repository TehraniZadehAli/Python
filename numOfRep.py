def numOfRep(str):
    x = str.split()
    count = 0
    for i in x :
        if i == "Emma":
            count +=1
    print(count)

str = input("Enter")
numOfRep(str)
