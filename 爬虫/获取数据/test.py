import requests
import json
from xlutils.copy import copy
import os
import time
import xlwt
import xlrd
from openpyxl import load_workbook
import numpy as np
global filename
filename = "./list.xlsx"

# headers = {
#         'apptype': '1',
#         'Content-Type':'application/json',
#         'authority': 'api.youpin898.com',
#         'method': 'POST',
#         'path': '/api/youpin/commodity/purchase/find',
#         'origin': 'https://www.youpin898.com' ,
#         'referer': 'https://www.youpin898.com/' ,
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
#     }
# url = 'https://api.youpin898.com/api/youpin/commodity/purchase/find'
#
# pagesize =100
# Payload ={'templateId': "43951", 'pageIndex': 1, 'pageSize': pagesize}
# Payload = json.dumps(Payload)
# #print(Payload)
# response = requests.post(url=url, data = Payload, headers=headers)
# #改成json文件
# obj = response.json()
# #print(obj[str('Data')][str('CommodityList')])#获取到了json里面Msg的文件
#
# #print(obj)
# #持久化存储(存储了获取的json文件)
# with open('./道具信息_2.json','w',encoding= 'utf-8') as fp:
#         json.dump(obj,fp = fp, ensure_ascii = False)
#
# sell_price = []
# sell_name = []
# XXX = obj[str('data')][str('response')]
#
# #根据获取的数据来得到出租的人和物
# for T in XXX :
#         sell_name.append(T[str('userNickname')])  # 获取名字
#         sell_price.append(float(T[str('unitPrice')]/100))
# min_sellprice = min(sell_price)
# sellname = sell_name[np.argmin(sell_price)]
# print(sell_price)
# print(sellname)



headers = {
        'apptype': '1',
        'Content-Type': 'application/json',
        'authority': 'api.youpin898.com',
        'method': 'POST',
        'path': '/api/youpin/commodity/purchase/find',
        'origin': 'https://www.youpin898.com',
        'referer': 'https://www.youpin898.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
}
url = 'https://api.youpin898.com/api/youpin/commodity/purchase/find'
pagesize =100
Payload ={'templateId': "43951", 'pageIndex': 1, 'pageSize': pagesize}
Payload= json.dumps(Payload)
# print(Payload)
response = requests.post(url=url, data=Payload, headers=headers)
# 改成json文件
obj = response.json()
# print(obj[str('Data')][str('CommodityList')])#获取到了json里面Msg的文件

# print(obj)
# 持久化存储(存储了获取的json文件)
with open('./道具信息_2.json', 'w', encoding='utf-8') as fp:
        json.dump(obj, fp=fp, ensure_ascii=False)

buy_price = []
buy_name = []
XXX = obj[str('data')][str('response')]

# 根据获取的数据来得到出租的人和物
for T in XXX:
        buy_name.append(T[str('userNickname')])  # 获取名字
        buy_price.append(float(T[str('unitPrice')] / 100))
max_buyprice = max(buy_price)
buyname = buy_name[np.argmax(buy_price)]
print(max_buyprice,buyname)