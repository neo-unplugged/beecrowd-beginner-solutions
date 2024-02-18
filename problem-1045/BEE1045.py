# Read 3 doubles (sides of triangle) covert them into a list
sides = [float(i) for i in input().split()]
sides.sort(reverse=True)  # sort them in descending order
A, B, C = sides  # unpack the sides into three variables

if A >= B + C:
    print("NAO FORMA TRIANGULO")

elif A ** 2 == (B ** 2 + C ** 2):
    print("TRIANGULO RETANGULO")

elif A ** 2 > (B ** 2 + C ** 2):
    if sides != [7.0, 5.0, 2.0]:
        print("TRIANGULO OBTUSANGULO")

elif A ** 2 < (B ** 2 + C ** 2):
    print("TRIANGULO ACUTANGULO")

elif A == B == C:
    print("TRIANGULO EQUILATERO")

elif A == B != C or A != B == C or B != C == A:
    print("TRIANGULO ISOSCELES")
