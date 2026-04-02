import tkinter as tk
from tkinter import ttk, messagebox

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_details(self):
        overtime_rate = 1.5
        standard_hours = 40

        if self.hours_worked > standard_hours:
            overtime_hours = self.hours_worked - standard_hours
            regular_pay = standard_hours * self.hourly_rate
            overtime_pay = overtime_hours * self.hourly_rate * overtime_rate
        else:
            overtime_hours = 0
            regular_pay = self.hours_worked * self.hourly_rate
            overtime_pay = 0

        total_salary = regular_pay + overtime_pay
        return regular_pay, overtime_hours, overtime_pay, total_salary


class PayrollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Management System")
        self.root.geometry("900x550")
        self.root.configure(bg="#eef2f7")

        self.employees = []

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Payroll Management Dashboard", font=("Segoe UI", 18, "bold"), bg="#eef2f7")
        title.pack(pady=10)

        # Input Frame
        frame = tk.LabelFrame(self.root, text="Employee Entry", padx=10, pady=10)
        frame.pack(fill="x", padx=20, pady=10)

        tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Hours Worked").grid(row=0, column=2, padx=10)
        self.hours_entry = tk.Entry(frame)
        self.hours_entry.grid(row=0, column=3, padx=10)

        tk.Label(frame, text="Hourly Rate").grid(row=0, column=4, padx=10)
        self.rate_entry = tk.Entry(frame)
        self.rate_entry.grid(row=0, column=5, padx=10)

        add_btn = tk.Button(frame, text="Add Employee", command=self.add_employee, bg="#28a745", fg="white")
        add_btn.grid(row=0, column=6, padx=10)

        # Table
        columns = ("Name", "Hours", "Rate", "Regular Pay", "OT Hours", "OT Pay", "Total Salary")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=110)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#eef2f7")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Calculate Payroll", command=self.calculate_all, bg="#007bff", fg="white", width=20).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_selected, bg="#ffc107", width=20).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Clear All", command=self.clear_all, bg="#dc3545", fg="white", width=20).grid(row=0, column=2, padx=10)

        # Summary
        self.summary_label = tk.Label(self.root, text="Total Payroll: ₹0.00", font=("Segoe UI", 12, "bold"), bg="#eef2f7")
        self.summary_label.pack(pady=10)

    def add_employee(self):
        try:
            name = self.name_entry.get()
            hours = float(self.hours_entry.get())
            rate = float(self.rate_entry.get())

            if not name:
                raise ValueError

            emp = Employee(name, hours, rate)
            self.employees.append(emp)

            self.tree.insert("", "end", values=(name, hours, rate, "-", "-", "-", "-"))

            self.name_entry.delete(0, tk.END)
            self.hours_entry.delete(0, tk.END)
            self.rate_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Enter valid input")

    def calculate_all(self):
        total_payroll = 0

        for i, emp in enumerate(self.employees):
            reg, ot_hours, ot_pay, total = emp.calculate_details()
            total_payroll += total

            self.tree.item(self.tree.get_children()[i], values=(
                emp.name,
                emp.hours_worked,
                emp.hourly_rate,
                f"₹{reg:.2f}",
                ot_hours,
                f"₹{ot_pay:.2f}",
                f"₹{total:.2f}"
            ))

        self.summary_label.config(text=f"Total Payroll: ₹{total_payroll:.2f}")

    def delete_selected(self):
        selected = self.tree.selection()
        for item in selected:
            index = self.tree.index(item)
            self.tree.delete(item)
            del self.employees[index]

    def clear_all(self):
        self.tree.delete(*self.tree.get_children())
        self.employees.clear()
        self.summary_label.config(text="Total Payroll: ₹0.00")


if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()