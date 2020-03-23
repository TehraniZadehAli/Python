def mixstr(s1,s2):
    s2 = s2[::-1]
    lens1 = len(s1)
    lens2 = len(s2)
    lenght = lens1 if lens1 > lens2 else lens2
    res = ""
    for i in range(lenght):
        if i < lens1:
            res += s1[i]
        if i < lens2:
            res += s2[i]
    print(res)


s1 = input("Enter s1")
s2 = input("Enter s2")
mixstr(s1, s2)