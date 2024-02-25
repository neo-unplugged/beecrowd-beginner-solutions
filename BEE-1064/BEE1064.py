input_count = 6
cnt = 0
avg = 0.0
total = 0

for i in range(input_count):
    num = float(input())
    if num > 0:
        cnt += 1
        total += num

avg = total / cnt

print("{} valores positivos".format(cnt))
print("{:.1f}".format(avg))
