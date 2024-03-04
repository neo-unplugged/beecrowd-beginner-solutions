# test cases
animals = {
    'C': 0,
    'R': 0,
    'S': 0
}

N = int(input())
for i in range(N):
    amount, item = input().split(" ")
    animals[item] += int(amount)

total_animals = sum(animals.values())

print("Total: {} cobaias".format(total_animals))
print("Total de coelhos: {}".format(animals['C']))
print("Total de ratos: {}".format(animals['R']))
print("Total de sapos: {}".format(animals['S']))
print("Percentual de coelhos: {:.2f} %".format((animals['C'] / total_animals) * 100))
print("Percentual de ratos: {:.2f} %".format((animals['R'] / total_animals) * 100))
print("Percentual de sapos: {:.2f} %".format((animals['S'] / total_animals) * 100))
