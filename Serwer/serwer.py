from flask import Flask, jsonify, render_template

import psycopg2

app = Flask(__name__)

def select_one():
    connection = psycopg2.connect(user="piotr",
            password="windows7",
            host="127.0.0.1",
            port="5432",
            database="pgs")

    cursor = connection.cursor()
    query = "SELECT number, date FROM data ORDER BY date DESC LIMIT 1"
    cursor.execute(query)
    anwser = cursor.fetchone()
    return anwser

@app.route('/api', methods=['GET'])
def api():
    anwser=select_one()
    return jsonify(number=anwser[0], date=anwser[1])

@app.route('/', methods=['GET'])
def home():
    anwser=select_one()
    return render_template('home.html', number=anwser[0], date=anwser[1])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
