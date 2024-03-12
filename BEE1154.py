ages = []

while True:
    n = int(input())
    if n < 0:
        break
    ages.append(n)
print("{:.2f}".format(sum(ages)/len(ages)))
