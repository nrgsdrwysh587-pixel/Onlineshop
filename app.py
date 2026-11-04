from flask import Flask, render_template, request, redirect, session
import pyodbc

app = Flask(__name__)
app.secret_key = "12345"

def connect():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=OnlineShop;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

@app.route("/")
def home():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    db.close()
    return render_template("index.html", products=products)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "1234":
            session["admin"] = True
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

@app.route("/add", methods=["POST"])
def add():
    if not session.get("admin"):
        return redirect("/login")

    db = connect()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        request.form["name"],
        request.form["price"],
        request.form["category"]
    )
    db.commit()
    db.close()
    return redirect("/")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    if not session.get("admin"):
        return redirect("/login")

    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", id)
    db.commit()
    db.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
