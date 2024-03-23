
while True:
    x = int(input())
    if x == 0:
        break
    cnt = 0
    total = 0

    while cnt != 5:
        if x % 2 == 0:
            total += x
            cnt += 1
        x += 1
    print(total)
