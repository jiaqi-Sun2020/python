import requests
import  re
from lxml import etree
url = "https://www.boohee.com/food/group/4"
head={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39?page={page}".format(page=1),
}
# parmer={
#     "page":"1"
# }

get = requests.get(url=url,headers=head)
print(get.text)
#==============
with open('./水果.html', 'w',encoding="utf-8") as f:
    f.write(get.text)
# /html/body/div[1]/div[2]/div[2]/div/div[2]/ul/li[1]/div[2]/h4/a
selector = etree.HTML(get.text)#转到了xpath的文件下
# html_data = re.findall('<li><a href="/shiwu/"></a>', get.text)
# print(html_data)
data = selector.xpath('/html/body/div[1]/div[2]')
print(data)