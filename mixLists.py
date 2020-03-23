listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3 = []

odds = listOne[1::2]
evens = listTwo[0::2]

list3.extend(odds)
list3.extend(evens)

print(list3)