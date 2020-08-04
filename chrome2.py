#-*-coding: utf-8 -*-
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#pip3 install pillow selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert 
from PIL import Image
import time
import csv
import re
import sys
import datetime
import string
import os
from bs4 import BeautifulSoup
import urllib.request


nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-images')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.amazon.com/?currency=USD&language=en_US')
time.sleep(5)
driver.execute_script("document.body.style.zoom='0.9'")
driver.get('chrome://version/')
chromeversion = driver.find_element_by_xpath('//*[@id="version"]/span[1]').text
print('chrome version is : ' + chromeversion)

counts = 0
final_result = {}
with open('2.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:       
        lineToStr = row[0]
        lineToList = lineToStr.split(' ')
        linkStr='s?k='
        for i in range(len(lineToList)):
            linkStr= linkStr + lineToList[i] + '+'
            # picPath = picPath + lineToList[i] +'_'
        linkStr= linkStr[:-1]
        # picPath = picPath[:-1].replace('/','-')
        driver.maximize_window()
        counts = 1 + counts
        print('this is counts : ' , str(counts))
        count = 0

        for i in range(1,7):
            exits = 0
            driver.get('https://www.amazon.com/' + linkStr + '&page=' + str(i))
            if count == 0:
                count = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').text
                count = count.split(' ')[-3].replace(',','')
            print(count)
            # page_nums = driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[4]').get_attribute('class')
            # print(page_nums,'111111111')
            
            # for i in range(page_nums):
            #     print (i)
            #     asindata=driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]')
            #     print(asindata)
            # print(divs)
            # divs1 = driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]')
            # print(len(divs1))
            # print('22222222')
            # print(divs1)

#             soup = BeautifulSoup(driver.page_source, "html.parser")
#             soup.select('div.s-main-slot')
#             for a in soup.find_all('img'):
#                 flag_adver = 0
#                 flag_nature = 0
#                 link = str(a.get('src'))
#                 if ("61wZfCGn7AL._AC_UL320" in link):
#                     keyword = linkStr.replace('+', ' ')[4:]
#                     if (keyword not in final_result):
#                         final_result[keyword] = {'adver':[],'nature':[]}
#                     if flag_adver == 0:
#                         for b in soup.find_all('a'):
#                             b_link = str(b.get('href'))
#                             if ("READY-PARD-Compression-Pants-Tights" in b_link):
#                                 if (b_link.startswith('/gp')):
#                                     flag_adver = 1
#                                     final_result[keyword]['adver'] = [str(i)]
#                                     break
#                     if flag_nature == 0:
#                         for b in soup.find_all('a'):
#                             b_link = str(b.get('href'))
#                             if ("READY-PARD-Compression-Pants-Tights" in b_link):
#                                 if (b_link.startswith('/READY-PARD-Compression-Pants-Tights')):
#                                     flag_nature = 1
#                                     ASIN = b_link.split('/')[3]
#                                     NUM = b_link.split('-')[-1]
#                                     final_result[keyword]['nature'] = [str(i), ASIN, NUM]
#                                     break
#                     if (flag_nature == 1 and flag_adver == 1):
#                         print(keyword+" has get two keyword    ---------------------------")
#                         exits = 1
#                         break
#             if exits == 1:
#                 break
# print(final_result)
driver.quit()


# csv_columns = ['1','2','3','4','5','6']
# final_result= {'knee pad basketball': {'adver': [], 'nature': ['1', 'B08CS8YFK5', '8']}, 'basketball pants with knee pads': {'adver': ['1'], 'nature': ['1', 'B08CS8YFK5', '7']}, 'youth basketball leggings with knee pads': {'adver': ['1'], 'nature': ['1', 'B08CS8YFK5', '7']}}
# csv_file = 'data.csv'

# resutls  = []
# for k , v  in final_result.items():
#     resutls  = []
#     resutls.append(k)
#     if isinstance(v,dict):
#         for a,b in v.items():
#             for i in range(len(b)):
#                 # if (b[i]) is None:
#                 #     b[i] = 'None'
                
                
#                 if b[i]:
#                     pass
#                 else:
#                     b[i] = 'None'
#                 print(b[i])
#                 resutls.append(b[i])
                
#     print(resutls)
#     print('\n')


# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in final_result:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")
# for k,v in final_result.items():
#     c = ''
#     d = ''
#     for a,b in v.items():
#         # print('k is : ',k,' a is : ', a , ' b is : ', b)
#         a = c
#         b = d
#     print (k,c,d)


# def traverse(value, key=None):
#     if isinstance(value, dict):
#         for k, v in value.items():
#             yield from traverse(v, k)
#     else:
#         yield key, value
# def myprint(d):
#     for k, v in traverse(d):
#         print(f"{k} : {v}")

# myprint(final_result)

# def print_nested(d):
#     if isinstance(d, dict):
#         for k, v in d.items():
#             print_nested(v)
#     elif hasattr(d, '__iter__') and not isinstance(d, str):
#         for item in d:
#             print_nested(item)
#     elif isinstance(d, str):
#         print(d)

#     else:
#         print(d)

# print_nested(final_result)