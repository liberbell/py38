class Employee:
    __organization = "somewhere"

    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def display_detail(self):
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Salary: {self.__salary}")
        print(f"Organization: {Employee.__organization}")

def create_employee(name, department, salary):
    employee = Employee(name, department, salary)
    # employee = employee.Employee(name, department, salary)
    return employee

print("In employee **********", __name__)