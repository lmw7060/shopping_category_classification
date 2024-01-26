from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

#selenium, webdriver_manager 설치

category = ['Fasion', 'Makeup', 'Interior', 'Digital', 'Food', 'Trip']
ca = ['0002', '0003', '0004', '0006', '0015', '8370']
options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
#pages = [164, 352, 556, 81, 107, 81] #각 카테고리 뉴스마다의 마지막 페이지. 다 긁어올거면 이렇게 하면 된다.
                                    #근데 학습할 때 데이터의 불균형이 있으면 판단을 제대로 못한다.
pages = [150, 150, 150, 150, 150, 150] #그래서 학습데이터 개수 균형 맞춰주기

df_titles = pd.DataFrame()

for l in ca:  #정치인지, 경제인지...
    section_url = 'https://search.shopping.naver.com/search/category/10000{}'.format(l)
    titles = []
    for k in range(1, pages[ca.index(l)]): #1~105페이지 긁기위해
        if l == '0002':
            url = section_url + ('?adQuery&catId=50000167%2050000168%2050000173%'
                                '2050000176&iq=%EC%97%AC%EC%9E%90&origQuery&pagingIndex={}&pagingSize=40&productSet=total&query&sort'
                                '=rel&timestamp=&viewType=list').format(k) #페이지 마다 뒷숫자만 달라지는 주소
        elif l == '0003':
            url = section_url + ('?adQuery&catId=50000002&origQuery&pagingIndex={}&'
                                 'pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list').format(k)
        elif l == '0004':
            url = section_url + ('?adQuery&catId=50000004&origQuery&pagingIndex={}&'
                                 'pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list').format(k)
        elif l == '0006':
            url = section_url + ('?adQuery&catId=50000088%2050000209%2050000204%'
                                 '2050000152%2050000205&origQuery&pagingIndex={}&pagingSize=40&productSet=total&query&sort=rel&timestamp=&'
                                 'viewType=list').format(k)
        elif l == '0015':
            url = section_url + ('?adQuery&catId=50000006&origQuery&pagingIndex={}&'
                                 'pagingSize=40&productSet=total&query&sort=rel&timestamp=&viewType=list').format(k)
        elif l == '8370':
            url = section_url + ('?adQuery&catId=50007256%2050007261%2050007253%'
                                 '2050007254%2050007255%2050007274&origQuery&pagingIndex={}&pagingSize=40&productSet=total&query&sort=rel&'
                                 'timestamp=&viewType=list').format(k)
        try:
            driver.get(url) #여기가 브라우저 여는 부분
            time.sleep(0.5)
        except:
            print('driver.get', l, k)
        time.sleep(0.5)
        for i in range(1, 41):
            try:
                title = driver.find_element('xpath',
                        '//*[@id="content"]/div[1]/div[2]/div/div[{}]/div/div/div[2]/div[1]/a'.format(i)).text
                title = re.compile('[^가-힣]').sub(' ', title)
                titles.append(title)
            except:
                print('find element', l, k, i)
        if k % 5 == 0:
            print(l, k)
            df_section_title = pd.DataFrame(titles, columns=['titles'])
            df_section_title['category'] = category[ca.index(l)]
            df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(l, k)) #저장
            #df_titles = pd.concat([df_titles, df_section_title], axis='rows', ignore_index=True)
            titles=[]
driver.close()
#df_titles.to_csv()



