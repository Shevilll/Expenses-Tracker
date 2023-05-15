from flask import Flask, render_template,request,redirect
import sqlite3
import datetime

app = Flask(__name__)
db = sqlite3.connect("data.db",check_same_thread=False)

@app.route("/",methods=["POST", "GET"])
def index():
    global month_year
    now = datetime.datetime.now()
    month_year = request.form.get("monthyear")
    total_earned,total_spent,total_expenses = 0,0,0
    if not month_year:
        month_year = now.strftime("%B-%Y").replace("-","_")
    if month_year == now.strftime("%B-%Y").replace("-","_"):
         disable_button = False
    else:
         disable_button = True
    db.execute(f"CREATE TABLE IF NOT EXISTS {month_year} (item VARCHAR(20),radio varchar(10), quantity int, time varchar(10), date varchar(12), day varchar(10), amount float, total float)")
    data = db.execute(f"SELECT * FROM {month_year}").fetchall()
    if data:
         for i in data:
            if i[1] == "Earned":
                total_earned += i[7]
            else:
                total_spent += i[7]
            total_expenses += i[7]
    return render_template("index.html",data=data, month_year=month_year.replace("_","-"),disable_button=disable_button,total_earned=total_earned,total_spent=total_spent,total_expenses=total_expenses)

@app.route('/add',methods=["POST","GET"])
def get_data():
    name = request.form.get("name")
    quantity = request.form.get("quantity")
    price = request.form.get("price")
    radio = request.form.get("earned/spent")
    time,date,day = timedateday()
    if name and quantity and price and radio and month_year:
        total = float(quantity)*float(price)
        query = f"INSERT INTO {month_year} values (?,?,?,?,?,?,?,?)"
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
        if month_year:
            for items in checked_items:
                items = items.split(",")
                cur.execute(f"DELETE FROM {month_year} WHERE item=? and radio=? and quantity=? and time=? and date=? and day=? and amount=? and total=?",
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



