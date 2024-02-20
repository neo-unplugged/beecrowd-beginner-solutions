# credit user given to bank
N = float(input())

units = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
credit = int(N * 100)  # turn the credit into cents and trim the changes

print("NOTAS:")
for i in units:
    count = credit // i
    credit %= i
    if units.index(i) == 6:
        print("MOEDAS:")
    print("{} nota(s) de R$ {:.2f}".format(count, i/100))
