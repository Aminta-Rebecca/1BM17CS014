
import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
conn.execute("DROP TABLE IF EXISTS EMPLOYEE")
try:
    conn.execute("CREATE TABLE EMPLOYEE(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL)");

    print ("Table created successfully")
except:
    conn.rollback()
try:    
    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (1, 'Chandana', 32, 'California', 20000.00 )");

    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (2, 'Apeksha', 25, 'Texas', 15000.00 )");

    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (3, 'Irene', 23, 'London', 20000.00 )");

    conn.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (4, 'Ruhen', 25, 'Netherlands', 65000.00 )");


    conn.commit()
except:
    conn.rollback()
    
print ("Records created successfully")

cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEE")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")

try:
    conn.execute("UPDATE EMPLOYEE set SALARY = 25000.00 where ID = 1")
    conn.commit()
except:
    conn.rollback()
print ("Table has been updated")

cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEE")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

print ("Operation done successfully")
try:
    conn.execute("DELETE from EMPLOYEE where ID = 2;")
    conn.commit()
except:
    conn.rollback()    
print ("Total number of rows deleted :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from EMPLOYEE")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
   print ("Operation done successfully")
conn.close()
