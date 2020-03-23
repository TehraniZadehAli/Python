str1 = "P@#yn26at^&i5ve"
lower = 0
upper = 0
digits = 0
symbols = 0

for i in str1:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1
print("lowers are " , lower , "uppers are " , upper , "digits are"
      ,digits , "symbols are " ,symbols , "chars are " , lower + upper)