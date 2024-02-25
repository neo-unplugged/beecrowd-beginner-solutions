N = int(input())

for _ in range(1, N+1):
    print("{}^{} = {}".format(_, 2, _ ** 2)) if _ % 2 == 0 else None
