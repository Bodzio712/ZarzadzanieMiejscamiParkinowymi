from flask import Flask, jsonify

import psycopg2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    connection = psycopg2.connect(user="piotr",
            password="windows7",
            host="127.0.0.1",
            port="5432",
            database="pgs")

    cursor = connection.cursor()
    query = "SELECT number, date FROM data ORDER BY date DESC LIMIT 1"
    cursor.execute(query)
    anwser = cursor.fetchone()
    return jsonify(number=anwser[0], date=anwser[1])
