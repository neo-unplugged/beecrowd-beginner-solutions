N = int(input())

for i in range(N):
    x = int(input())

    if all(map(lambda num: x % num, range(2, x))):
        print("%d eh primo" % x)
    else:
        print("%d nao eh primo" % x)
