input_count = 5

cnt = 0
for i in range(input_count):
    num = int(input())
    cnt += 1 if num % 2 == 0 else 0

print("{} valores pares".format(cnt))
