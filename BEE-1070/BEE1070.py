# read an integer value
X = int(input())

count = 0
while count < 6:
    if (X % 2) == 1:
        print(X)
        count += 1
    X += 1
