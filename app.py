from flask import Flask, render_template,request,redirect
import sqlite3
import datetime

app = Flask(__name__)
db = sqlite3.connect("data.db",check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS data (item VARCHAR(20), quantity int, time varchar(10), data varchar(12), day varchar(10), amount float, total float)")


@app.route("/",methods=["POST", "GET"])
def index():
    data = db.execute("SELECT * FROM data").fetchall()
    return render_template("index.html",data=data)
 
@app.route('/add',methods=["POST","GET"])
def get_data():
    name = request.form.get("name")
    quantity = request.form.get("quantity")
    price = request.form.get("price")
    time,date,day = timedateday()
    if name and quantity and price:
        total = float(quantity)*float(price)
        query = "INSERT INTO data values (?,?,?,?,?,?,?)"
        db.execute(query,(name,quantity,time,date,day,price,total))
        db.commit()
    return redirect("/")

def timedateday():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    date,time = formatted_date.split(' ')
    day = now.strftime("%A")
    return time,date,day

if __name__ == "__main__":
    app.run(debug=True)



