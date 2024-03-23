N = int(input())

for i in range(N):
    x = int(input())
    divisors = [j for j in range(1, x) if x % j == 0]
    total = sum(divisors)

    if total == x:
        print("{} eh perfeito".format(x))
    else:
        print("{} nao eh perfeito".format(x))
