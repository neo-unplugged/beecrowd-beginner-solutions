N = []

for i in range(20):
    N.append(int(input()))
N.reverse()

for i in range(len(N)):
    print("N[%d] = %d" % (i, N[i]))
