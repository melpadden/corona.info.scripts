import datetime
import os
import urllib.request
import shutil
import requests
import urllib
# https://towardsdatascience.com/gather-all-the-coronavirus-data-with-python-19aa22167dea

dir_path = os.path.dirname(os.path.realpath(__file__))
the_day = datetime.date(2020, 1, 22)
date_template = '{0:02d}-{1:02d}-{2}'
url_template = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{0}.csv'
today = datetime.date.today()
    
while the_day < today:
    date_string = date_template.format(the_day.month, the_day.day, the_day.year)
    url = url_template.format(date_string)
    output_file_name = dir_path + '\\data\\' + date_string + '.csv'
    
    # with urllib.request.urlopen(url) as response, open(output_file_name, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)

    print ('{0} created'.format(output_file_name))
    the_day = the_day + datetime.timedelta(days = 1)
    print(the_day)
    print(the_day < today)

print("Done!")

