# def lst(lst1, lst2):
#     lst3 = []
#     for num in lst1:
#         if num % 2 != 0:
#             lst3.append(num)
#     for num in lst2:
#         if num %2 ==0:
#             lst3.append(num)
#     print(lst3)
#
#
# lst1 = [1,2,3,4,5,6]
# lst2 = [7,8,9,10,11]
# lst(lst1,lst2)
#
floatNumbers = []
n = int(input("Enter the list size : "))
for i in range(0, n):
    print("Enter number at location", i, ":")
    item = float(input())
    floatNumbers.append(item)
print("User List is ", floatNumbers)