# enter test cases  count
N = int(input())

for i in range(N):
    x, y = map(int, input().split(" "))
    if x > y:
        temp = x
        x = y
        y = temp
    result = 0
    for j in range(x+1, y):
        if j % 2 == 1:
            result += j
    print(result)
