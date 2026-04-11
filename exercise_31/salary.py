from employees import Employee

employee = Employee("Ibrahim", "Kiri", 50000)

print(employee.annual_salary)  # 50000

employee.give_raise()
print(employee.annual_salary)  # 55000

employee.give_raise(10000)
print(employee.annual_salary)  # 65000