class Employee:

    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"Employee(emp_id={self.emp_id}, name={self.name}, age={self.age}, salary={self.salary})"

def main():
    emp_data = [
        Employee(161E90, "Raman", 41, 56000),
        Employee(161F91, "Himadri", 38, 67500),
        Employee(161F99, "Jaya", 51, 82100),
        Employee(171E20, "Tejas", 30, 55000),
        Employee(171G30, "Ajay", 45, 44000),
    ]
    print("Employee Table:")
    print("Employee ID Name Age Salary (PM)")
    for emp in emp_data:
        print(emp)

    print("\nSelect sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_parameter = int(input("Enter sorting parameter: "))

    if sorting_parameter == 1:
        emp_data.sort(key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        emp_data.sort(key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        emp_data.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter!")
        return

    print("\nSorted Employee Table:")
    print("Employee ID Name Age Salary (PM)")
    for emp in emp_data:
        print(emp)

if __name__ == "__main__":
    main()
