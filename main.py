from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/home")
def bla():
    return "Welcome to my"

@app.route("/heeelo")
def bla2():
    return "hi"

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0", port= 4000) 