def inTrue(lst):

    lstStart = lst[0]
    lstEnd = lst[len(lst) - 1]
    if lstStart == lstEnd:
        print("True")
    else:
        print("False")

lst = list(input("Enter"))
inTrue(lst)