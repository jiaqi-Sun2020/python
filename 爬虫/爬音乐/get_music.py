import requests
import os
import re
from lxml import etree
import html
os.makedirs('music',exist_ok=True)

url = 'https://music.163.com/#/discover/toplist?id=2809513713'   #获取音乐列表
head = {
"cookie": "_ntes_nnid=273aa6cd2c9b4834de70916de9b28928,1636197670821; UM_distinctid=17cf4fb278885-029e8a313b0acb-561a135a-1fa400-17cf4fb2789f88; _ntes_nuid=273aa6cd2c9b4834de70916de9b28928; unisdk_udid=71d4d9f8b13b373044a18cf3a46299b0; NTES_P_UTID=HQOJqyJodQV7kZEg99eDIWCxetfxGnhd|1639838795; nts_mail_user=sjq1623958071@163.com:-1:1; _iuqxldmzr_=32; NMTID=00OL5sweNCFRNsnwke7n55BoxG01w0AAAF9zgJY-Q; WEVNSM=1.0.0; WNMCID=utaakf.1639838801793.01.0; WM_TID=iCKlKe%2FgIdZFRRVQEFJv96C9VFwj0rNP; _ga=GA1.2.1996916940.1646207084; timing_user_id=time_z5DVq2xMfe; P_INFO=15306260007|1647485103|1|netease_buff|00&99|null&null&null#jis&320400#10#0|&0||15306260007; WM_NI=i5W5zUMYjWHdwqOGYiFIAetrSRPFEzIrJHluVMv6XVm6PlQTvPP4d3Z6zN%2F%2B9GATz6HTEy3IjTKnOen9NuH5cAOLPIZXyYLErMqEkpT2TYxYSuhjveScv%2FVv2voo4GD6MXY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eedad966acb4a3ace15e87e78fa6d15f879e8b84f57bfbee9785ca6ea7b8add7ef2af0fea7c3b92aabeb99d6f95f8f87a6b8cb70b5af81a8dc6386978f86f77a918ea0a7c8728bae86a9ef7f9693bad7db5eafeaa08dd460b690a0d5e7399aeab6afae21fb998fb5f93e8c8c8b9ab243aa8c858fce6faee78296cb3fa19f81add3439a88b7bacf4fb293bfa6ea7c98ee9cbafb5391aba88bf56f91bdbad0d57ef2aaa190b74d88ea83b9dc37e2a3; playerid=33970720; JSESSIONID-WYYY=NoDPFcDR4ushRalbWrKRyd5eHh0DC5QmSZkW2IujTJii5%2BvPWAnIYVCKuDf7XkpeOcJC5a9rTO8%2BhGwG9YAjWQyehijwrI%5CDSZyVdoSPXsEqwdoI437%2Baj2Sfu4KlR3KvY%2FCtBU3MwsWONi3PZuB3oD6VfZBf4uF5qh4JV%5Cy%2B9gIVF%2FZ%3A1647833234928",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
}

get_title = requests.get(url=url,headers=head)
print(get_title.text)

with open('./test.html', 'w',encoding="utf-8") as f:
    f.write(get_title.text)

# selector = etree.HTML(data)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', get_title.text)
print(html_data)




#http://music.163.com/song/media/outer/url?id=1859245776  //下载地址

