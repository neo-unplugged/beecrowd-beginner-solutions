
while True:
    sum = 0
    M, N = map(int, input().split(" "))
    if M <= 0 or N <= 0:
        break
    if M > N:
        temp = N
        N = M
        M = temp
    for num in range(M, N+1):
        print(num, end=" ")
        sum += num
    print("Sum={}".format(sum))
