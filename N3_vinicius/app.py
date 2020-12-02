from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost/crud"

mongo = PyMongo(app)
