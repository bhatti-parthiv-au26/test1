# detabase

import sqlite3
conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute("""CREATE TABLE employee_master(
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT,
    employee_address TEXT,
    employee_phone TEXT,
    employee_email TEXT,
    employee_dob TEXT,
    employee_doj TEXT,
    employee_designation TEXT,
    employee_department TEXT,
    employee_salary INTEGER,
    employee_status TEXT
)""")

c.execute("""CREATE TABLE salary_master(
    salary_id INTEGER PRIMARY KEY,
    salary_amount INTEGER,
    salary_date TEXT,
    salary_status TEXT
)""")

c.execute("""CREATE TABLE attendance_master(
    attendance_id INTEGER PRIMARY KEY,
    attendance_date TEXT,
    attendance_status TEXT
)""")

c.execute("""CREATE TABLE employee_salary(
    employee_id INTEGER,
    salary_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employee_master(employee_id),
    FOREIGN KEY(salary_id) REFERENCES salary_master(salary_id)
)""")

c.execute("""CREATE TABLE employee_attendance(
    employee_id INTEGER,
    attendance_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employee_master(employee_id),
    FOREIGN KEY(attendance_id) REFERENCES attendance_master(attendance_id)
)""")

c.execute("""CREATE TABLE employee_attendance_report(
    employee_id INTEGER,
    attendance_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employee_master(employee_id),
    FOREIGN KEY(attendance_id) REFERENCES attendance_master(attendance_id)
)""")

c.execute("""CREATE TABLE employee_salary_report(
    employee_id INTEGER,
    salary_id INTEGER,
    FOREIGN KEY(employee_id) REFERENCES employee_master(employee_id),
    FOREIGN KEY(salary_id) REFERENCES salary_master(salary_id)
)""")

conn.commit()
conn.close()
print("""
1. Create Employee
2. Create Salary
3. Create Attendance
4. Update Employee
5. Update Salary
6. Update Attendance
7. Delete Employee
8. Delete Salary
9. Delete Attendance
10. Read Employee
11. Read Salary
12. Read Attendance
13. Read Employee Salary
14. Read Employee Attendance
15. Read Employee Attendance Report
16. Read Employee Salary Report
""")

print("Enter your choice: ")


#  employe reports

class Employee:
    def __init__(self, name, email, mobile, address, city, state, country):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.city = city
        self.state = state
        self.country = country

    def __str__(self):
        return f"{self.name} {self.email} {self.mobile} {self.address} {self.city} {self.state} {self.country}"

    def __repr__(self):
        return f"{self.name} {self.email} {self.mobile} {self.address} {self.city} {self.state} {self.country}"


class Salary:
    def __init__(self, employeeid, basic_salary, da, hra, kit_allowance, pf, pt, gross_salary):
        self.employeeid = employeeid
        self.basic_salary = basic_salary
        self.da = da
        self.hra = hra
        self.kit_allowance = kit_allowance
        self.pf = pf
        self.pt = pt
        self.gross_salary = gross_salary

    def __str__(self):
        return f"{self.employeeid} {self.basic_salary} {self.da} {self.hra} {self.kit_allowance} {self.pf} {self.pt} {self.gross_salary}"

    def __repr__(self):
        return f"{self.employeeid} {self.basic_salary} {self.da} {self.hra} {self.kit_allowance} {self.pf} {self.pt} {self.gross_salary}"


class Attendance:
    def __init__(self, employeeid, datetime, in_out, remarks):
        self.employeeid = employeeid
        self.datetime = datetime
        self.in_out = in_out
        self.remarks = remarks

    def __str__(self):
        return f"{self.employeeid} {self.datetime} {self.in_out} {self.remarks}"

    def __repr__(self):
        return f"{self.employeeid} {self.datetime} {self.in_out} {self.remarks}"


def create_employee():
    name = input("Enter name: ")
    email = input("Enter email: ")
    mobile = input("Enter mobile: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    country = input("Enter country: ")
    employee = employee(name, email, mobile, address, city, state, country)
    return employee


def create_salary():
    employeeid = input("Enter employeeid: ")
    basic_salary = input("Enter basic salary: ")
    da = input("Enter da: ")
    hra = input("Enter hra: ")
    kit_allowance = input("Enter kit allowance: ")
    pf = input("Enter pf: ")
    pt = input("Enter pt: ")
    gross_salary = input("Enter gross salary: ")
    salary = salary(employeeid, basic_salary, da, hra, kit_allowance, pf, pt, gross_salary)
    return salary


def create_attendance():
    employeeid = input("Enter employeeid: ")
    datetime = input("Enter datetime: ")
    in_out = input("Enter in/out: ")
    remarks = input("Enter remarks: ")
    attendance = attendance(employeeid, datetime, in_out, remarks)
    return attendance





def create_employee_master():
    employee = create_employee()
    print(employee)
    return employee


def create_salary_master():
    salary = create_salary()
    print(salary)
    return salary


def create_attendance_master():
    attendance = create_attendance()
    print(attendance)
    return attendance

# updete employee
def update_employee():
    employee = create_employee()
    print(employee)
    return employee


def update_salary():
    salary = create_salary()
    print(salary)
    return salary


def update_attendance():
    attendance = create_attendance()
    print(attendance)
    return attendance


def update_employee_master():
    pass


def update_salary_master():
    pass


def update_attendance_master():
    pass


def delete_employee_master():
    pass


def delete_salary_master():
    pass


def delete_attendance_master():
    pass


def read_employee_master():
    pass


def read_salary_master():
    pass


def read_attendance_master():
    pass


def read_employee_salary():
    pass


def read_employee_attendance():
    pass


def read_employee_attendance_report():
    pass


def read_employee_salary_report():
    pass

