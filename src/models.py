#Este archivo me permite crear las tablas de la base de datos

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):                     #Opcional
        return '<User %r>' % self.email

    def serialize(self):                    #Obligatorio
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=True)
    birth_year = db.Column(db.Integer, unique=False, nullable=True)
    height = db.Column(db.Integer, unique=False, nullable=True)
    mass = db.Column(db.Integer, unique=False, nullable=True)
    hair_color = db.Column(db.String(50), unique=False, nullable=True)
    skin_color = db.Column(db.String(50), unique=False, nullable=True)
    eye_color = db.Column(db.String(50), unique=False, nullable=True)

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth year": self.birth_year,
            "height": self.height,
            "mass": self.mass,
            "hair color": self.hair_color,
            "skin color": self.skin_color,
            "eye color": self.eye_color
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    climate = db.Column(db.String(50), unique=False, nullable=True)
    rotation_period = db.Column(db.String(50), unique=False, nullable=True)
    orbital_period = db.Column(db.String(50), unique=False, nullable=True)
    diameter = db.Column(db.String(50), unique=False, nullable=True)
    gravity = db.Column(db.String(50), unique=False, nullable=True)
    population = db.Column(db.String(50), unique=False, nullable=True)

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "rotation period": self.rotation_period,
            "orbital period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population
        }

class Fav_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_people = db.Column(db.Integer, db.ForeignKey('people.id'))
    rel_user = db.relationship("User")
    rel_people = db.relationship("People")

    def __repr__(self):
        return '<Favorite character %r>' % self.id_people

    def serialize(self):
        return {
            "id": self.id,
            "character name": self.id_people,
            "user name": self.id_user
        }

class Fav_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    rel_user = db.relationship("User")
    rel_planets = db.relationship("Planets")

    def __repr__(self):
        return '<Favorite planet %r>' % self.id_planets

    def serialize(self):
        return {
            "id": self.id,
            "planet name": self.id_planets,
            "user name": self.id_user
        }
 
