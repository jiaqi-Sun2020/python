import pandas as pd
import numpy as np
import os

all_str = []  # 这个为编写的txt


# ==========================================================================================
def Splicing_vlan(vlan,space=True):  # 列表中的元素按规定拼接成字符串
    vlan_str = ""
    # print(vlan)
    # print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(vlan, int):
        if space:
            vlan_str = " {vlan}".format(vlan =vlan)
        else:
            vlan_str = "{vlan}".format(vlan =vlan)
    else:
        if space:
            for value in vlan:
                vlan_str = vlan_str + " " + str(value)
        else:
            for value in vlan:
                vlan_str = vlan_str + str(value)
    return vlan_str


def Splicing_port(ports):  # 列表中的元素按规定拼接成字符串
    port_str = ""
    # print(vlan)
    # print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(ports, int):
        port_str = " {}".format(ports)
    else:
        for value in ports:
            port_str = port_str + " " + str(value)
    return port_str


def init_trunk(port, vlan, all_str):  # 交换机接交换机
    # 拼接vlan数据
    vlan_str = Splicing_vlan(vlan)
    # print(vlan_str)

    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_access(port, vlan, all_str):  # 交换机接电脑
    vlan_str = Splicing_vlan(vlan)
    # print(vlan_str)
    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type access\n" \
         " port default vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str


def init_hybrid(port, tag_vlan, untag_vlan, all_str):  # 混合接口
    tag_vlan_str = Splicing_vlan(tag_vlan)
    untag_vlan_str = Splicing_vlan(untag_vlan)
    # print(vlan_str)
    wr = "#\n" \
         " interface GigabitEthernet0/0/{port}\n" \
         " port link-type hybrid\n" \
         " port hybrid pvid vlan{untag_vlan}\n" \
         " port hybrid untagged vlan{untag_vlan}\n" \
         " port hybrid tagged vlan{tag_vlan}\n".format(port=port, tag_vlan=tag_vlan_str, untag_vlan=untag_vlan_str)
    all_str.append(wr)
    return all_str


def init_ETH_trunk_add(change_ports, trunk_port, all_str):
    for port in change_ports:
        wr = "#\n" \
             "interface GigabitEthernet0/0/{port}\n" \
             " eth-trunk {trunk_port}    \n" \
             " lacp priority 100    \n".format(port=port, trunk_port=trunk_port)
        all_str.append(wr)
    return all_str


def init_ETH_trunk(port, vlan, all_str, add_ports):  # 聚合接口
    vlan_str = Splicing_vlan(vlan)
    wr = "#\n" \
         " interface Eth-Trunk{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n" \
         " mode lacp \n" \
         " lacp preempt enable\n" \
         " max active-linknumber 4  \n" \
         " lacp preempt delay 10   \n".format(port=port, vlan=vlan_str)
    all_str.append(wr)  # 加入了定义
    all_str = init_ETH_trunk_add(add_ports, port, all_str)
    return all_str


def init_PPPOE(port,username,password,all_str):
    wr = "#\n" \
         "interface Dialer{port}\n" \
         "link-protocol ppp\n" \
         "ppp chap user {username}\n" \
         "ppp chap password cipher {password}\n" \
         "ppp pap local-user {username} password cipher {password}\n" \
         "ppp ipcp dns admit-any\n" \
         "ppp ipcp dns request\n" \
         "tcp adjust-mss 1200\n" \
         "ip address ppp-negotiate\n" \
         "dialer user arweb\n" \
         "dialer bundle {port}\n" \
         "dialer number {port} autodial\n" \
         "dialer-group {port}\n" \
         "nat outbound 2000\n".format(port=port,username = username, password=password)
    all_str.append(wr)
    return all_str
def init_interface_internet(port,ip,mask,all_str):
    wr ="#\n" \
        "interface GigabitEthernet0/0/{port}\n" \
        "ip address {ip} {mask} \n" \
        "nat outbound 2000 \n".format(port = port,ip = ip,mask = mask)
    all_str.append(wr)
    return all_str



def PPPOE_add(ports,all_str):
    wr = "#\n" \
         "dialer-rule\n"
    for port in ports:
        wr_str ="dialer-rule {port} ip permit\n".format(port = port)
        wr += wr_str
    wr = wr+"#\n" \
        "ip load-balance hash src-ip\n"
    for port in ports:
        wr_str ="ip route-static 0.0.0.0 0.0.0.0 Dialer{port}\n".format(port=port)
        wr += wr_str
    all_str.append(wr)
    return all_str

def gate_add(ip_gateways,all_str):
    wr = "#\n"
    for ip_gateway in ip_gateways:
        wr_str ="ip route-static 0.0.0.0 0.0.0.0 {port}\n".format( port =ip_gateway )
        wr += wr_str
    all_str.append(wr)
    return all_str
def init_vlanif(port,vlan,type,DNS,all_str):  # interface vlan dhcp:interface
    # 拼接vlan数据
    vlan_str = Splicing_vlan(vlan)
    wr = "#\n" \
         " interface vlanif {port}\n" \
         " ip address 192.168.{port}.1 255.255.255.0\n" \
         " dhcp select {type}\n" \
         " dhcp server dns-list {dns}\n".format(port=port,type=type,dns=DNS)
    all_str.append(wr)
    return all_str
def init_vlanif_global(port,type,all_str):  # interface vlan dhcp:global
    # 拼接vlan数据
    #vlan_str = Splicing_vlan(vlan)
    wr = "#\n" \
         " interface vlanif {port}\n" \
         " ip address 192.168.{port}.1 255.255.255.0\n" \
         " dhcp select {type}\n".format(port=port,type=type)
    all_str.append(wr)
    return all_str
def init_ip_pool(vlan,DNS,all_str):  # ip pool
    print(type(vlan))
    vlan_str = Splicing_vlan(vlan =vlan,space=False)   #你把这个启用了就行了(把默认的space在前关掉)
    print('====='*20)
    print(vlan_str)
    wr = "#\n" \
         " ip pool vlan_{vlan}\n" \
         " gateway-list 192.168.{vlan}.1\n" \
         " network 192.168.{vlan}.0 mask 255.255.255.0\n" \
         " dns-list {dns}\n".format(vlan=vlan_str, dns = DNS)
    all_str.append(wr)
    return all_str
# ==========================================================================================

# 如果值为nan那么设置为9999
def get_item(file, clomn):
    dict_datas = []
    for row_index in file.index.values:
        row_data = file.loc[row_index, clomn].to_dict()
        dict_datas.append(row_data)
    return dict_datas


# 如果值为nan那么设置为9999
def claear_nan(file, repalce_numb):
    for colmn in list(file):
        file[colmn].fillna(repalce_numb, inplace=True)


# ================
#
# 主函数
#
# ================
os.makedirs("output", exist_ok=True)  # 建立文件夹
path = r"output/4.txt"  # 建立txt

file = pd.read_excel("./sq/sw3.12.xlsx", sheet_name=0)  # 获取对应的表单
#file = pd.read_excel("sw3.12.xlsx", sheet_name=0)  # 获取对应的表单
# print(file)
claear_nan(file, 9999)  # 清除nan值变成9999

dictorys = get_item(file, list(file))  # 把excel变成字典列表

# 调整字典==
for dictory in dictorys:  # 取出字典列表中的每一个字典
    contain = []
    VLAN = str(dictory['VLAN'])
    VLAN = VLAN.split(" ")
    if VLAN is not None:  # 对字典的数据进行分离操作
        for t in VLAN:
            contain.append(int(t))
        dictory['VLAN'] = contain
        if dictory['类型'] == "HYBRID":
            dictory["tag_vlan"] = contain[0]
            dictory["untag_vlan"] = contain[1:]
        # print(dictory)
# ====
# 编写txt

PPPOE_port = []
ip_gateway = []
for data in dictorys:  # 遍历列表
    port = data["端口号"]
    if data["接口"] == "interface GigabitEthernet":
        if data['类型'] == "HYBRID":
            all_str = init_hybrid(port, data["tag_vlan"], data["untag_vlan"], all_str)
        if data['类型'] == "ACCESS":
            all_str = init_access(port, data["VLAN"], all_str)
        if data['类型'] == "TRUNK":
            all_str = init_trunk(port, data["VLAN"], all_str)
    if data['接口'] == 'interface Eth-Trunk':
        add_ports = data['TRUNK_PORT'].split(",")  # 关于,号分离
        # print(port)
        all_str = init_ETH_trunk(port, data["VLAN"], all_str, add_ports)

    if data["接口"] == "interface internet":
        ip_gateway.append(data['gateway'])#加入队列
        ip = data['IP']
        mask = data['mask']
        all_str = init_interface_internet(port,ip,mask,all_str)
        all_str = gate_add(ip_gateway, all_str)  # 专线固定IP默认路由加入
    if data["接口"] == "interface Dialer":
        username = data['用户名']
        password = data['密码']
        PPPOE_port.append(port)  #加入队列
        all_str = init_PPPOE(port,username,password,all_str)
        all_str = PPPOE_add(PPPOE_port, all_str)  # PPPOE默认路由加入
    if data["接口"] == "interface Vlanif":
        if data['类型'] == "interface":
            all_str = init_vlanif(port,data["VLAN"],data["类型"],data["DNS"],all_str)
        if data['类型'] == "global":
            all_str = init_vlanif_global(port, data["类型"], all_str)
            all_str = init_ip_pool(data["VLAN"],  data["DNS"], all_str)




s = "".join(all_str)  # 对其进行拼接
print(s)
with open(path, 'w', encoding='UTF-8') as txt:
    txt.write(s)






