def sumNumsN(num):
    total = 0
    for i in range(num + 1):
        total += i
    print(total)


num = int(input("Enter Number"))
sumNumsN(num)