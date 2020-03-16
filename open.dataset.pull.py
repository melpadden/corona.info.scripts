import pandas as pd
import matplotlib, openblender, wordcloud

action = 'API_getObservationsFromDataset'
parameters = {
    'token': 'YOUR_TOKEN_HERE',
    'id_dataset': '5e6ac97595162921fda18076',
    'date_filter': {
        "start_date": "2020-01-01T06:00:00.000Z",
        "end_date": "2020-03-11T06:00:00.000Z"},

}

df_confirmed = pd.read_json(json.dumps(OpenBlender.call(action, parameters)[
                            'sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df_confirmed.reset_index(drop=True, inplace=True)
df_confirmed.head(10)
