import os


#创建输出文件夹
os.makedirs("output",exist_ok=True)
path = r"output/1.txt"
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






'''
在此处编辑信息
在对应列表中编写对应的数据信息
'''
trunk_tip=[
# (port, vlan)
    (2,(1,2,3)),
    (4,(1,2,3)),
    (6,(1,2,3)),
    (8,(1,2,3)),
    (10,(1,2,3)),
]
access_tip = [
# (port, vlan)
    (1,(1)),
    (3,(2)),
    (5,(1)),
    (7,(2)),
    (9,(3)),
]

hybrid_tip = [
   #(port, tag, untag)
    (27,(3,4,5),(1)),
    (35,(3,4,5),(2)),
    (19,(3,4,5),(1)),
    (51,(3,4,5),(2)),
    (33,(3,4,5),(3)),
]
for port,vlan in trunk_tip:
    all_str = init_trunk(port,vlan,all_str)

for port,vlan in access_tip:
    all_str = init_access(port,vlan,all_str)

for port,tag_vlan,untag_vlan in hybrid_tip:
    all_str = init_hybrid(port,tag_vlan,untag_vlan,all_str)



s ="".join(all_str)#对其进行拼接
print(s)
with open(path, 'w', encoding='UTF-8') as txt:
    txt.write(s)



