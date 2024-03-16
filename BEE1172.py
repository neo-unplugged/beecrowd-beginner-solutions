x = []

for i in range(3):
    num = int(input())
    num = 1 if num <= 0 else num
    x.append(num)
    
for j in range(len(x)):
    print("X[%d] = %d" % (j, x[j]))
