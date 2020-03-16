import datetime
import urllib.request
import shutil
import requests
import urllib

the_day = datetime.date(2022, 1, 22)
date_template = '{0:02d}-{1:02d}-{2}'
url_template = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{0}.csv'
today = datetime.date.today()

while the_day < today:
    date_string = date_template.format(the_day.month, the_day.day, the_day.year)
    url = url_template.format(date_string)
    output_file_name = date_string + '.csv'
    with urllib.request.urlopen(url) as response, open(output_file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

print("Done!")