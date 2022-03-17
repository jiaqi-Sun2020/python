import requests
import re
from lxml import etree
url = "https://buff.163.com/goods/42530"
headers ={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
':authority': 'buff.163.com'

}
#text 文本文件 ,contant二进制文件, json()对象文件
data = requests.get(url,headers).text   #获取了网页页面的响应   #并且要用utf-8解析   .content.decode('utf-8')
print(data)
selector = etree.HTML(data)
#data = selector.xpath("/html/body/div[6]/div/div[5]")#/strong[class='f_Strong']
# #复制完整的xpath#'/html/body/div[6]/div/div[5]/table/tbody/tr[2]/td[5]/div[1]/strong'
#一部分xpath //*[@id="sell_order_220303T1740846366"]/td[5]/div[1]/strong
data = selector.xpath('/html/body/div[6]/div/div[5]')

print('='*20)
print(data)



#结果发现这个还是获取post包对html进行填充的!!!!!我去搞post请求了!!!!!