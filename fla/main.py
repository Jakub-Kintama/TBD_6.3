#main.py
import psycopg2
from flask import Flask, request

app = Flask(__name__)

def DB():
    return psycopg2.connect(host='172.17.0.2', database='db', user='postgres', password='mysecretpassword', port=5432)

@app.route('/')
def home():
    return "Flask Sample Application"

@app.route('/cars', methods=['GET'])
def Cars():
    db = DB()
    year = request.args.get('year')

    if year is None:
        query = "SELECT * FROM Car"
    else:
        query = "SELECT * FROM Car WHERE year = " + year

    cur = db.cursor()
    cur.execute(query)
    output_json = cur.fetchall()
    db.close()

    return jsonify(output_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)