from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import pandas as pd
import re
import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

category = ['Fashion', 'Makeup', 'Interior', 'Digital', 'Food', 'Trip']
ca = ['03', '05', '31', '32', '20', '77']
fc = ['one', 'suit', 'tshirt', 'mtom', 'blouse', 'shirt', 'jeans']
mc = ['skin', 'clean', 'mask', 'basem', 'colorm', 'sun', 'nail']
ic = ['desk', 'chair', 'kidf', 'bed', 'storage', 'dressing', 'closet', 'sofa', 'lcloset', 'business']
dc = ['tv', 'projector', 'notebook', 'desktop', 'phone', 'wearable']
foc = ['rice', 'mixrice', 'fruit', 'ffruit', 'nut', 'rootv', 'chicken', 'pork']
tc = ['esasia', 'china', 'honkong', 'japan', 'usa', 'eu']

options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument('user_agent=' + user_agent)
options.add_argument('lang=ko_KR')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

pages = [50, 50, 50, 50, 50, 50]

df_titles = pd.DataFrame()


yt_url = 'https://www.gmarket.co.kr/'
driver = webdriver.Chrome()
driver.get(yt_url)
time.sleep(2)
for w in ca:
#fashion    fc = ['pants', 'one', 'suit', 'tshirt', 'mtom', 'blouse', 'shirt', 'jeans']
    # if w == '03':
    #     for z in fc:
    #         driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
    #         search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[2]/a')
    #         actions = webdriver.ActionChains(driver).move_to_element(search_box)
    #         actions.perform()
    #         time.sleep(2)
    #         driver.find_element(By.XPATH,
    #                             '//*[@id="box__category-all-layer"]/ul/li[2]/div/div/div[1]/ul/li[1]/a').click()
    #         if z == 'one':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
    #         elif z == 'suit':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[2]/a').click()
    #         elif z == 'tshirt':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
    #         elif z == 'mtom':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/a').click()
    #         elif z == 'blouse':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[3]/a').click()
    #         elif z == 'shirt':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[4]/a').click()
    #         elif z == 'jeans':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[1]/a').click()
    #         titles = []
    #         for k in range(1, 11):  # 페이지수
    #             if z == 'one':
    #                 u = driver.current_url + '&k=8&p={}'.format(k)
    #             elif z == 'suit':
    #                 u = driver.current_url + '&k=21&p={}'.format(k)
    #             elif z == 'tshirt':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'mtom':
    #                 u = driver.current_url + '&k=11&p={}'.format(k)
    #             elif z == 'blouse':
    #                 u = driver.current_url + '&k=4&p={}'.format(k)
    #             elif z == 'shirt':
    #                 u = driver.current_url + '&k=7&p={}'.format(k)
    #             elif z == 'jeans':
    #                 u = driver.current_url + '&k=17&p=2'.format(k)
    #             driver.get(u)
    #             time.sleep(0.5)
    #             for i in range(11, 100):  # 한 페이지의 타이틀 수
    #                 try:
    #                     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #                     title = driver.find_element('xpath','/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[{}]/div/div[2]/div[1]/div[1]/span/a'.format(i)).text
    #                     title = re.compile('[^가-힣]').sub(' ', title)
    #                     titles.append(title)
    #                 except:
    #                     print('find element', z, i)
    #             if k % 5 == 0:
    #                 print(k)
    #                 df_section_title = pd.DataFrame(titles, columns=['titles'])
    #                 df_section_title['category'] = category[ca.index(w)]
    #                 df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
    #                 titles = []
#makeup     mc = ['skin', 'clean', 'mask', 'basem', 'colorm', 'sun', 'nail']
    # elif w == '05':
    #     for z in mc:
    #         driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
    #         search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[2]/a')
    #         actions = webdriver.ActionChains(driver).move_to_element(search_box)
    #         actions.perform()
    #         time.sleep(2)
    #         driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[2]/div/div/div[3]/ul/li[1]/a').click()
    #         if z == 'skin':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
    #         elif z == 'clean':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
    #         elif z == 'mask':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/a').click()
    #         elif z == 'basem':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[1]/a').click()
    #         elif z == 'colorm':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[2]/a').click()
    #         elif z == 'sun':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[3]/a').click()
    #         elif z == 'nail':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[4]/li[1]/a').click()
    #         titles=[]
    #         for k in range(1, 11):  # 페이지수
    #             if z == 'skin':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'clean':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'mask':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'basem':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'colorm':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'sun':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'nail':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             driver.get(u)
    #             time.sleep(0.5)
    #             for i in range(11, 100):  # 한 페이지의 타이틀 수
    #                 try:
    #                     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #                     title = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[{}]/div[1]/div[2]/div[1]/div[1]/span/a'.format(i)).text
    #                     title = re.compile('[^가-힣]').sub(' ', title)
    #                     titles.append(title)
    #                 except:
    #                     print('find element', z, i)
    #             if k % 5 == 0:
    #                 print(k)
    #                 df_section_title = pd.DataFrame(titles, columns=['titles'])
    #                 df_section_title['category'] = category[ca.index(w)]
    #                 df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
    #                 titles = []
#interior   ic = ['desk', 'chair', 'kidf', 'bed', 'storage', 'dressing', 'closet', 'sofa', 'lcloset', 'business']
    # elif w == '31':
    #     for z in ic:
    #         driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
    #         search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[5]/a')
    #         actions = webdriver.ActionChains(driver).move_to_element(search_box)
    #         actions.perform()
    #         time.sleep(2)
    #         driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[5]/div/div/div[1]/ul/li[1]/a').click()
    #         if z == 'desk':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
    #         elif z == 'chair':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[2]/a').click()
    #         elif z == 'kidf':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[3]/a').click()
    #         elif z == 'bed':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
    #         elif z == 'storage':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/a').click()
    #         elif z == 'dressing':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[3]/a').click()
    #         elif z == 'closet':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[4]/a').click()
    #         elif z == 'sofa':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[1]/a').click()
    #         elif z == 'lcloset':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[2]/a').click()
    #         elif z == 'business':
    #             driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[3]/a').click()
    #         titles = []
    #         for k in range(1, 11):  # 페이지수
    #             if z == 'desk':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'chair':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'kidf':
    #                 u = driver.current_url + '&k=6&p={}'.format(k)
    #             elif z == 'bed':
    #                 u = driver.current_url + '&k=26&p={}'.format(k)
    #             elif z == 'storage':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'dressing':
    #                 u = driver.current_url + '&k=23&p={}'.format(k)
    #             elif z == 'closet':
    #                 u = driver.current_url + '&k=19&p={}'.format(k)
    #             elif z == 'sofa':
    #                 u = driver.current_url + '&k=20&p={}'.format(k)
    #             elif z == 'lcloset':
    #                 u = driver.current_url + '&k=26&p={}'.format(k)
    #             elif z == 'business':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             driver.get(u)
    #             time.sleep(0.5)
    #             for i in range(11, 100):  # 한 페이지의 타이틀 수
    #                 try:
    #                     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #                     title = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[{}]/div[1]/div[2]/div[1]/div[1]/span/a'.format(i)).text
    #                     title = re.compile('[^가-힣]').sub(' ', title)
    #                     titles.append(title)
    #                 except:
    #                     print('find element', z, i)
    #             if k % 5 == 0:
    #                 print(k)
    #                 df_section_title = pd.DataFrame(titles, columns=['titles'])
    #                 df_section_title['category'] = category[ca.index(w)]
    #                 df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
    #                 titles = []
#digital    dc = ['tv', 'projector', 'notebook','desktop', 'phone', 'wearable']
    if w == '32':
        for z in dc:
            if z == 'tv':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[3]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
            elif z == 'projector':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[3]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
            elif z == 'notebook':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[1]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
            elif z == 'desktop':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[1]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[1]/a').click()
            elif z == 'phone':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[2]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
            elif z == 'wearable':
                driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
                search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[6]/a')
                actions = webdriver.ActionChains(driver).move_to_element(search_box)
                actions.perform()
                time.sleep(2)
                driver.find_element(By.XPATH,
                                    '//*[@id="box__category-all-layer"]/ul/li[6]/div/div/div[2]/ul/li[1]/a').click()
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[5]/li[1]/a').click()
            titles = []
            for k in range(1, 11):  # 페이지수
                if z == 'tv':
                    u = driver.current_url + '&k=27&p={}'.format(k)
                elif z == 'projector':
                    u = driver.current_url + '&k=8&p={}'.format(k)
                elif z == 'notebook':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'desktop':
                    u = driver.current_url + '&k=26&p={}'.format(k)
                elif z == 'phone':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'wearable':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                driver.get(u)
                time.sleep(0.5)
                for i in range(11, 100):  # 한 페이지의 타이틀 수
                    try:
                        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        title = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[{}]/div/div[2]/div[1]/div[1]/span/a'.format(i)).text
                        title = re.compile('[^가-힣]').sub(' ', title)
                        titles.append(title)
                    except:
                        print('find element', z, i)
                if k % 5 == 0:
                    print(k)
                    df_section_title = pd.DataFrame(titles, columns=['titles'])
                    df_section_title['category'] = category[ca.index(w)]
                    df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
                    titles = []
#food       foc = ['rice', 'mixrice', 'fruit', 'ffruit', 'nut', 'rootv', 'leafv', 'chicken', 'pork']
    elif w == '20':
        for z in foc:
            driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
            search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[4]/a')
            actions = webdriver.ActionChains(driver).move_to_element(search_box)
            actions.perform()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[4]/div/div/div[1]/ul/li[1]/a').click()
            if z == 'rice':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[1]/a').click()
            elif z == 'mixrice':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[1]/li[2]/a').click()
            elif z == 'fruit':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[1]/a').click()
            elif z == 'ffruit':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[2]/a').click()
            elif z == 'nut':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[2]/li[3]/a').click()
            elif z == 'rootv':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[3]/li[1]/a').click()
            elif z == 'chicken':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[4]/li[1]/a').click()
            elif z == 'pork':
                driver.find_element(By.XPATH, '//*[@id="gnb"]/ul[4]/li[2]/a').click()
            titles = []
            for k in range(1, 11):  # 페이지수
                if z == 'rice':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'mixrice':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'fruit':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'ffruit':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'nut':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'rootv':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                elif z == 'chicken':
                    u = driver.current_url + '&k=23&p={}'.format(k)
                elif z == 'pork':
                    u = driver.current_url + '&k=30&p={}'.format(k)
                driver.get(u)
                time.sleep(0.5)
                for i in range(11, 100):  # 한 페이지의 타이틀 수
                    try:
                        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                        title = driver.find_element('xpath', '/html/body/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div[{}]/div[1]/div[2]/div[1]/div[1]/span/a'.format(i)).text
                        title = re.compile('[^가-힣]').sub(' ', title)
                        titles.append(title)
                    except:
                        print('find element', z,  i)
                if k % 5 == 0:
                    print(k)
                    df_section_title = pd.DataFrame(titles, columns=['titles'])
                    df_section_title['category'] = category[ca.index(w)]
                    df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
                    titles = []
#trip       tc = ['esasia', 'china', 'honkong', 'japan', 'usa', 'eu']
    # elif w == '77':
    #     for z in tc:
    #         driver.find_element(By.XPATH, '//*[@id="button__category-all"]').click()
    #         search_box = driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[9]/a')
    #         actions = webdriver.ActionChains(driver).move_to_element(search_box)
    #         actions.perform()
    #         time.sleep(2)
    #         driver.find_element(By.XPATH, '//*[@id="box__category-all-layer"]/ul/li[9]/div/div/div[1]/ul/li[3]/a').click()
    #         if z == 'esasia':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[1]/a').click()
    #         elif z == 'china':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[2]/a').click()
    #         elif z == 'honkong':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[3]/a').click()
    #         elif z == 'japan':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[4]/a').click()
    #         elif z == 'usa':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[7]/a').click()
    #         elif z == 'eu':
    #             driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[1]/div[1]/ul/li[6]/a').click()
    #         titles = []
    #         for k in range(1, 11):  # 페이지수
    #             if z == 'esasia':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'china':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'honkong':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'japan':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'usa':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             elif z == 'eu':
    #                 u = driver.current_url + '&k=30&p={}'.format(k)
    #             driver.get(u)
    #             time.sleep(0.5)
    #             for i in range(5, 70):  # 한 페이지의 타이틀 수
    #                 try:
    #                     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #                     title = driver.find_element('xpath',
    #                                                 '/html/body/div[2]/div[4]/div[3]/div[9]/table/tbody/tr[{}]/td[1]/div/div[2]/div[2]'.format(
    #                                                     i)).text
    #                     title = re.compile('[^가-힣]').sub(' ', title)
    #                     titles.append(title)
    #                 except:
    #                     print('find element', z, i)
    #             if k % 5 == 0:
    #                 print(k)
    #                 df_section_title = pd.DataFrame(titles, columns=['titles'])
    #                 df_section_title['category'] = category[ca.index(w)]
    #                 df_section_title.to_csv('./crawling_data/data_{}_{}.csv'.format(z, k))
    #                 titles = []

driver.close()