import pandas as pd
import datetime
import os
import urllib.request
import shutil
import requests
import urllib

# https://towardsdatascience.com/gather-all-the-coronavirus-data-with-python-19aa22167dea
# https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports

dir_path = os.path.dirname(os.path.realpath(__file__))
the_day = datetime.date(2020, 1, 22)
date_template = '{0:02d}-{1:02d}-{2}'
url_template = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/{0}.csv'
today = datetime.date.today()

while the_day < today:
    #try:
    date_string = date_template.format(the_day.month, the_day.day, the_day.year)
    output_file_name = dir_path + '\\data\\' + date_string + '.csv'
    #output_file_name = dir_path + '\\data\\columns.csv'
    data = pd.read_csv(output_file_name)
    print(output_file_name + ' read')
    print(data.head())
    the_day = the_day + datetime.timedelta(days=1)
        # print ('{0} read'.format(output_file_name))
        # print(the_day)
        # print(the_day < today)
    #except FileNotFoundError:
    #    print(output_file_name + ' not found')
    #    exit()
    #except:
    #    print('Error occurred')
    #    exit()

print("Done!")


