import requests
from  bs4  import BeautifulSoup
import json
def get_web(str):
    web = str.split('"')[1]
    return web

def Nutrition_name(dt):
    Nutrition_list = []
    for name in dt:
        name = name.text
        Nutrition_list.append(name)
    return Nutrition_list[2:]
def Nutrition_value(dd):
    Nutrition_list = []
    for name in dd:
        name = name.text
        Nutrition_list.append(name)
    return Nutrition_list[2:]


def get_name_web(all_dicts,page):
    url = "https://www.boohee.com/food/group/4?page={page}".format(page=page)
    base_url = "https://www.boohee.com"
    head={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
    }


    get = requests.get(url=url,headers=head)
    #==============
    # with open('./水果.html', 'w',encoding="utf-8") as f:
    #     f.write(get.text)
    #==============
    selector = BeautifulSoup(get.text,"html.parser")#指定html解析器


    name_datas = selector.find_all("div",class_="text-box pull-left")

    for name_data in name_datas:
        dict = {}
        data= name_data.find("a")
        #print(data.text.split("，")[0])
        dict["name"] = data.text.split("，")[0]  #， 是中文的！！！
        add_web = get_web(str(data))
        web =base_url +add_web
        dict["web"] = web
        all_dicts.append(dict)
    return  all_dicts


def get_continer(all_dicts):
    for dict in all_dicts:
        url = dict['web']
        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39",
        }
        get_fruits = requests.get(url=url, headers=head)
        selector = BeautifulSoup(get_fruits.text, "html.parser")  # 指定html解析器   <div class="content">
        continer = selector.find_all("span", class_="dt")  # 找到营养名字
        value = selector.find_all("span", class_="dd")
        # print(continer,value,)
        N_name = Nutrition_name(continer)
        N_value = Nutrition_value(value)
        # print(N_name)
        # print(N_value)
        for i, name in enumerate(N_name):
            dict[name] = N_value[i]
    return all_dicts

#===========main

all_dicts = []
for page in range(0,1):  #
    all_dicts = get_name_web(all_dicts,page)  #获取到了名字和对应水果网页   (page是对应的页数)
# print(all_dicts)
all_dicts = get_continer(all_dicts)


print(all_dicts)
    #print(get_fruits.text)
    #print(continer)
with open('./fruits.json', 'w', encoding='utf-8') as fp:
    json.dump(all_dicts, fp=fp, ensure_ascii=False)


