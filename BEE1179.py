par = []
impar = []
nums = []

for _ in range(15):
    nums.append(int(input()))

for num in nums:
    if num % 2:
        impar.append(num)
    else:
        par.append(num)

    if len(par) == 5:
        for item in enumerate(par):
            print("par[{}] = {}".format(*item))
        par = []

    if len(impar) == 5:
        for item in enumerate(impar):
            print("impar[{}] = {}".format(*item))
        impar = []

if len(impar) > 0:
    for item in enumerate(impar):
        print("impar[{}] = {}".format(*item))

if len(par) > 0:
    for item in enumerate(par):
        print("par[{}] = {}".format(*item))
