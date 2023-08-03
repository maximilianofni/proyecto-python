from flask import Flask
from admin.src.core.database import db
from flask_sqlalchemy import SQLAlchemy
from admin.src.core import database
from flask import Flask
from flask import render_template, request, redirect , url_for
from admin.src.core.config import config
from admin.src.core.models.usuario_model import Usuario


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    # configuracion de la bd
    database.init_app(app)
    app.secret_key= "holamundo"
    app.config["SESSION_TYPE"] = "filesystem"

    
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

    #para la configuracion de la bd
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()
  

    return app