A = []

for i in range(100):
    A.append(float(input()))

for num in range(len(A)):
    print("A[%d] = %.1f" % (num, A[num])) if A[num] <= 10 else None
