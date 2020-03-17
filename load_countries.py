import pandas as pd
import psycopg2
import constants 
#from sqlescapy import sqlescape

conn = psycopg2.connect(
    database=constants.DB_NAME,
    user=constants.USER_NAME,
    password=constants.PASSWORD,
    host=constants.HOST_NAME,
    port=constants.PORT_NUMBER
)

cur = conn.cursor()

df = pd.read_json('country_codes.json')
print(df.columns)

for index, row in df.iterrows():
    #print(row['Code'], row['Name'])
    country_code = row['Code']
    country_name = row['Name']
    sql = "INSERT INTO country (country_code, country_name) VALUES ( '{0}', '{1}' )".format(row['Code'], row['Name'])
    sql_template = "INSERT INTO country (country_code, country_name) VALUES ( %s, %s )"
    #print(sql)
    result = cur.execute(sql_template, (country_code, country_name))
    #print(result)
conn.commit()





