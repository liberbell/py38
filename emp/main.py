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

employee_denvor = Employee("Denvor", "HR", 67000)
employee_denvor.display_detail()