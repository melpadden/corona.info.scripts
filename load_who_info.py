import pandas as pd
import psycopg2
import constants
import os, datetime, math

conn = psycopg2.connect(
    database=constants.DB_NAME,
    user=constants.USER_NAME,
    password=constants.PASSWORD,
    host=constants.HOST_NAME,
    port=constants.PORT_NUMBER
)
cur = conn.cursor()

dir_path = os.path.dirname(os.path.realpath(__file__))
who_file_name = dir_path + '\\who_data.csv'

df = pd.read_csv(who_file_name)
print(df.head())


for index, row in df.iterrows():
    # print(row['Code'], row['Name'])
    date = row['Date']
    country_region = row['Country_Region']
    province_state = row['Province_State']
    case_type = row['Case_Type']
    cases = row['Cases']
    difference = row['Difference']
    prep_flow_runtime = row['Prep_Flow_Runtime']
    latest_date = row['Latest_Date']
    lat = row['Lat']
    long = row['Long']

    sql_template = 'INSERT INTO who_data ("date",country_region,province_state,case_type,cases,difference,prep_flow_runtime,latest_date,lat,long ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )'
    #sql = cur.mogrify(sql_template, (date,country_region,province_state,case_type,cases,difference,prep_flow_runtime,latest_date,lat,long))
    #print(sql)
    result = cur.execute(sql_template, (date,country_region,province_state,case_type,cases,difference,prep_flow_runtime,latest_date,lat,long))
    #if index > 10 : exit()


conn.commit()

print("Done!")
