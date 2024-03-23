T = int(input())

for i in range(T):
    N = int(input())
    n1, n2 = 0, 1
    nth = 0
    for j in range(N+1):
        if j == N:
            print("Fib(%d) = %d" % (j, nth))
        n1 = n2
        n2 = nth
        nth = n1 + n2
