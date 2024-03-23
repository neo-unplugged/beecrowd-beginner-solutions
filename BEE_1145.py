x, y = map(int, input().split())
count = 0

for num in range(1, y+1):
    count += 1
    if count == x:
        print(num)
        count = 0
    else:
        print(num, end=" ")
