while True:
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        print("primeiro")
    elif x > 0 > y:
        print("quarto")
    elif x < 0 < y:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        break
