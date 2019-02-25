from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml 

config_file = 'config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = cfg['driftinfo_for_database']['path_to_database']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

from app import routes
