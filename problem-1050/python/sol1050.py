# dial destination
dials = {
    61: "Brasilia", 71: "Salvador", 11: "Sao Paulo", 21: "Rio de Janeiro", 32: "Juiz de Fora", 19: "Campinas",
    27: "Vitoria", 31: "Belo Horizonte"
}
ddd = int(input())  # get the ddd input
print("DDD nao cadastrado") if dials.get(ddd) is None else print(dials.get(ddd))  # get corresponding name
