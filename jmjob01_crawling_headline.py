import pandas as pd
from bs4 import BeautifulSoup #pip install bs4
import requests
import re
import datetime

category = ['Fashion','Makeup','Interior','Digital','Food','Trip']
ca = ['03','05','31','32','20']
df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z]')
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
titles=[]
for i in ca:
    url = 'https://category.gmarket.co.kr/listview/L1000000{}.aspx'.format(i)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.name')
    for title_tag in title_tags:
        titles.append(re_title.sub(' ', title_tag.text))
    df_section_titles = pd.DataFrame(titles, columns=['titles'])
    df_section_titles['category'] = category[ca.index(i)]
    df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)
url = 'https://gtour.gmarket.co.kr/TourLP/List?gdmc_cd=200000719 '
resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'html.parser')
title_tags = soup.select('.goods_name')
for title_tag in title_tags:
    titles.append(re_title.sub(' ', title_tag.text))
df_section_titles = pd.DataFrame(titles, columns=['titles'])
df_section_titles['category'] = category[5]
df_titles = pd.concat([df_titles, df_section_titles], axis='rows', ignore_index=True)

print(df_titles.head())
df_titles.info()
print(df_titles['category'].value_counts())
df_titles.to_csv('./crawling_data/gmarket_shopping_{}.csv'.format(
    datetime.datetime.now().strftime('%Y%m%d')), index=False)