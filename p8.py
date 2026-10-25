class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def yearly_pay(self):
        return self.monthly_salary * 12


class Manager(Employee):
    def __init__(self, name, monthly_salary, bonus):
        super().__init__(name, monthly_salary)
        self.bonus = bonus

    def yearly_pay(self):
        return super().yearly_pay() + self.bonus


emp = Employee("Ali", 50000)
mgr = Manager("Sara", 80000, 100000)

print(emp.name, emp.yearly_pay())
print(mgr.name, mgr.yearly_pay())
print(isinstance(emp, Employee), isinstance(emp, Manager))
print(isinstance(mgr, Employee), isinstance(mgr, Manager))
