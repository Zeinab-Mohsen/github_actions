from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    conn = mysql.connector.connect(
        host="db",
        port=3306,
        user="root",
        password="p@ssw0rd",
        database="userdb",
    )
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        gender = request.form["gender"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (first_name, last_name, gender) VALUES (%s, %s, %s)",
            (first_name, last_name, gender),
        )
        conn.commit()
        cursor.close()
        conn.close()

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
