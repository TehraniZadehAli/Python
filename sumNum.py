def sumNum(num):
    num0 = 0
    for i in range(num):
        num = num0 + i
        print(num)
        num0 = i

num = int(input("enter num"))
sumNum(num)