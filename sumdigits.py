def sumdigits(str1):
    count = 0
    total = 0
    # avg = 0

    for i in str1:
        if i.isdigit():
            count += 1
            total += int(i)
        if count > 0:
            avg = total / count

    print('Total is: ', total, 'Average is: ', "%.2f" % avg)


str1 = input("Enter")
sumdigits(str1)