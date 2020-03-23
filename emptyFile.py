"""count = 0
f = open('test3'
         '.txt', 'r')
count = len(f.readlines())
with open('test3.txt', 'r') as f:
    if count == 0:
        print("Empty")
    else:
        print("Full")"""
import os
print(os.stat("test2.txt").st_size ==0)