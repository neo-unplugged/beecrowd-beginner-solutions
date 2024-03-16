T = float(input())
N = []

for i in range(100):
    N.insert(i, T)
    print("N[%d] = %.4f" % (i, N[i]))
    T /= 2
