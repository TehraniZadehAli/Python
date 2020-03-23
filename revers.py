def reverse(num):
    orgnum = num
    rev = 0
    while num> 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10
    if orgnum == rev:
        print("Mashala")
    else:
        print("Zeki")


num = int(input("Enter num"))
reverse(num)
