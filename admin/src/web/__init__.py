from cgitb import handler
from flask import Flask
from flask import render_template, request, redirect , url_for

from src.web.helpers import handlers

def create_app():
    app = Flask(__name__)

    #ruta al home
    @app.route("/")
    def home():
        return redirect(url_for("login"))
    
    #ruta al login
    @app.route("/login", methods=["GET" , "POST"])
    def login():
        if request.method == "POST":
            print(request.form['username'])
            print(request.form['password'])
            return render_template("auth/login.html")
        else:
            return render_template("auth/login.html")

    #funcion para mostrar un mensaje para cuando el usuario ingrese una url invalida o modulo invalido
    app.register_error_handler(404, handlers.not_found_error)

    return app