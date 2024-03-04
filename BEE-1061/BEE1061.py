
str1, w1 = input().split(" ")
w1 = int(w1)
x1, y1, z1 = map(int, input().split(':'))
str2, w2 = input().split(" ")
w2 = int(w2)
x2, y2, z2 = map(int, map(str.strip, input().split(':')))


z = z2 - z1
y = y2 - y1
x = x2 - x1
w = w2 - w1


if z < 0:
    z += 60
    y -= 1

if y < 0:
    y += 60
    x -= 1

if x < 0:
    x += 24
    w -= 1


print("{} dia(s)".format(w))
print("{} hora(s)".format(x))
print("{} minuto(s)".format(y))
print("{} segundo(s)".format(z))
