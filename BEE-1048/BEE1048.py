# take user salary as input
salary = float(input())
new_salary = salary
percentage = 0

if 0 <= salary <= 400.00:
    percentage = 15
    new_salary += (salary * .15)

elif 400.01 <= salary <= 800.00:
    percentage = 12
    new_salary += (salary * .12)

elif 800.01 <= salary <= 1200.00:
    percentage = 10
    new_salary += (salary * .10)

elif 1200.01 <= salary <= 2000.00:
    percentage = 7
    new_salary += (salary * .07)

elif salary > 2000.00:
    percentage = 4
    new_salary += (salary * .04)

print("Novo salario: %.2f" % new_salary)
print("Reajuste ganho: %.2f" % (new_salary - salary))
print("Em percentual: %d %%" % percentage)