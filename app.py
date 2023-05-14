from flask import Flask, render_template,request,redirect
import sqlite3
import datetime

app = Flask(__name__)
db = sqlite3.connect("data.db",check_same_thread=False)
db.execute("CREATE TABLE IF NOT EXISTS data (item VARCHAR(20),radio varchar(10), quantity int, time varchar(10), date varchar(12), day varchar(10), amount float, total float)")


@app.route("/",methods=["POST", "GET"])
def index():
    data = db.execute("SELECT * FROM data").fetchall()
    return render_template("index.html",data=data)
 
@app.route('/add',methods=["POST","GET"])
def get_data():
    name = request.form.get("name")
    quantity = request.form.get("quantity")
    price = request.form.get("price")
    radio = request.form.get("earned/spent")
    time,date,day = timedateday()
    if name and quantity and price and radio:
        total = float(quantity)*float(price)
        query = "INSERT INTO data values (?,?,?,?,?,?,?,?)"
        db.execute(query,(name,radio,quantity,time,date,day,price,total))
        db.commit()
    return redirect("/")

def timedateday():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    date,time = formatted_date.split(' ')
    day = now.strftime("%A")
    return time,date,day

@app.route("/remove", methods=["POST", "GET"])
def remove():
        cur = db.cursor()
        checked_items = request.form.getlist("items")
        for items in checked_items:
            items = items.split(",")
            cur.execute(f"DELETE FROM data WHERE item=? and radio=? and quantity=? and time=? and date=? and day=? and amount=? and total=?",
                        (items[0],items[1], int(items[2]), items[3], items[4], items[5], float(items[6]), float(items[7])))
            db.commit()
        cur.close()
        return redirect("/")

@app.route("/dropdown",methods=["POST", "GET"])
def dropdown():
     monthyear = request.form["monthyear"]
     print(monthyear)
     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)



