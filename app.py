from flask import Flask, render_template,jsonify,request
import sqlite3
import datetime

app = Flask(__name__)
db = sqlite3.connect("data.db",check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS data (item VARCHAR(20), quantity int, time varchar(10), data varchar(12), day varchar(10), amount float, total float)")


@app.route("/",methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route('/data',methods=["POST","GET"])
def get_data():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)



