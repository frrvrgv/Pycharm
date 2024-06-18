import sqlite3
#create a connection to the data base
connection = sqlite3.connect('employee.db')
#cursor object
cursor_obj = connection.cursor()


#insert data to the employee table
cursor_obj.execute("""INSERT INTO employee(Employeename,EmployeeID,EmployeeBU,EmployeeSalary) VALUES("John",1001,"HR",7897687)""")
cursor_obj.execute("""INSERT INTO employee(Employeename,EmployeeID,EmployeeBU,EmployeeSalary) VALUES("Sowmi",1002,"IT",9789360)""")
cursor_obj.execute("""INSERT INTO employee(Employeename,EmployeeID,EmployeeBU,EmployeeSalary) VALUES("Rechu",1003,"Telecom",8056632)""")
cursor_obj.execute("""INSERT INTO employee(Employeename,EmployeeID,EmployeeBU,EmployeeSalary) VALUES("Bran",1004,"Telecom",9791902)""")
cursor_obj.execute("""INSERT INTO employee(Employeename,EmployeeID,EmployeeBU,EmployeeSalary) VALUES("Johnson",1005,"HR",4567893)""")

cursor = cursor_obj.execute("select * from employee")
for row in cursor:
    print(row)

cursor_obj.commit()
cursor_obj.close()