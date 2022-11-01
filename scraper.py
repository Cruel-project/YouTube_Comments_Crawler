from asyncio.sslproto import _DO_HANDSHAKE
from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import warnings 

import file_witer

warnings.filterwarnings('ignore')



#유튜브 불러오기
wb = Workbook(write_only=True)
ws = wb.create_sheet()

fl = file_witer
    
def get_comments(input):
    fl.save_video_id(input)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://youtu.be/" + input)
    driver.implicitly_wait(3)

    time.sleep(1.5)

    driver.execute_script("window.scrollTo(0, 2)")
    time.sleep(3)

    #스크롤
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.5)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(1.5)

    #프리미엄 창 끄기
    try:
        driver.find_element(By.ID, 'more-replies').click()
    except:
        pass

    #댓글 가져오기
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    id_list = soup.select("div#header-author > h3 > #author-text > span")
    comment_list = soup.select("yt-formatted-string#content-text")

    id_final = []
    comment_final = []

    for i in range(len(comment_list)):
        temp_id = id_list[i].text
        temp_id = temp_id.replace('\n', '')
        temp_id = temp_id.replace('\t', '')
        temp_id = temp_id.replace('    ', '')
        id_final.append(temp_id) # 댓글 작성자

        temp_comment = comment_list[i].text
        temp_comment = temp_comment.replace('\n', '')
        temp_comment = temp_comment.replace('\t', '')
        temp_comment = temp_comment.replace('    ', '')
        comment_final.append(temp_comment) # 댓글 내용
        
    #댓글 저장
    pd_data = {"아이디" : id_final , "댓글 내용" : comment_final}
    youtube_pd = pd.DataFrame(pd_data)

    youtube_pd.to_excel('result.xlsx')
    print("="*16)
    print("저장 완료!")
    print("경로: result.xlsx")
    print("="*16)

