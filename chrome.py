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
chrome_option.add_argument('--headless')
chrome_option.add_argument('log-level=3')
chrome_option.add_argument('--disable-gpu')
chrome_option.add_argument('--ignore-certificate-errors')
chrome_option.add_argument('--disable-images')
chrome_option.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=chrome_option)
driver.get('https://www.amazon.com/?currency=USD&language=en_US')
time.sleep(5)
driver.execute_script("document.body.style.zoom='0.9'")
# time.sleep(5)

final_result = []
with open('1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:       
        lineToStr = row[0]
        lineToList = lineToStr.split(' ')
        # print(lineToList)
        linkStr='s?k='
        # picPath = ''
        for i in range(len(lineToList)):
            linkStr= linkStr + lineToList[i] + '+'
            # picPath = picPath + lineToList[i] +'_'
        linkStr= linkStr[:-1]
        # picPath = picPath[:-1].replace('/','-')
        driver.maximize_window()

        for i in range(1,7):
            exits = 0
            driver.get('https://www.amazon.com/' + linkStr + '&page=' + str(i))
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup.select('div.s-main-slot')
            for a in soup.find_all('img'):
                flag_adver = 0
                flag_nature = 0
                link = str(a.get('src'))
                if ("61wZfCGn7AL._AC_UL320" in link):
                    keyword = linkStr.replace('+', ' ')[4:]
                    # print('\n')
                    
                    if flag_adver == 0:
                        for b in soup.find_all('a'):
                            b_link = str(b.get('href'))
                            if ("READY-PARD-Compression-Basketball-Tights" in b_link):
                                if (b_link.startswith('/gp')):
                                    print('\nthis is adver link : ')
                                    print(keyword+' page is : '+str(i))
                                    print(b_link)
                                    flag_adver = 1
                                    break
                    if flag_nature == 0:
                        for b in soup.find_all('a'):
                            b_link = str(b.get('href'))
                            if ("READY-PARD-Compression-Basketball-Tights" in b_link):
                                if (b_link.startswith('/READY-PARD-Compression-Basketball-Tights')):
                                    print('\nthis is nature link : ')
                                    print(keyword+' page is : '+str(i))
                                    print(b_link)
                                    flag_nature = 1
                                    break
                    if (flag_nature == 1 and flag_adver == 1):
                        print(keyword+"has get two keyword    ---------------------------")
                        exits = 1
                        break
            if exits == 1:
                break

driver.quit()

