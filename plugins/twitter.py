#!/local/driftinfo/venv/bin/python3
import twitter
from datetime import datetime
import sqlite3
import yaml


config_file = '/local/driftinfo/conf/config_file.yml'
with open(config_file,'r') as ymlfile:
    cfg = yaml.load(ymlfile)

def send_to_twitter(twitter_data):
    consumer_key = cfg['driftinfo_for_twitter']['key']
    consumer_secret = cfg['driftinfo_for_twitter']['secret']
    access_token = cfg['driftinfo_for_twitter']['token']
    access_secret = cfg['driftinfo_for_twitter']['token_secret']
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

    status = api.PostUpdate(twitter_data)
    print(status.text)


def connect_to_Twitter():
    try:
        conn = sqlite3.connect(cfg['driftinfo_for_database']['path_to_database'])
        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")
        sql_select_Query = 'select * from driftinfo where processed_twitter = 0'
        cursor = conn.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total of information in driftinfo is ", cursor.rowcount)
        print("Printing each row's column values in driftinfo")
        for row in records:
            send_to_twitter(row[1])
            sql_update_Query = "update driftinfo set twitter_process =" + str(dtime) + " where id  = " + str(row[0])
            cursor.execute(sql_update_Query)
            conn.commit()
        cursor.close()

    except Error as error:
        print(error)

    finally:
        conn.close()
        print('Connection closes.')


if __name__ == '__main__':
    connect_to_Twitter()
