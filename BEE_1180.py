# number of elements
N = int(input())

# elements
X = list(map(int, input().split()[:N]))

min_value = min(X)
min_value_index = X.index(min_value)

print("Menor valor: {}".format(min_value))
print("Posicao: {}".format(min_value_index))
