x = int(input())
y = int(input())

if x > y:
    temp = y
    y = x
    x = temp

my_nums = range(x+1, y)
qualified_nums = filter(lambda i: (i % 5 == 2) or (i % 5 == 3), my_nums)
for x in qualified_nums:
    print(x)
