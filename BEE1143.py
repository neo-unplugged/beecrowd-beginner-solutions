N = int(input())


for i in range(1, N+1):
    for j in range(2):
        print("{} {} {}".format(i, (i**2)+j, (i ** 3)+j))
