def repForNums(nums):
    for i in range(1, nums+1):
        for j in range(i):
            print(i, end=" ")
        print()


nums = int(input("Enter"))
repForNums(nums)