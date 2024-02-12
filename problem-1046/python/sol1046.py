# get the start and end time
start_time, end_time = (int(i) for i in input().split())

# calculate duration
duration = end_time - start_time

# if duarion negative or zero add 24
if duration <= 0:
    duration += 24
print("O JOGO DUROU %d HORA(S)" % duration)
