
pos = int((39-1)/2)
nums = []

for i in range(pos+1):
    nums.append((2 * i + 1) / (2 ** i))
print("%.2f" % sum(nums))
