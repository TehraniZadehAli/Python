def strcheck(s1,s2):
    s1List = []
    s2List = []

    for i in s1:
        s1List.append(i)
    for i in s2:
        s2List.append(i)

    print(set(s1) & set(s2))


str1 = input("Enter s1")
str2 = input("Enter s2")
strcheck(str1,str2)
######Secound way!
'''def strcheck(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


str1 = input("Enter s1")
str2 = input("Enter s2")
flag = strcheck(str1, str2)
print(flag)'''