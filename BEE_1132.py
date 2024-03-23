x = int(input())
y = int(input())

if x > y:
    temp = x
    x = y
    y = temp

nums = list(range(x, y+1))


def filter_mult_13(num: int):
    if num % 13 != 0:
        return True
    else:
        return False


total = sum(filter(filter_mult_13, nums))
print(total)
