from employee import Employee, create_employee

if __name__ == "__main__":
    print("**********", __name__)
    employee_denvor = create_employee("Denvor", "HR", 67000)
    employee_denvor.display_detail()
    employee_jessica = create_employee("Jessica", "Sales", 76000)
    employee_jessica.display_detail()