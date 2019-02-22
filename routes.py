#!/usr/bin/env python3
from flask import render_template, request, flash
from app import app
from app import db
import sqlite3

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
def bacon_form():
    if request.method == "POST":
       long  = request.form.get('long')
       short = request.form.get('short')
       sms = request.form.get('sms')
      # sms_process = request.get('sms_process')
       rubrik = request.form.get('rubrik')
       wordpress = request.form.get('wordpress')
       twitter = request.form.get('twitter')
       conn = sqlite3.connect(cfg['driftinfo_for_database']['path_to_database'])
       cur = conn.cursor()
       cur.execute("INSERT INTO driftinfo (rubrik,big,small,sms,wordpress_process)  VALUES(?,?,?,?,?)",(rubrik,long,short,sms,wordpress))
       conn.commit()
       cur.close()
       return   "<h1> the title is  {} the long text is {} \n the short text is   {}</h1> \n sms{} ".format(rubrik,long,short,sms,wordpress,twitter)
    return render_template('/base.html', title='Home')


app.secret_key='secret123'



