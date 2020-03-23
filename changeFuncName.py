def student(name, age):
    print(name, age)


name = input("Enter name")
age = int(input("Enter age"))
student(name, age)
show = student
show(name, age)