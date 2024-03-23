X = int(input())
Y = int(input())
total = 0

if Y < X:
    temp = Y
    Y = X
    X = temp

for i in range(X+1, Y):
    if i % 2 != 0:
        total += i
print(total)
