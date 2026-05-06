class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_employee_info(self):
        return f"{self.name} - {self.role}"


class EmployeeDatabase:
    @staticmethod
    def save_employee(employee):
        print(f"Saving {employee.name} to database")


class EmployeeReportGenerator:
    @staticmethod
    def generate_report(employee):
        print(f"Generating report for {employee.name}")


emp = Employee("John Doe", "Developer")
print(emp.get_employee_info())
EmployeeDatabase.save_employee(emp)
EmployeeReportGenerator.generate_report(emp)