from app import db
from datetime import datetime as dt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    user_name = db.Column(db.String(100), unique=True)
    hour_price = db.Column(db.Numeric)
    profit = db.Column(db.Integer)
    image_url = db.Column(db.String(300))


    def __init__(self, email, password, user_name, hour_price, profit, image_url):
        self.email = email
        self.password = password
        self.user_name = user_name
        self.hour_price = hour_price
        self.profit = profit
        self.image_url = image_url
    
    def __str__(self):
        return self.email


class Material (db.Model):
    __tablename__ = 'materials'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    color = db.Column(db.String(100))
    unit_messure = db.Column(db.String(30))
    unit_weight = db.Column(db.String(30))
    quantity = db.Column(db.Integer)


    def __init__(self, name, price, color, unit_messure, unit_weight, quantity):
        self.name = name
        self.price = price
        self.color = color
        self.unit_messure = unit_messure
        self.quantity = quantity
        self.unit_weight = unit_weight


class Time (db.Model):
    __tablename__ = 'times'

    id = db.Column(db.Integer, primary_key=True)
    time_date = db.Column(db.String(100))
    beg_time = db.Column(db.Numeric)
    current_time = db.Column(db.Numeric)
    final_time = db.Column(db.Numeric)


    def __init__(self, time_date, beg_time, current_time, final_time):
        self.time_date = time_date
        self.beg_time = beg_time
        self.current_time = current_time
        self.final_time = final_time


class Proyect (db.Model):
    __tablename__ = 'proyects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    client_name = db.Column(db.String(100))
    deliver_date = db.Column(db.Date(), default=dt.now)
    annotations = db.Column(db.String)
    total_price = db.Column(db.Integer)
    total_time = db.Column(db.Integer)


    def __init__(self, name, client_name, deliver_date, annotations, total_price, total_time):
        self.name = name
        self.client_name = client_name
        self.deliver_date = deliver_date
        self.annotations = annotations
        self.total_price = total_price
        self.total_time = total_time


class Folder (db.Model):
    __tablename__ = 'folders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


    def __init__(self, name):
        self.name = name
    