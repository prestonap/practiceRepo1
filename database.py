import sqlite3 
connection = sqlite3.connect('sampleDB.db')
cursor = connection.cursor()
cursor.execute("SELECT*FROM SampleTable")
#print(cursor.fetchall())
cursor.execute("SELECT*FROM SampleTable WHERE year > 2000")
#print(cursor.fetchall())
cursor.execute("SELECT*FROM SampleTable WHERE Color = 'Blue'")
print(cursor.fetchall())

#Deleting data in a database with 'cursor.execute()'
#DELETE FROM <tableName> WHERE <columnName> = <value>

#EX   DELETE FROM movies WHERE title = "Wolf of Wallstreet"
cursor.execute("DELETE FROM sampleTable WHERE color = 'Blue' ")