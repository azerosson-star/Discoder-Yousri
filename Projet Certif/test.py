# from flask import Flask, render_template,send_file
import sqlite3

# app = Flask(__name__)

# def lire_db() :
#     conn = sqlite3.connect("BDD/BDD.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM Users")
#     donnees = cursor.fetchall()
#     conn.close()
#     return donnees



# @app.route("/")
# def home():
#     return lire_db()

# @app.route("/test")
# def afficher_utilisateurs():
#     data = lire_db()
#     return render_template("test.html", lignes=data)

def compter_id() :
    conn = sqlite3.connect("BDD/BDD.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id_lesson FROM Lessons")
    donnees = [x[0] for x in cursor.fetchall()]
    conn.close()
    return donnees

def lire_db(id) :
    conn = sqlite3.connect("BDD/BDD.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT file_path FROM Lessons WHERE id_lesson = {id}")
    donnees = [x[0] for x in cursor.fetchall()]
    conn.close()
    return donnees

for id in compter_id() :
    print(lire_db(id))

def lire_db_test() :
    conn = sqlite3.connect("BDD/BDD.db")
    cursor = conn.cursor()
    cursor.execute("SELECT file_path FROM Lessons")
    donnees = [x[0] for x in cursor.fetchall()]
    conn.close()
    return donnees

print(lire_db_test())

# @app.route("/test")
# def afficher_lessons():
#     data = lire_db()
#     return render_template("test.html", lignes=data)

# app.run()