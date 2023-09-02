import pytchat
import time
import csv
import pandas as pd
import os
from dotenv import load_dotenv
import shutil

#必要なデータをここにぶち込む
text_in = []
load_dotenv()
URL = os.environ.get("Youtube_URL")
Directory = os.environ.get('DILECTORY')

# PytchatCoreオブジェクトの取得
livechat = pytchat.create(video_id = URL)

while livechat.is_alive():
    # チャットデータの取得
    chatdata = livechat.get()
    for c in chatdata.items: 
 #csvファイルに変換して出力
        text_in.append(f"{c.datetime} {c.message} {c.amountString}")
        with open("Phalen_comment.csv",'w', newline='',encoding='utf-8') as f:
            for row in text_in:
                f.write(str(row) + "\n")
f.close()

#ファイルが変な場所に作られるので整理
shutil.move("Phalen_comment.csv", r'C:/Users/f/Desktop/comment取得/result_csv')
#カンマの右側に保存したいフォルダのパスをぶちこむ
