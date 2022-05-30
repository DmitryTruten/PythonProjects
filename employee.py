# 11-3 Employee
class Employee:
    def __init__(self, name, surname, year_salary):
        self.name = name
        self.surname = surname
        self.year_salary = year_salary

    def give_raise(self, raised_salary=5000):
        self.year_salary += raised_salary

    def show_employee_info(self):
        print(f"Name - {self.name.title()}\n"
              f"Surname - {self.surname.title()}\n"
              f"Year salary - {self.year_salary}$\n")


me = Employee('dima', 'truten', 0)
me.show_employee_info()
me.give_raise()
me.show_employee_info()