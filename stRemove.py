def stRemove(str,num):
    newStr = str[num::]
    print(newStr)

str = input("Enter str")
num = int(input("Enter num"))
stRemove(str,num)