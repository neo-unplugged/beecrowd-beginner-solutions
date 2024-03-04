# number of test cases
N = int(input())
for i in range(N):
    x, y, z = map(float, input().split())
    mean = (x * 2 + y * 3 + z * 5) / (2 + 3 + 5)
    print("%.1f" % mean)
