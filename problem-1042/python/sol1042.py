# get the numbers and turn them into a list
numbers = [int(i) for i in input().split()]
# make of the numbers
numbers_copy = numbers.copy()
# sort in ascending order copied number
numbers_copy.sort()

for i in numbers_copy:
    print(i)
# add a blank line
print()
for i in numbers:
    print(i)
