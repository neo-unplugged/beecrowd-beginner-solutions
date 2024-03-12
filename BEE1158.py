N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    total = 0
    while y != 0:
        if x % 2 != 0:
            total += x
            y -= 1
        x += 1
    print(total)
