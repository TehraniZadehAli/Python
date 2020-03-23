import sys
sys.setrecursionlimit(10**6)
def recursive(num):
    if num:
        return num + recursive(num -1)
    else:
        return 0

num = int(input("Num"))
print(recursive(num))