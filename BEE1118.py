while True:
    total = 0
    count = 0
    while count != 2:
        num = float(input())
        if 0 <= num <= 10:
            total += num
            count += 1
        else:
            print("nota invalida")
    print("media = {:.2f}".format(total / count))

    newCalc = 0

    while True:
        print("novo calculo (1-sim 2-nao)")
        newCalc = int(input())
        if newCalc == 1 or newCalc == 2:
            break

    if newCalc == 2:
        break
