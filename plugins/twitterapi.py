#!/local/driftinfo/venv/bin/python3

from datetime import datetime
import sqlite3
import yaml
import twitter

CONFIG_FILE = '/local/driftinfo/conf/config_file.yml'
with open(CONFIG_FILE, 'r') as ymlfile:
    CFG = yaml.load(ymlfile, Loader=yaml.FullLoader)

def send_to_twitter(twitter_data):
    consumer_key = CFG['twitter']['key']
    consumer_secret = CFG['twitter']['secret']
    access_token = CFG['twitter']['token']
    access_secret = CFG['twitter']['token_secret']
    api = twitter.Api(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)

    status = api.PostUpdate(twitter_data)
    print(status.text)

def connect_to_twitter():
    try:
        conn = sqlite3.connect(CFG['database']['path'])
        now = datetime.now()
        dtime = now.strftime("%d/%m/%Y %H:%M:%S")
        sql_select_query = 'select * from driftinfo where processed_twitter = 0'
        cursor = conn.cursor()
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Total of information in driftinfo is ", len(records))
        for row in records:
            twitterdata = row[1][:279]
            send_to_twitter(twitterdata)
            sql_update_query = "update driftinfo set processed_twitter =\""+\
                                str(dtime) + "\" where id = " + str(row[0])
            cursor.execute(sql_update_query)
            conn.commit()
        cursor.close()

    except ConnectionError as error:
        print(error)

    finally:
        conn.close()
        print('Connection closes.')


if __name__ == '__main__':
    connect_to_twitter()
