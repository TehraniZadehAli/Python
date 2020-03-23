#Define a function for changing value of two variables
def changevar(a,b):
    a = a + b   #Assign a+b to a
    b = a - b   #Assign a-b to b
    a = a -b    #Assign a-b to a
    print("a2 is : " ,a)    #Printing new value for a
    print("b2 is : " ,b)    #Printing new value for b

a = int(input("a"))     #Getting number from user
b = int(input("b"))
print(changevar(a,b))   #Call the function and print output



