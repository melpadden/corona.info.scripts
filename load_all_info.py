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
the_day = datetime.date(2020, 1, 22)
date_template = '{0:02d}-{1:02d}-{2}'
url_template = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{0}.csv'
today = datetime.date.today()

while the_day < today:
    date_string = date_template.format(the_day.month, the_day.day, the_day.year)
    output_file_name = dir_path + '\\data\\' + date_string + '.csv'
    df = pd.read_csv(output_file_name)

    for index, row in df.iterrows():
        # print(row['Code'], row['Name'])
        province_name = row['Province/State']
        country_name = row['Country/Region']
        last_update = row['Last Update']
        confirmed = row['Confirmed']
        deaths = row['Deaths']
        recovered = row['Recovered']
        if isinstance(province_name, float) and math.isnan(province_name): province_name = ""
        if isinstance(country_name, float) and math.isnan(country_name): country_name = ""
        if isinstance(last_update, float) and math.isnan(last_update): last_update = None
        if math.isnan(confirmed): confirmed = 0
        if math.isnan(deaths): deaths = 0
        if math.isnan(recovered): recovered = 0

        sql_template = "INSERT INTO corona_info (country_name, province_name, last_update, confirmed, deaths, recovered) VALUES ( %s, %s, %s, %s, %s, %s )"
        sql = cur.mogrify(sql_template, (country_name, province_name, last_update, confirmed, deaths, recovered))
        print(sql)

        result = cur.execute(sql_template, (country_name, province_name, last_update, confirmed, deaths, recovered))

    the_day = the_day + datetime.timedelta(days=1)

conn.commit()

print("Done!")
