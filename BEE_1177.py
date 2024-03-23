T = int(input())
N = []
j = 0

for i in range(1000):
    if j > T-1:
        j = 0
    N.insert(i, j)
    print("N[%d] = %d" % (i, N[i]))
    j += 1
