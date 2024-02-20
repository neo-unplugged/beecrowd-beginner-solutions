times = [int(i) for i in input().split()]
start_hour, start_min, end_hour, end_min = times

hours = end_hour - start_hour
minutes = end_min - start_min

if minutes < 0:
    hours -= 1
    minutes += 60

if hours <= 0 :
    hours += 24
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hours, minutes))
