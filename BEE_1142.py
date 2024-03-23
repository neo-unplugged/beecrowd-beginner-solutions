N = int(input())
num = 1

while N > 0:
    for i in range(4):
        print(num, end=" ") if num % 4 != 0 else print("PUM")
        num += 1
    N -= 1
