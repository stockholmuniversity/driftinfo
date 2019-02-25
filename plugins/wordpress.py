import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime
import yaml


config_file = 'config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)



#lägger upp en post till wordpress genom att skicka en email
def send_email(headline,message):
    email = cfg['driftinfo']['email_from']
    password = cfg['driftinfo']['password']
    send_to_email = cfg['driftinfo']['send_to_email']
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

#anslutar till wordpress databasen
def connect_to_Wordpress():
    print( """ Connect to database """)
    try:
        conn = sqlite3.connect(cfg['driftinfo_for_database']['path_to_database'])

        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")
        sql_select_Query = "select * from driftinfo where processed_wordress = 0"
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of information in driftinfo is ", cursor.rowcount)
        print("Printing each row's column values in driftinfo")
        for row in records:
            send_email(row[3],row[4])
            sql_update_Query = "update driftinfo set processed_wordpress ="+ str(dtime) + " where id = " + str(row[0])
            cursor.execute(sql_update_Query)
            conn.commit()
        cursor.close()
    except ConnectionError as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')



connect_to_Wordpress()
