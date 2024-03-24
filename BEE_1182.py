L = int(input())  # Line number
T = input()

M = [[0.0] * 12] * 12
result = 0

for i in range(12):
    for j in range(12):
        M[i][j] = float(input())
        if j == L:
            result += M[i][j]

print('{}'.format(result)) if M == 'S' else print('{:.1f}'.format(result//12))
