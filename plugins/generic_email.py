#!/local/driftinfo/venv/bin/python3
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sqlite3
import sys
import yaml

service = sys.argv[1]
valid_services = ["wordpress", "sms"]
use_short = ["sms"]
if service not in valid_services:
    msg = service + " is not one of the valid services:"
    for e in  valid_services:
        msg += " " + e
    print(msg)
    sys.exit(1)

config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def send_email(headline,message):
    email = cfg['email']['email_from']
    password = cfg['email']['password']
    send_to_email = cfg['email']['send_to_email_' + service ]
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = headline

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()

def connect_to_db():
    print( """ Connect to database """)
    try:
        conn = sqlite3.connect(cfg['database']['path'])

        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")
        sql_select_Query = "select * from driftinfo where processed_" + service +" = 0"
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of unprocessed messages for " + service + " in driftinfo is ", len(records))
        for row in records:
            message = row[4]
            if service in use_short:
                message = row[1]
            send_email(row[3],message)
            sql_update_Query = "update driftinfo set processed_" + service + " =\""+ str(dtime) + "\" where id = " + str(row[0])
            cursor.execute(sql_update_Query)
            conn.commit()
        cursor.close()
    except ConnectionError as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')

connect_to_db()
