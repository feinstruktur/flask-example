import flask
import random
import sqlite3

app = flask.Flask(__name__)

db = sqlite3.connect('./test.sqlite')
conn = db.cursor()
conn.row_factory = sqlite3.Row

@app.route("/plaintext")
def plaintext():
    return "Hello, world!"

@app.route("/json")
def json():
    return flask.jsonify(**{
        "array": [1, 2, 3],
        "dict": {"one": 1, "two": 2, "three": 3},
        "int": 42,
        "string": "test",
        "double": 3.14,
        "null": None
    })

@app.route("/sqlite-fetch")
def sqlite_fetch():
    id = random.randint(1, 3)
    r = conn.execute("select * from users where id = ?", (id,)).fetchone()
    print 'res:', r
    if r is not None:
        d = dict(zip(r.keys(), r))
        return flask.jsonify(d)
    else:
        flask.abort(404)
    

if __name__ == "__main__":
    app.run(port=8137)
