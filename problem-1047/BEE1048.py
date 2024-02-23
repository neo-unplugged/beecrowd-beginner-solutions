# read start time and end time
h1, m1, h2, m2 = map(int, input().split())

h = h2 - h1
m = m2 - m1

# keep in mind only case when both
# h and m greater than 0 we pass
# either of them greater than 0 we pass

if h == 0 and m == 0:
    h += 24

elif h == 0 and m < 0:
    h += 23
    m += 60

elif h < 0 and m == 0:
    h += 24

elif h > 0 > m:
    h -= 1
    m += 60

elif h < 0 < m:
    h += 23

elif h < 0 and m < 0:
    h += 23
    m += 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
