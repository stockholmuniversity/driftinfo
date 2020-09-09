#!/local/driftinfo/venv/bin/python3
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sqlite3
import sys
import yaml

service = sys.argv[1]
valid_services = []
#Workaround for crappy logging
try:
    sys.stdout = open('/local/driftinfo/logs/generic_email_stdout', 'a+')
    sys.stderr = open('/local/driftinfo/logs/generic_email_stderr', 'a+')
except:
    print("Assigning stdout/err didn't go too well.")
    pass

config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile,Loader=yaml.SafeLoader)

for obj in cfg['plugins']:
    for plugin in obj:
        if plugin == "generic_email":
            valid_services = obj[plugin]

use_brief_text = ["sms"]
disturbance_only = ["sms"]

if service not in valid_services:
    msg = service + " is not one of the valid services:"
    for e in  valid_services:
        msg += " " + e
    print(msg)
    sys.exit(1)

def send_email(headline,message):
    email = cfg['email']['email_from_office365']
    password = cfg['email']['password_office365']
    smtp_address = cfg['email']['smtp_address_office365']
    smtp_port = cfg['email']['smtp_port_office365']
    send_to_email = cfg['email']['send_to_email_' + service ]
    user_office365 = cfg['email']['user_office365']
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = headline

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_address, smtp_port)
    server.ehlo()
    server.starttls()
    server.login(user_office365, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    # Save the entire message to log, to find out if the service provider is lying to us about message concatenation:
    print("MESSAGE:\n\n"+text+"\n\n")
    server.quit()

def connect_to_db():
    print( """ Connect to database """)
    try:
        conn = sqlite3.connect(cfg['database']['path'])

        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")
        sql_select_Query = "select id,brief_text,headline,long_text,categories from driftinfo where processed_" + service +" = 0"
        if service in disturbance_only:
            sql_select_Query += " AND disturbance = 1" 
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of unprocessed messages for " + service + " in driftinfo is ", len(records))
        for row in records:
            message = row[3]
            if service == "wordpress" :
                message += "\n[category "+ row[4] + "]"
            if service in use_brief_text:
                message = row[1]
            send_email(row[2],message)
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
