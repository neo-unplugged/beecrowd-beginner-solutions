# income
salary = float(input())
tax = 0

if 0 <= salary <= 2000:
    print("Isento")
if 0 <= salary < 2000:
    tax = (salary - 2000) * (8.0 / 100)


print("$R %.2f" % tax)
