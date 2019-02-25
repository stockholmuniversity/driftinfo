
from twilio.rest import Client
from datetime import datetime
import sqlite3
import yaml


config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def send_sms(sms):
    account_sid = cfg['driftinfo_for_sms']['sid']
    auth_token = cfg['driftinfo_for_sms']['token']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=sms,
        from_=cfg['driftinfo_for_sms'][nummer],
        to= cfg['driftinfo_for_sms'][to_nummer]

    )
    print(message.sid)


def connect_to_message():
    print(""" Connect to database """)
    try:
        print('Connecting to database...')
        conn = sqlite3.connect(cfg['driftinfo_for_database']['path_to_database'])
        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")


        sql_select_Query = 'select * from driftinfo where processed_sms = 0  and disturbance = 1'
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of information in driftinfo is ", cursor.rowcount)
        print("Printing each row's column values in driftinfo")
        for row in records:
            send_sms(row[1])
            sql_update_Query = "update driftinfo set processed_sms =" + str(dtime) + " where id = " + str(row[0])
            cursor.execute(sql_update_Query)
            conn.commit()
        cursor.close()
    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')


connect_to_message()
