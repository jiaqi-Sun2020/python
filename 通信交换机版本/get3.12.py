import pandas as pd
import numpy as np
import os


all_str = []   #这个为编写的txt

#==========================================================================================
def Splicing_vlan(vlan):#列表中的元素按规定拼接成字符串
    vlan_str = ""
    #print(vlan)
    #print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(vlan,int):
        vlan_str =" {}".format(vlan)
    else:
        for value in vlan:
            vlan_str = vlan_str + " " + str(value)
    return vlan_str

def Splicing_port(ports):   #列表中的元素按规定拼接成字符串
    port_str = ""
    #print(vlan)
    #print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(ports,int):
        port_str =" {}".format(ports)
    else:
        for value in ports:
            port_str = port_str + " " + str(value)
    return port_str

def init_trunk(port,vlan,all_str):   #交换机接交换机
    #拼接vlan数据
    vlan_str = Splicing_vlan(vlan)
    #print(vlan_str)

    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_access(port,vlan,all_str):  #交换机接电脑
    vlan_str = Splicing_vlan(vlan)
    #print(vlan_str)
    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type access\n" \
         " port default vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_hybrid(port,tag_vlan,untag_vlan,all_str): #混合接口
    tag_vlan_str = Splicing_vlan(tag_vlan)
    untag_vlan_str = Splicing_vlan(untag_vlan)
    #print(vlan_str)
    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type hybrid\n" \
         " port hybrid pvid vlan{untag_vlan}\n"\
         " port hybrid untagged vlan{untag_vlan}\n"\
         " port hybrid tagged vlan{tag_vlan}\n".format(port=port, tag_vlan=tag_vlan_str,untag_vlan=untag_vlan_str)
    all_str.append(wr)
    return all_str
def init_ETH_trunk_add(change_ports,trunk_port,all_str):
    for port in change_ports:
        wr = "#\n" \
             "interface GigabitEthernet0/0/{port}\n" \
             " eth-trunk {trunk_port}    \n" \
             " lacp priority 100    \n".format(port = port,trunk_port =trunk_port)
        all_str.append(wr)
    return all_str


def init_ETH_trunk(port,vlan,all_str,add_ports):   #聚合接口
    vlan_str = Splicing_vlan(vlan)
    wr = "#\n" \
         " interface Eth-Trunk{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n" \
         " mode lacp \n" \
         " lacp preempt enable\n" \
         " max active-linknumber 4  \n" \
         " lacp preempt delay 10   \n".format(port=port, vlan=vlan_str)
    all_str.append(wr)  #加入了定义
    all_str = init_ETH_trunk_add(add_ports,port,all_str)
    return all_str
# def init_PPPOE(port,username,password):

#==========================================================================================

#如果值为nan那么设置为9999
def get_item(file,clomn):
    dict_datas = []
    for row_index in file.index.values:
        row_data = file.loc[row_index,clomn].to_dict()
        dict_datas.append(row_data)
    return dict_datas

#如果值为nan那么设置为9999
def claear_nan(file,repalce_numb):
    for colmn in list(file):
        file[colmn].fillna(repalce_numb, inplace=True)



#================
#
#主函数
#
#================
os.makedirs("output",exist_ok=True)   #建立文件夹
path = r"output/3.txt"                #建立txt

file = pd.read_excel("./sq/sw3.12.xlsx",sheet_name=0)#获取对应的表单
#print(file)
claear_nan(file,9999)     #清除nan值变成9999

dictorys = get_item(file,list(file))     #把excel变成字典列表

#调整字典==
for dictory in dictorys:                 #取出字典列表中的每一个字典
    contain = []
    VLAN = str(dictory['VLAN'])
    VLAN = VLAN.split(" ")
    if VLAN is not None:   #对字典的数据进行分离操作
        for t in VLAN:
            contain.append(int(t))
        dictory['VLAN'] = contain
        if dictory['类型']=="HYBRID":
            dictory["tag_vlan"] =contain[0]
            dictory["untag_vlan"] = contain[1:]
        #print(dictory)
#====
#编写txt
for data in dictorys:  #遍历列表
    port = data["端口号"]
    if data["接口"]=="interface GigabitEthernet":
        if data['类型']=="HYBRID":
            all_str = init_hybrid(port,data["tag_vlan"],data["untag_vlan"],all_str)
        if data['类型']=="ACCESS":
            all_str = init_access(port, data["VLAN"], all_str)
        if data['类型'] == "TRUNK":
                all_str = init_trunk(port, data["VLAN"], all_str)
    if data['接口']=='interface Eth-Trunk':
        add_ports = data['TRUNK_PORT'].split(",")  #关于,号分离
        #print(port)
        all_str = init_ETH_trunk(port, data["VLAN"], all_str,add_ports)


s ="".join(all_str)#对其进行拼接
print(s)
with open(path, 'w', encoding='UTF-8') as txt:
    txt.write(s)






