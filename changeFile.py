file1 = open('test1.txt', 'w')
file1.writelines(['line1 \n', 'line2 \n', 'line3 \n', 'line4 \n', 'line5'])
count = 0
file1 = open('test1.txt', 'r')
count = len(file1.readlines())
with open('test1.txt', 'r') as file1:
    lines = file1.readlines()
    print(lines[2])

    with open('test2.txt', 'w') as file2:
        for lines in file1:
            if count == 3:
                count -= 1
                continue
            else:
                file2.write(lines)
                count -= 1