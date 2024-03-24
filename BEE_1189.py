# operation to be performed
O = input()

M = [[0.0] * 12] * 12
result = 0
count = 0
for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
        if (i > j) and (i + j < 11):
            result += M[i][j]
            count += 1

if O == 'M':
    print('{:.1f}'.format(result / count))
else:
    print('{:.1f}'.format(result))
