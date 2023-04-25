"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False          #para que la url pueda o no terminar con un / :)

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)            #para que en la url principal me aparezcan todas las rutas creadas

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def get_people():
    return "List of people here"

@app.route('/people/<int:people_id>', methods=['GET'])
def get_character():
    return "Info of one character only"

@app.route('/planets', methods=['GET'])
def get_planets():
    return "list of planets"

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet():
    return "Info of one planet only"

@app.route('/users', methods=['GET'])
def get_users():
    return "List of all blog users"

@app.route('/users/favorites', methods=['GET'])
def get_userFavorites():
    return "List of all favorites that beong to the current user"

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favoritePlanet():
    return "Add a new favorite planet to the current user with the planet id = planet_id."

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favoritePeople():
    return "Add a new favorite people to the current user with the people id = people_id."

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_fvoritePlanet():
    return "Delete favorite planet with the id = planet_id."

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_fvoritePeople():
    return "Delete favorite people with the id = people_id."

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
