def pattern(num):
    for row in range(1, num+1):
        for column in range(1,row+1):
            print(column, end=" ")
        print("")


num = int(input("Enter num"))
pattern(num)