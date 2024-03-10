count = 0
total = 0

while count != 2:
    num = float(input())
    if 0 <= num <= 10:
        total += num
        count += 1
    else:
        print("nota invalida")
print("media = {:.2f}".format(total/count))
