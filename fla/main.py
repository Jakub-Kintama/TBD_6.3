#main.py
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_DB():
    return psycopg2.connect(host='postgres_db', database='postgres', user='postgres', password='postgres', port=5432)

@app.route('/')
def home():
    return "Flask is working"

@app.route('/cars', methods=['GET'])
def Cars():
    db = get_DB()
    year = request.args.get('year')

    if year is None:
        query = "SELECT * FROM Car"
    else:
        query = "SELECT * FROM Car WHERE year = " + year

    cur = db.cursor()
    cur.execute(query)
    output = cur.fetchall()
    cur.close()
    db.close()

    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)