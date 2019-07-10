import sqlite3
from flask import Flask, g
from contextlib import closing

app = Flask(__name__, static_folder='public')

DATABASE = "database.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_cur():
    return closing(get_db().cursor())

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def main():
    sql_delete_moves_table = """ DROP TABLE IF EXISTS moves """
    sql_create_moves_table = """ CREATE TABLE IF NOT EXISTS moves (
                                    id INTEGER NOT NULL,
                                    move INTEGER NOT NULL,
                                    type TEXT NOT NULL,
                                    advice TEXT,
                                    PRIMARY KEY (id, move)
                                ); """

    sql_add_move = ''' INSERT INTO moves (id, move, type, advice)
                           VALUES (21, 21, 'dont put it next to the 2', 'next to 2');'''

    with app.app_context():
        with get_cur() as c:
            c.execute(sql_delete_moves_table)
            c.execute(sql_create_moves_table)

@app.route("/api/saveMove")
def saveMove():
    with get_cur() as c:
        data = {
            "id": 0,
            "move": 0,
            "type": "good",
            "advice": "bad"
        }

        c.execute( "INSERT INTO moves (id, move, type, advice) VALUES ({id}, {move}, '{type}', '{advice}')".format(**data) )

        get_db().commit()

        return "", 200


@app.route("/api/readMove")
def readMove():
    with get_cur() as c:
        array = c.execute("SELECT * FROM moves").fetchall()
        for row in array:
            print(row)

        return "Welcome to my world"

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
    
    app.run(debug=True, host="0.0.0.0", port=4000)
