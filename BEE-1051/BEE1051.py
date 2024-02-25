# income
salary = float(input())
tax = 0

if 0 <= salary <= 2000:
    print("Isento")

elif 2000 < salary <= 3000.00:
    tax = (salary - 2000) * (8.0 / 100)
    print("R$ %.2f" % tax)

elif 3000 < salary <= 4500.00:
    tax = 1000 * (8.0 / 100) + (salary - 3000) * (18.0 / 100)
    print("R$ %.2f" % tax)

elif salary > 4500.00:
    tax = 1000 * (8.0 / 100) + 1500 * (18.0 / 100) + + (salary - 4500) * (28.0 / 100)
    print("R$ %.2f" % tax)
