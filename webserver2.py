import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
 
    return None
def create_table(conn, create_table_sql, add_values_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        c.execute(add_values_sql)
        array = c.execute("SELECT id, name, name_of_advice, name_of_move, used_advice from projects")
        #array2 = c.execute("SELECT id, text, priority, status_id, project_id, begin_date, end_date,  from actions")
        for row in array:
            print ("ID = ", row[0])
            print ("NAME = ", row[1])
            print ("ADVICE = ", row[2])
            print ("USER MOVE = ", row[3])
            print ("DID USER USE ADVICE = ", row[4], "\n")

        #for row2 in array2:
         #   print ("ID = ", row2[0])
          #  print ("NAME = ", row2[1])
           # print ("PRIORITY  = ", row2[2])
            #print ("STATUS_ID = ", row2[3], "\n")
            #print ("PROJECT_ID = ", row2[0])
            #print ("BEGIN_DATE = ", row2[1])
            #print ("END_DATE = ", row2[2])
        
    except Exception as e:
        print(create_table_sql)
        print(e)


def main():
    database = "database.db"
    
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        name_of_advice text,
                                        name_of_move text,
                                        used_advice boolean
                                    );"""
    sql_add_projects = ''' INSERT INTO projects (id, name, name_of_advice, name_of_move, used_advice)
                           VALUES (21, 'Eduardo', 'dont put it next to the 2', 'next to 2', 'False');'''
 
    #sql_create_actions_table = """CREATE TABLE IF NOT EXISTS actions (
                                    #id integer PRIMARY KEY,
                                    #name text NOT NULL,
                                    #priority integer,
                                    #status_id integer NOT NULL,
                                    #project_id integer NOT NULL,
                                    #begin_date text NOT NULL,
                                    #end_date text NOT NULL
                                #);"""

    #sql_add_actions = ''' INSERT INTO actions (id, name, priority, status_id, project_id, begin_date, end_date)
                       # VALUES (22, 'bob', 1, 3, 5, 'january', 'december');'''

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_projects_table, sql_add_projects)
       # create_table(conn, sql_create_actions_table, sql_add_actions)

    else:
        print("Error! cannot create the database connection.")
    
@app.route("/home")
def bla():
    return "Welcome to my world"



if __name__ == '__main__':
    main()
    app.run(debug=True, host = "0.0.0.0", port= 4000) 

