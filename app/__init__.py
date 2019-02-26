from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml 

config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = cfg['database']['path']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from app import routes
