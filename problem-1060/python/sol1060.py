# get 6 numbers
input_count = 6
count = 0

while input_count > 0:
    count += 1 if float(input().strip()) > 0 else 0
    input_count -= 1

print("{} valores positivos".format(count))
