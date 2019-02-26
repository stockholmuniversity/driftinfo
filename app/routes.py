#!/usr/bin/env python3
from flask import render_template, request, flash
from app import app
from app import db
import sqlite3
import yaml 

config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)

@app.route('/')
@app.route('/submit', methods=['POST'])
def bacon_form():
    if request.method == "POST":
       brief_text = request.form.get('brief_text')
       headline = request.form.get('headline')
       long_text  = request.form.get('long_text')
       username  = request.form.get('username')
       disturbance_checkbox = request.form.get('disturbance')
       disturbance = 0
       if disturbance_checkbox == "on":
           disturbance = 1
       conn = sqlite3.connect(cfg['driftinfo_for_database']['path_to_database'])
       cur = conn.cursor()
       cur.execute("INSERT INTO driftinfo (headline,long_text,brief_text,disturbance,username)  VALUES(?,?,?,?,?)",(headline,long_text,brief_text,disturbance,username))
       conn.commit()
       cur.close()
       return render_template('/submitted.html', headline=headline, long_text=long_text, brief_text=brief_text, disturbance=disturbance)
    return render_template('/base.html')


app.secret_key=cfg['app']['secret_key']



