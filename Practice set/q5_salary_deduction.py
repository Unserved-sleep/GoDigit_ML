basic_salary: int = int(input())
late_day: int = int(input())
absence: int = int(input())

if late_day > 5:
    basic_salary -= basic_salary * 0.05
elif late_day > 10:
    basic_salary -= basic_salary * 0.1
if absence > 2:
    basic_salary -= basic_salary * 0.05
print(basic_salary)