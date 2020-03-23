s1 = ("abcdefg")
s2 = ("HIJKLMN")
mid = int(len(s1) / 2)
s3 = s1[:mid] + s2 + s1[mid:]
print(s3)