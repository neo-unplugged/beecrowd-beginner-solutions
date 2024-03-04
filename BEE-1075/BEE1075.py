# read an integer N
N = int(input())

for i in range(1, 10000):
    print(i) if i % N == 2 else None  # print only the values that divided by n spits out remainder 2
