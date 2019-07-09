import sqlite3
from flask import Flask
db_filename = 'datastorage.db'
connect = sqlite3.connect(db_filename)

c = connect.cursor()

c.execute('CREATE TABLE IF NOT EXISTS task (id number PRIMARY KEY, priority integer, details text, status text)')
c.execute("INSERT INTO task (id,priority,details,status) \
      VALUES (1,22,'ABC','YES' )")
cursor = c.execute("SELECT id,priority,details,status from task")
for row in cursor:
   print ("ID = ", row[0])
   print ("PRIORITY = ", row[1])
   print ("DETAILS = ", row[2])
   print ("STATUS = ", row[3], "\n")
connect.commit()
connect.close()