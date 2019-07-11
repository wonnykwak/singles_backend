import sqlite3
import json
from flask import Flask, g, request
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

@app.route("/api/moves", methods=["post"])
def logMove():
    with get_cur() as c:
        data = request.json
        c.execute( "INSERT INTO moves VALUES ({id}, {move}, '{type}', '{feedback}')".format(**data) )

        get_db().commit()

        return "", 200

@app.route("/api/reset")
def reset():
    sql_delete_moves_table = """ DROP TABLE IF EXISTS moves """
    sql_create_moves_table = """ CREATE TABLE IF NOT EXISTS moves (
                                    id INTEGER NOT NULL,
                                    move INTEGER NOT NULL,
                                    type TEXT NOT NULL,
                                    feedback TEXT,
                                    PRIMARY KEY (id, move)
                                ); """
    with get_cur() as c:
        c.execute(sql_delete_moves_table)
        c.execute(sql_create_moves_table)

    return ""

@app.route("/api/moves", methods=["get"])
def readMoves():
    with get_cur() as c:
        rows = c.execute("SELECT * FROM moves").fetchall()
        return json.dumps(rows)

@app.route("/api/moves/<int:id>", methods=["get"])
def readMovesForId(id):
    with get_cur() as c:
        rows = c.execute(f"SELECT * FROM moves WHERE id={id}").fetchall()
        return json.dumps(rows)

if __name__ == '__main__': 
    app.run(debug=True, host="0.0.0.0", port=4000)