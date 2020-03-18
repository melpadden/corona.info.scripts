import pandas as pd
import urllib.request
import shutil
import urllib


url = "https://query.data.world/s/aswecb236xebxxcncltyf4isn4w763"
df = pd.read_csv('https://query.data.world/s/aswecb236xebxxcncltyf4isn4w763')

with urllib.request.urlopen(url) as response, open('who_data.csv', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)