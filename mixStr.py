s1 = ("America")
s2 = ("Japan")
mids1 = int(len(s1)/2)
mids2 = int(len(s2)/2)
s3 = s1[:1] + s2[:1] + s1[mids1] + s2[mids2] + s1[len(s1)-1] + s2[len(s2)-1]
print(s3)