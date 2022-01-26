import employee

if __name__ == "__main__":
    print("**********", __name__)
    employee_denvor = employee.Employee("Denvor", "HR", 67000)
    employee_denvor.display_detail()