# declare an empty list
nums = []
for i in range(100):
    nums.append(int(input()))  # append the numbers to the empty list

max_num = max(nums)
print(max_num)    # print the maximum number of the list
print(nums.index(max_num)+1)  # index position of maximum number
