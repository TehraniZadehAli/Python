def inToFLoat(inLst):
    lstItems = inLst.split()
    x =[]
    for i in lstItems:
        x.append(float(i))
    print(x)


inLst = input("Enter List whit space")
inToFLoat(inLst)