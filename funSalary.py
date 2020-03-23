def salary(name,income = 9000):
    if income == 0:
        income = 9000
    print(name,income)


name = input("name")
income = input("income")

salary(name,income)