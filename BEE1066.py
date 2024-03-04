input_count = 5

positive_count = 0
negative_count = 0
even_count = 0

for i in range(input_count):
    num = int(input())
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    even_count += 1 if num % 2 == 0 else 0

print("{} valor(es) par(es)".format(even_count))
print("{} valor(es) impar(es)".format(input_count - even_count))
print("{} valor(es) positivo(s)".format(positive_count))
print("{} valor(es) negativo(s)".format(negative_count))
