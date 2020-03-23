def divide3_5(num):
    i = 0
    while i <= num:
        if i % 5 ==0 and i % 3 == 0:
            print(i)
        i += 1


num = int(input("Enter"))
divide3_5(num)