class Employee:
    __organization = "somewhere"

    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary

    def display_detail(self):