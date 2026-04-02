class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        overtime_rate = 1.5
        standard_hours = 40

        if self.hours_worked > standard_hours:
            overtime_hours = self.hours_worked - standard_hours
            regular_pay = standard_hours * self.hourly_rate
            overtime_pay = overtime_hours * self.hourly_rate * overtime_rate
            total_salary = regular_pay + overtime_pay
        else:
            total_salary = self.hours_worked * self.hourly_rate

        return total_salary


def main():
    print("=== Payroll System ===")

    employees = []
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print(f"\nEmployee {i+1}")
        name = input("Enter name: ")
        hours = float(input("Enter hours worked: "))
        rate = float(input("Enter hourly wage: "))

        emp = Employee(name, hours, rate)
        employees.append(emp)

    print("\n=== Salary Details ===")
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"{emp.name} => Salary: ₹{salary:.2f}")


if __name__ == "__main__":
    main()