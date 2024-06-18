import sqlite3
#create a connection to the data base
connection = sqlite3.connect('Pysician.db')
#cursor object
cursor_obj = connection.cursor()
table1 = """CREATE TABLE Pysician(
           employeeid INT
           Name VARCHAR(255) NOT NULL,
           Position VARCHAR(100) NOT NULL,
           ssn INT);"""
cursor_obj.execute(table1)


cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(2, "Elliot_Reid", "attending_pysician", 22222222)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(3, "Christoper_Turk", "Surgical_attending_pysician" , 33333333)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(4, "Percival_cox", "senior_attending_pysician", 44444444)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(5, "Bob_Kelsa", "Head_Cheif_of_Medicine", 55555555)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(6, "Todd_Quinlan", "Surgical_attending_pysician" , 66666666)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(7, "John_Wen", "Surgical_attending_pysician", 777777777,)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(8, "Keith_Dudemeister", "MD_Resident", 88888888)""")
cursor_obj.execute("""INSERT INTO Pysician(employee_id, Name, Position, ssn) VALUES(9, "Molly_clock", "Attending_psychiatrist", 99999999)""")

cursor = cursor_obj.execute("select * from Pysician")
for row in cursor:
    print(row)

table2 = """CREATE TABLE department (
           Departmentid INT
           Name VARCHAR(255) NOT NULL,
           Head INT);"""
cursor_obj.execute(table2)


cursor_obj.execute("""INSERT INTO department(Departmentid, Name,Head) VALUES(1, "General medicine", 4)""")
cursor_obj.execute("""INSERT INTO department(Departmentid, Name,Head) VALUES(2,"surgery", 7)""")
cursor_obj.execute("""INSERT INTO department(Departmentid, Name,Head) VALUES(3, "psychiatry", 9)""")

cursor = cursor_obj.execute("select * from department")
cursor = cursor_obj.execute("SELECT d.Name AS department, p.Name AS Pysician")
for row in cursor:
    print(row)

cursor_obj.commit()
cursor_obj.close()
