import pandas as pd
import os
#创建输出文件夹
os.makedirs("output",exist_ok=True)
path = r"output/2.txt"
all_str = []

def Splicing_vlan(vlan):
    vlan_str = ""
    #print(vlan)
    #print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(vlan,int):
        vlan_str =" {}".format(vlan)
    else:
        for value in vlan:
            vlan_str = vlan_str + " " + str(value)
    return vlan_str

def init_trunk(port,vlan,all_str):   #交换机接交换机
    #拼接vlan数据
    vlan_str = Splicing_vlan(vlan)
    #print(vlan_str)

    wr = "#\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         "port link-type trunk\n" \
         "port trunk allow-pass vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_access(port,vlan,all_str):  #交换机接电脑
    vlan_str = Splicing_vlan(vlan)
    #print(vlan_str)
    wr = "#\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         "port link-type access\n" \
         "port default vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_hybrid(port,tag_vlan,untag_vlan,all_str): #混合接口
    tag_vlan_str = Splicing_vlan(tag_vlan)
    untag_vlan_str = Splicing_vlan(untag_vlan)
    #print(vlan_str)
    wr = "#\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         "port link-type hybrid\n" \
         "port hybrid pvid vlan{untag_vlan}\n"\
         "port hybrid untagged vlan{untag_vlan}\n"\
         "port hybrid tagged vlan{tag_vlan}\n".format(port=port, tag_vlan=tag_vlan_str,untag_vlan=untag_vlan_str)
    all_str.append(wr)
    return all_str







filename = "sw.xlsx"

file = pd.read_excel(filename,sheet_name=0)#获取第一个表单
#print(file)

dict_datas = []
for row_index in file.index.values:
    row_data = file.loc[row_index, ['端口', '类型', 'VLAN']].to_dict()
    dict_datas.append(row_data)

#print(dict_datas)

#调整vlan空的配置
for data in dict_datas:
    container =[]
    VLAN = str(data['VLAN'])
    VLAN =VLAN.split(" ")
    for vlan in VLAN:
        container.append(int(vlan))
    data['VLAN'] = container
    if data['类型']=="HYBRID":
        data["tag_vlan"] =container[0]
        data["untag_vlan"] = container[1:]

print(dict_datas)


for data in dict_datas:
    port = data["端口"]
    if data['类型']=="HYBRID":
        all_str = init_hybrid(port,data["tag_vlan"],data["untag_vlan"],all_str)
    if data['类型']=="ACCESS":
        all_str = init_access(port, data["VLAN"], all_str)
    if data['类型'] == "TRUNK":
        all_str = init_access(port, data["VLAN"], all_str)


s ="".join(all_str)#对其进行拼接
print(s)
with open(path, 'w', encoding='UTF-8') as txt:
    txt.write(s)