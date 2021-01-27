import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# Mongo Config
client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.test
users = db.users
# User Config
nombre = ""
apellido = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global nombre
    global apellido
    if request.method == "POST":
        user = request.form.get("usuario")
        dni = request.form.get("dni_number")
        if(users.find_one({"nombre": user, "DNI": dni})):
            res = users.find_one({"nombre": user, "DNI": dni})
            nombre = res["nombre"]
            apellido = res["apellido"]
            return redirect("home/")
    return render_template("login.html")

@app.route("/home/")
def home():
    return render_template("inicio.html", nombre=nombre, apellido=apellido)

if __name__ == '__main__':
    app.run(port=8000)
