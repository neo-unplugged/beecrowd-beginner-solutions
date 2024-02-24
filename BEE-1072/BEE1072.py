N = int(input())
ins = 0

for i in range(N):
    num = int(input())
    if 10 <= num <= 20:
        ins += 1

print("{} in".format(ins))
print("{} out".format(N-ins))
