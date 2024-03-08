# I=1 J=7
# I=1 J=6
# I=1 J=5
# I=3 J=9
# I=3 J=8
# I=3 J=7
# ...
# I=9 J=15
# I=9 J=14
# I=9 J=13

x = 7   # initial J value
for i in range(1, 10, 2):
    for j in range(x, x-3, -1):     # to 3 values down
        print("I={} J={}".format(i, j))
    x += 2      # after each iteration increment J start index by 2



