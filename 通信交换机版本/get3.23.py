import pandas as pd
import numpy as np
import os

all_str = []  # 这个为编写的txt
# ==========================================================================================
def Splicing_vlan(vlan,space_first=True):  # 列表中的元素按规定拼接成字符串
    vlan_str = ""
    # print(vlan)
    # print(isinstance(vlan,int))   #判断是否为int类型-----学到了
    if isinstance(vlan, int):
        if space_first:
            vlan_str = " {vlan}".format(vlan =vlan)
        else:
            vlan_str = "{vlan}".format(vlan =vlan)
    else:
        if space_first:
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
    vlan_str = Splicing_vlan(vlan,space_first=True)
    # print(vlan_str)
    wr = "#\n" \
         "vlan batch {vlan}\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_access(port, vlan, all_str):  # 交换机接电脑
    vlan_str = Splicing_vlan(vlan,space_first=False)
    # print(vlan_str)
    wr = "#\n" \
         "vlan batch {vlan}\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         " port link-type access\n" \
         " port default vlan{vlan}\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_hybrid(port, tag_vlan, untag_vlan, vlan,all_str):  # 混合接口
    vlan_str = Splicing_vlan(vlan, space_first=True)
    tag_vlan_str = Splicing_vlan(tag_vlan)
    untag_vlan_str = Splicing_vlan(untag_vlan)
    # print(vlan_str)
    wr = "#\n" \
         "vlan batch {vlan}\n" \
         "interface GigabitEthernet0/0/{port}\n" \
         " port link-type hybrid\n" \
         " port hybrid pvid vlan{untag_vlan}\n" \
         " port hybrid untagged vlan{untag_vlan}\n" \
         " port hybrid tagged vlan{tag_vlan}\n".format(port=port, tag_vlan=tag_vlan_str, untag_vlan=untag_vlan_str,vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_ETH_trunk_add(change_ports, trunk_port, all_str): # 聚合接口
    for port in change_ports:
        wr = "#\n" \
             "interface GigabitEthernet0/0/{port}\n" \
             " eth-trunk {trunk_port}   \n" \
             " lacp priority 100   \n".format(port=port, trunk_port=trunk_port)
        all_str.append(wr)
    return all_str
def init_ETH_trunk(port, vlan, all_str, add_ports):  # 聚合接口端口配置
    vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "#\n" \
         "vlan batch {vlan}\n" \
         "interface Eth-Trunk{port}\n" \
         " port link-type trunk\n" \
         " port trunk allow-pass vlan{vlan}\n" \
         " mode lacp \n" \
         " lacp preempt enable\n" \
         " max active-linknumber 4  \n" \
         " lacp preempt delay 10   \n".format(port=port, vlan=vlan_str)
    all_str.append(wr)  # 加入了定义
    all_str = init_ETH_trunk_add(add_ports, port, all_str)
    return all_str
def init_PPPOE(port,username,password,all_str): #pppoe拨号
    wr = "# pppoe拨号线路{port}\n" \
         "acl name Intenet 2000\n" \
         " rule 5 permit \n" \
         "interface Dialer{port}\n" \
         " link-protocol ppp\n" \
         " ppp chap user {username}\n" \
         " ppp chap password cipher {password}\n" \
         " ppp pap local-user {username} password cipher {password}\n" \
         " ppp ipcp dns admit-any\n" \
         " ppp ipcp dns request\n" \
         " tcp adjust-mss 1200\n" \
         " ip address ppp-negotiate\n" \
         " dialer user arweb\n" \
         " dialer bundle {port}\n" \
         " dialer number {port} autodial\n" \
         " dialer-group {port}\n" \
         " nat outbound 2000\n"\
         "quit \n" \
         "ip load-balance hash src-ip\n"\
         "ip route-static 0.0.0.0 0.0.0.0 Dialer{port}\n"\
         "dialer-rule\n"\
         " dialer-rule {port} ip permit\n".format(port=port,username = username, password=password)
    all_str.append(wr)
    return all_str

def init_interface_internet(port,ip,mask,gateway,all_str):
    wr ="# 专线固定IP配置\n" \
        "acl name Intenet 2000\n" \
        " rule 5 permit \n" \
        "interface GigabitEthernet0/0/{port}\n" \
        " ip address {ip} {mask} \n" \
        " nat outbound 2000 \n" \
        "quit\n" \
        "ip route-static 0.0.0.0 0.0.0.0 {gateway}\n".format(port = port,ip = ip,gateway=gateway,mask = mask)
    all_str.append(wr)
    return all_str
def init_vlanif(port,vlan,type,DNS,all_str):  # interface vlan dhcp:interface
    # 拼接vlan数据
    vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "# vlanif三层\n" \
         "vlan batch {vlan}\n" \
         "interface vlanif {port}\n" \
         " ip address 192.168.{port}.1 255.255.255.0\n" \
         " dhcp select {type}\n" \
         " dhcp server dns-list {dns}\n".format(port=port,type=type,dns=DNS,vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_vlanif_global(port,type,all_str):  # interface vlan dhcp:global
    # 拼接vlan数据
    # vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "#\n" \
         "vlan batch {vlan}\n" \
         "interface vlanif {port}\n" \
         " ip address 192.168.{port}.1 255.255.255.0\n" \
         " dhcp select {type}\n".format(port=port,type=type)
    all_str.append(wr)
    return all_str
def init_ip_pool(vlan,DNS,all_str):  # ip pool
    vlan_str = Splicing_vlan(vlan,space_first =False)
    wr = "# vlan{port} DHCP分配IP地址池\n" \
         "vlan batch {vlan}\n" \
         "ip pool vlan_{port}\n" \
         " gateway-list 192.168.{port}.1\n" \
         " network 192.168.{port}.0 mask 255.255.255.0\n" \
         " dns-list {dns}\n".format(port=vlan_str, dns = DNS,vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_VPN(vlan,port,all_str):  # VPN
    vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "# VPN 配置\n" \
         "vlan batch {vlan}\n" \
         "l2tp enable\n" \
         "l2tp-group {port} \n" \
         " undo tunnel authentication \n" \
         " allow l2tp virtual-template {port} \n" \
         "#\n" \
         "interface Virtual-Template {port} \n" \
         " ppp authentication-mode chap \n" \
         " remote address pool L2TP \n" \
         " ip address 192.168.{vlan}.1 255.255.255.0\n".format(port=port, vlan=vlan_str)
    all_str.append(wr)
    return all_str
def init_AAA(username,password,level,stype,all_str):  # Local_user
    wr = "#\n" \
         "aaa\n" \
         " local-user {username} password cipher {password}\n" \
         " local-user {username} privilege level {level} \n" \
         " local-user {username} service-type {stype} \n" \
         "user-interface vty 0 4 \n" \
         " authentication-mode aaa \n" \
         " user privilege level 3  \n" \
         " idle-timeout 30 0  \n" \
         " protocol inbound all \n" .format(username=username, password=password, level=level,
                                                               stype=stype)
    all_str.append(wr)
    return all_str
def init_CLOCK(ip,all_str):  # Local_user
    wr = "#\n" \
         "quit\n" \
         "clock timezone bj add 08:00:00\n" \
         "sys \n" \
         "ntp-service unicast-server {ip} \n" .format(ip=ip)
    all_str.append(wr)
    return all_str
def init_RATE_UP(speed,vlan,all_str):  # RATE_UP
    vlan_str = Splicing_vlan(vlan, space_first=False)
    #CIR：承诺信息速率 bits，CBS：承诺突发尺寸bit，PIR：峰值信息速率byte，PBS：峰值突发尺寸byte,
    #本方案为双速双桶:限制带宽以PIR为准（限最高速）：CBS=PIR/20,CBS=PIR*1.5,PBS=PIR*2
    wr = "#\n" \
         "interface vlanif {vlan}\n" \
         " qos car inbound source-ip-address range 192.168.{vlan}.2 to 192.168.{vlan}.254 per-address cir {cir} pir {pir} cbs {cbs} pbs {pbs} green pass yellow pass red discard \n" .format(vlan=vlan_str,cir=int(speed*1024/20),pir=speed*1024,cbs=int(speed*1024*1024*1.5/8),pbs=int(speed*1024*1024*2.5/8))
    all_str.append(wr)
    return all_str
def init_RATE_DOWN(speed,vlan,all_str):  # RATE_DOWN
    vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "#\n" \
         "interface vlanif {vlan}\n" \
         " qos car inbound source-ip-address range 192.168.{vlan}.2 to 192.168.{vlan}.254 per-address cir {cir} pir {pir} cbs {cbs} pbs {pbs} green pass yellow pass red discard \n" .format(vlan=vlan_str,cir=int(speed*1024/20),pir=speed*1024,cbs=int(speed*1024*1024*1.5/8),pbs=int(speed*1024*1024*2.5/8))
    all_str.append(wr)
    return all_str
def init_DDNS_ORAY(port,user,password,interface,stype,all_str):  # DDNS
    wr = "#\n" \
         "dns resolve\n" \
         "dns server 114.114.114.114\n" \
         "ddns policy ORAY{port}\n" \
         " interval 90\n" \
         " url oray://{user}:{password}@phddnsdev.oray.net\n" \
         " interface {interface}\n" \
         " ddns apply policy ORAY{port} fqdn {ddns}\n" .format(port=port,user=user,password=password,interface=interface,ddns=stype)
    all_str.append(wr)
    return all_str
def init_WLAN(port,user,password,stype,vlan,all_str):  # WLAN AC
    vlan_str = Splicing_vlan(vlan, space_first=False)
    wr = "# AC FIA AP无线配置\n" \
         "capwap source interface vlanif{port}\n" \
         "wlan ac\n" \
         "security-profile name wlanpassword{port}\n" \
         " security wpa2 psk pass-phrase {password} aes\n" \
         "y\n" \
         "ssid-profile name ssid{port}2G\n" \
         " ssid {user}_2.4G\n" \
         "y\n" \
         "ssid-profile name ssid{port}5G\n" \
         " ssid {user}_5G\n" \
         "y\n" \
         "vap-profile name wlan{port}2G\n" \
         " service-vlan vlan-id {vlan}\n" \
         " ssid-profile {user}2G\n" \
         "vap-profile name wlan{port}5G\n" \
         " service-vlan vlan-id {vlan}\n" \
         "wired-port-profile name GE0\n" \
         " mode root\n" \
         " vlan tagged {vlan}\n" \
         "wired-port-profile name GE1\n" \
         " mode endpoint \n" \
         " vlan pvid {vlan}\n" \
         " vlan untagged {vlan}\n" \
         "regulatory-domain-profile name {stype}\n" \
         "ap-group name {stype}\n" \
         " regulatory-domain-profile {stype}\n" \
         "y\n" \
         " vap-profile wlan{port}2G wlan 1 radio 0\n" \
         " vap-profile wlan{port}5G wlan 1 radio 1\n" \
         " radio 1\n" \
         " channel 80mhz 161\n" \
         "y\n" \
         "Q\n" \
         "ap-id 0 \n" \
         " ap-group {stype} \n" \
         " wired-port-profile GE0 gigabitethernet 0 \n" \
         " wired-port-profile GE1 gigabitethernet 1 \n" \
         "y\n" .format(port=port,user=user,password=password,vlan=vlan_str,stype=stype)
    all_str.append(wr)
    return all_str
def init_ACL_INT(port,vlan):  # ACL控制列表 2000已在上网处做，3001内网列表，
    #vlan_str = Splicing_vlan(vlan, space_first=True)
    i = 5
    wr = "#\n" \
         "acl name SDLAN 3001 \n" \
         " rule 5 permit ip source 192.168.0.0 0.0.255.255 destination 192.168.0.0 0.0.255.255  \n" \
         "acl name Class_int_{port} {port} \n".format(port=port)
    for V in vlan:
         wr_str = " rule {i} permit source 192.168.{vlan}.0 0.0.0.255 \n".format(i=i,vlan=V )
         i = i+1
         wr += wr_str
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
path = r"output/5.txt"  # 建立txt

file = pd.read_excel(r"sq/sw3.23.xlsx", sheet_name=0)  # 获取对应的表单
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
    port = int(data["端口号"])
    if data["接口"] == "interface GigabitEthernet":
        if data['类型'] == "HYBRID":
            all_str = init_hybrid(port, data["tag_vlan"], data["untag_vlan"], data["VLAN"], all_str)
        if data['类型'] == "ACCESS":
            all_str = init_access(port, data["VLAN"], all_str)
        if data['类型'] == "TRUNK":
            all_str = init_trunk(port, data["VLAN"], all_str)
    if data['接口'] == 'interface Eth-Trunk':
        add_ports = data['TRUNK_PORT'].split(",")  # 关于,号分离
        all_str = init_ETH_trunk(port, data["VLAN"], all_str, add_ports)

    if data["接口"] == "interface internet":  # 专线固定IP
        #ip_gateway.append(data['gateway'])#加入队列
        gateway = data['gateway']
        ip = data['IP']
        mask = data['mask']
        all_str = init_interface_internet(port,ip,mask,gateway,all_str)
    if data["接口"] == "interface Dialer":
        username = data['用户名']
        password = data['密码']
        PPPOE_port.append(port)  #加入队列
        all_str = init_PPPOE(port,username,password,all_str)

    if data["接口"] == "interface Vlanif":  #三层VLANif接口配置
        if data['类型'] == "interface":
            all_str = init_vlanif(port,data["VLAN"],data["类型"],data["DNS"],all_str)
        if data['类型'] == "global":
            all_str = init_vlanif_global(port, data["类型"], all_str)
            all_str = init_ip_pool(data["VLAN"], data["DNS"], all_str)
    if data["接口"] == "VPN": #VPN配置
        if data['类型'] == "L2TP":
            all_str = init_ip_pool(data["VLAN"], data["DNS"], all_str)
            all_str = init_VPN(data["VLAN"],port, all_str)
            all_str = init_AAA(data["用户名"], data["密码"], int(data["level"]), data["stype"], all_str)
    if data["接口"] == "AAA": #本地用户配置
       all_str = init_AAA(data["用户名"], data["密码"],int(data["level"]),data["stype"], all_str)
    if data["接口"] == "POOL": #IP地址池配置
       all_str = init_ip_pool(data["VLAN"], data["DNS"], all_str)
    if data["接口"] == "CLOCK": #IP地址池配置
       all_str = init_CLOCK(data["IP"], all_str)
    if data["接口"] == "RATE": #根据IP段智能限速
        if data["类型"] == "UP": #上行
            all_str = init_RATE_UP(int(data["level"]), data["VLAN"],all_str)
        if data["类型"] == "DOWN": #下行
            all_str = init_RATE_DOWN(int(data["level"]), data["VLAN"],all_str)
    if data["接口"] == "DDNS":  # 域名解析
        if data["类型"] == "ORAY":  # 花生壳域名解析
            all_str = init_DDNS_ORAY(port, data["用户名"], data["密码"], data["TRUNK_PORT"], data["stype"], all_str)

    if data["接口"] == "WLAN":  # AC FIA AP无线配置
        all_str = init_WLAN(port, data["用户名"], data["密码"],data["stype"], data["VLAN"], all_str)
    if data["接口"] == "ACL":  # AC FIA AP无线配置
        if data["类型"] == "TRAFFIC":
            all_str = init_ACL_INT(port, data["VLAN"])


s = "".join(all_str)  # 对其进行拼接
print(s)
with open(path, 'w', encoding='UTF-8') as txt:
    txt.write(s)






