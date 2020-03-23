# str1, str2, str3 = input("Enter Strings").split()
# print(str1, str2, str3)

quantity = 3
totalMoney = 1000
price = 450

str = ('I have {1} dollars, so I can buy {0} balls for {2:.2f} dollars.')
print(str.format(quantity, totalMoney, price))