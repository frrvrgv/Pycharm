import sqlite3
#create a connection to the data base
connection = sqlite3.connect('studentrepo.db')
#cursor object
cursor_obj = connection.cursor()



#insert data to the employee table
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("John Deo","Four",75,"female")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Max Ruin","Three",85,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Arnold","Three",55,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Krish Star","Four",60,"female")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("John Mike","Four",60,"female")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Alex John","Four",55,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("My John Rob","Five",78,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Asruid","Five",85,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Tes Qry","Five",85,"male")""")
cursor_obj.execute("""INSERT INTO studentrepo(Name,Class,Mark,Gender) VALUES("Big John","Four",55,"female")""")



cursor = cursor_obj.execute("select * from studentrepo")
for row in cursor:
    print(row)

import mysql.connector
mydb = mysql.coneector.connect(
    host = "localhost",
    user = "myusername"

)
update_query = """ 
                   UPDATE studentrepo 
                   SET Mark = 55
                   WHERE Mark = 75 
"""
try:
    cursor.execute(update_query)
    connection.commit()
    print("updated")
except:
    print("error")

cursor.close()
connection.close()
