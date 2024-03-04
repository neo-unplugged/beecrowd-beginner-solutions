# read an integer value
X = int(input())

for i in range(1, X+1):
    print(i) if i % 2 != 0 else None
