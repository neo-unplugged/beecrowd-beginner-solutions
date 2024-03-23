# while True:
# options = dict(zip(["Alcohol", "Gasoline", "Diesel"], [0, 0, 0]))
options = dict(zip([1, 2, 3], [0, 0, 0]))

while True:
    option = int(input())
    if option in options.keys():
        options[option] += 1
    elif option == 4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: {}\nGasolina: {}\nDiesel: {}".format(*options.values()))
