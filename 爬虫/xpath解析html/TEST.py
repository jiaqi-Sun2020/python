import requests
import json

headers = {
    #':path': '/api/market/goods/sell_order?game=csgo&goods_id=42530&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1646307155097',
    'referer': 'https://buff.163.com/goods/871196',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'cookie':'cookie: _ntes_nnid=273aa6cd2c9b4834de70916de9b28928,1636197670821; UM_distinctid=17cf4fb278885-029e8a313b0acb-561a135a-1fa400-17cf4fb2789f88; _ntes_nuid=273aa6cd2c9b4834de70916de9b28928; unisdk_udid=71d4d9f8b13b373044a18cf3a46299b0; NTES_P_UTID=HQOJqyJodQV7kZEg99eDIWCxetfxGnhd|1639838795; nts_mail_user=sjq1623958071@163.com:-1:1; timing_user_id=time_ysX566F1ZC; Device-Id=S93qHFLLAFCsOwFsn3gZ; _ga=GA1.2.1996916940.1646207084; _gid=GA1.2.784730422.1646298624; Locale-Supported=zh-Hans; game=csgo; NTES_YD_SESS=xLY505SdWnOpaxMlem6vRoKedKN_HMtRszPrA1BKJP15NK67NXivTdxNfyImrDtKF4VPE7xporAVEKrFX4DgYQP7ZDvXhMG3LCgQ.9B_pBVkr.1JRKGDMe5pxIrEHDGJmJJidZOnZ1Xf3ActCs1CS_dHN.laPYA7AcCOfJQ2Y0_dJ8_afk8URRUeXIAzdFMqZYWVGpNb.C.VfMDqSld.hEvVUIUrPIMSep57exgJ9qiQH; S_INFO=1646399177|0|0&60##|15306260007; P_INFO=15306260007|1646399177|1|netease_buff|00&99|null&null&null#jis&320500#10#0|&0|null|15306260007; remember_me=U1101189625|31rgSZ68DsNQzjUN6DbEI10x7WkGt3k7; session=1-M9v-klJoORR3N9NaV-rybJIYi7f6CSv7NXnqWVkXouum2037141153; csrf_token=IjNjZTUxZjE0MzFjMjY2YTcwYTY2YWYzNzhiMWFlNjczZTBlYjFiZGEi.FQO5Zg.F1BdCBmbTeSpawoI9ZHbj91M0bc'
}
url = 'https://buff.163.com/api/market/goods/sell_order'

id =42530
tag_ids = 871196

param = {
    'game': 'csgo',
    'goods_id': str(id),
    'page_num': '1',
    'sort_by': 'default',
    'mode':'',
    'allow_tradable_cooldown': '1',
    '_': '1646307155097'
}
param['tag_ids'] = str(tag_ids)


get_data = requests.get(url = url,params=param,headers=headers)#获取请求文件


get_data.content.decode("utf-8")
obj = get_data.json()
print(obj)
with open('./test.json', 'w', encoding='utf-8') as fp:
    json.dump(obj, fp=fp, ensure_ascii=False)