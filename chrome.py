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
chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_argument('--disable-images')
chrome_option.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get('https://www.amazon.com/?currency=USD&language=en_US')
time.sleep(15)
driver.execute_script("document.body.style.zoom='0.9'")
# time.sleep(5)

# #获取当前目录所有的图片，保存在对应变量中
existFile = []
# for filename in os.listdir('.'):
#     if filename.endswith('.png'):
#         existFile.append(filename.strip('.png').rstrip(string.digits).replace('_', ' ').rstrip())

# print(existFile)
# #读取ASIN csv 文件

# B08CS7S1QQ
# B08CS6WSN4
# B08CS8YFK5
# B08CS6PT7P
# B08CS8TZ3Y
# B08CS7F65L

num = 0
times = 1
final_result = []
with open('1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:       
        lineToStr = row[0]
        if lineToStr in existFile:
            print ('this pic has been finished')
            print(lineToStr)
        else:
            lineToList = lineToStr.split(' ')
            print(lineToList)
            linkStr='s?k='
            picPath = ''
            for i in range(len(lineToList)):
                linkStr= linkStr + lineToList[i] + '+'
                picPath = picPath + lineToList[i] +'_'
            linkStr= linkStr[:-1]
            picPath = picPath[:-1].replace('/','-')
            # s?k=workout+turf   linkStr format.
            linkfront = 'https://www.amazon.com/'
            driver.maximize_window()
            results = []
            for i in range(1,7):
                driver.get('https://www.amazon.com/' + linkStr + '&page=' + str(i))
                soup = BeautifulSoup(driver.page_source, "html.parser")
                soup.select('div.s-main-slot')
                for a in soup.find_all('a'):
                    link = str(a.get('href'))
                    results.append(link)
                result = set(results)
                for i in result:
                    if 'B08CS7S1QQ' in i:
                        final_result.append(i)
                        print(1)
                        print(i)
                        break
                    elif 'B08CS6WSN4' in i:
                        final_result.append(i)
                        print(2)
                        print(i)
                        break
                    elif 'B08CS8YFK5' in i:
                        final_result.append(i)
                        print(3)
                        print(i)
                        break
                    elif 'B08CS6PT7P' in i:
                        final_result.append(i)
                        print(4)
                        print(i)
                        break
                    elif 'B08CS8TZ3Y' in i:
                        final_result.append(i)
                        print(i)
                        print(5)
                        break
                    elif 'B08CS7F65L' in i:
                        final_result.append(i)
                        print(6)
                        print(i)
                        break

print(set(final_result))
driver.quit()


