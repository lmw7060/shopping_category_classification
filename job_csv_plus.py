import pandas as pd
import glob
import datetime

s1 = pd.read_csv('csv/gmarket_shopping_titles_20240130.csv')
s2 = pd.read_csv('csv/naver_shopping_titles_20240129.csv')
s3 = pd.read_csv('csv/crawling_data_last_coupang.csv')
s4 = pd.read_csv('csv/11st_shopping_title20240130.csv')

data_path = glob.glob('csv/*')
df = pd.DataFrame()
for path in data_path:
    df_temp = pd.read_csv(path)
    df_temp = df_temp.replace('Makeup', 'Beauty')
    df_temp = df_temp.replace('Interior', 'Furniture')
    df_temp = df_temp.replace('Fasion', 'Fashion')
    df_temp = df_temp.replace('HA/Di', 'Digital')
    df_temp = df_temp.replace('Fu/In', 'Furniture')
    df_temp = df_temp.replace('travel', 'Trip')
    df_temp.dropna(inplace=True)
    df = pd.concat([df, df_temp])

df.info()
df.to_csv('csv/shopping_titles_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)