x = int(input())
total = 0

while True:
    z = int(input())
    if z > x:
        break

num = 0
for i in range(x, z+1):
    if total > z:
        break
    total += i
    num += 1
print(num)
