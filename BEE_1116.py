N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    try:
        result = x/y
        print("{:.1f}".format(result))
    except ZeroDivisionError:
        print("divisao impossivel")
