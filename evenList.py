# def evenList(num):
#
#     lst =[]
#     for i in range(4, num+1):
#         if i % 2 == 0:
#             lst.append(i)
#     print(lst)


num = int(input("Enter"))
# evenList(num)
print(list(range(4, num+1, 2)))