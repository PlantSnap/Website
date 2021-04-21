import flask
import sqlite3
from flask import request

app = flask.Flask(__name__)

@app.route('/FlyingCows', methods=['GET'])
def hardware():
    connection = sqlite3.connect("FlyingCows.db")
    cursor = connection.cursor()

    id = request.args.get("id")
    results = cursor.execute("Select data From testData WHERE id = ?", (id,),)
    rows = results.fetchall()

    return(rows[0][0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
