from datetime import datetime
from admin.src.core.database import db
from sqlalchemy import Column, Boolean

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(500))    
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.String(10)) #activo no-activo
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
   
    def __init__(
            self, email, username, password, first_name, last_name , asociado_id = None, 
    ):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.activo = "Activo"
