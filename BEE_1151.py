N = int(input())
n1, n2 = 0, 1
nth = 0

for num in range(N):
    if num == N-1:
        print(nth)
    else:
        print(nth, end=" ")
    n1 = n2
    n2 = nth
    nth = n1 + n2
