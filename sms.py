
from twilio.rest import Client
from datetime import datetime
import sqlite3
import yaml


config_file = 'config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)



def send_sms(sms):
    account_sid = cfg['driftinfo_for_sms']['sid']
    auth_token = cfg['driftinfo_for_sms']['token']
    client = Client(account_sid, auth_token)

    #    numbers_to_message = ['+46766051555', '+46760344070']
    #   for number in numbers_to_message:
    #      client.messages.create(
    #          body = sms,
    #         from_ ='+46790644309',
    #        to = number
    #  )
    message = client.messages \
        .create(
        body=sms,
        from_=cfg['driftinfo_for_sms'][nummer],
        to= cfg['driftinfo_for_sms'][to_nummer]

    )
    print(message.sid)


def connect_to_message():
    print(""" Connect to MySQL database """)
    try:
        print('Connecting to MySQL database...')
        conn = sqlite3.connect("/home/usko/flask/venv/app/driftinfo.db")
        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")


        sql_select_Query = 'select * from driftinfo where sms_process = 0  and sms="on"'
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of information in driftinfo is ", cursor.rowcount)
        print("Printing each row's column values in driftinfo")
        for row in records:
            send_sms(row[3])
            # print("id = ",  row[0])
            # print("big = ", row[1])
            # print("small = ", row[2])
            # print("sms = ", row[3])
            # print("reg_date = ", row[4],"\n")

            sql_update_Query = "update driftinfo set sms_process =\"" + str(dtime) + "\" where id = " + str(row[0])
            cursor.execute(sql_update_Query)
            conn.commit()
        cursor.close()
    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closed.')


connect_to_message()
