str1 = "eyyyyyyyyyyyybabooooAAAlli"
result = dict()
for i in str1:
    count = str1.count(i)
    result[i] = count
print(result)
