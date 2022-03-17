import pandas as pd
import openpyxl
import numpy as np

#用了一下几个sheet: 汇总表(0),未结(1),委外(7),委外未交数(10)

global path

path = "1.xls"

#获取sheet名
df_name= pd.read_excel(path, sheet_name=None)
#print(df.keys()) #这个输出的话那就是字典的键值了
print(list(df_name))


#=====================================委外sheet操作
df_7 = pd.read_excel(io=path, sheet_name=7)    #df_7为委外编号
columns_name7 = df_7.columns  #获取所有列名
#工单信息
Work_orders = columns_name7[-1] #获取最后一列的名称名    工单
Work_orders_data = df_7[Work_orders]  #获取最后一列的数据

#已收未验量
Qrbis= columns_name7[-4] #获取的名称名   已收未验量
Qrbis_data = df_7[Qrbis]  #获取数据

df_7_index=df_7.set_index(Work_orders)#设置工单号为索引
#print(df_7_index.loc[Work_orders_data[4],Qrbis])#获取到这个工单号对应的已收未验量
#print(sum(df_7_index.loc[Work_orders_data[4],Qrbis])) #一个工单可能对应多个验收量所以相加

#编写字典
Dicts = []        #字典列表
clear_list = []   #独热列表
df_7_index=df_7.set_index(Work_orders)#设置工单号为索引
for i,Work_order_data in enumerate(Work_orders_data):
    if Work_order_data not in clear_list: #查看是否在独热列表中
        clear_list.append(Work_order_data)
        #写入字典
        Qrbi_data = np.sum(df_7_index.loc[Work_order_data, Qrbis])    #为啥df_7_index查找生成的是一个numpy int64的数   这边必须求和！！！多个表单求和
        Dict = {"Work_order_data":Work_order_data,"Qrbi_data":Qrbi_data,"Unquantity":None}
        Dicts.append(Dict)
        #print(Dict)
#print(Dicts)
#print(Dicts)  #输出的是独立唯一的工单对应值


#====================================委外未交数sheet
df_10 = pd.read_excel(io=path, sheet_name=10)    #df_10为委外编号
columns_name10 = df_10.columns  #获取所有列名
#获取工单号
Work_orders = columns_name10[6] #获取最后一列的名称名    工单
#Work_orders_data = df_10[Work_orders]  #获取第一列的数据
print(Work_orders)

#未交量
Unquantity = columns_name10[5] #获取5列的名称名    未交量
Unquantity_data = df_10[Unquantity]  #获取5列的数据

df_10_index=df_10.set_index(Work_orders)#设置工单号为索引
#对于每一个工单来做的
for i,Dict in enumerate(Dicts):
    Work_order_data =Dict["Work_order_data"]   #工号
    Unquantity_data = np.sum(df_10_index.loc[Work_order_data, Unquantity]) #对表单10进行查询(工单号，)              #一定要相加
    Dict["Unquantity"] = Unquantity_data
    print(Dict)



#准备建立excel
Work_order_data_list =[]
Qrbi_data_list = []
Unquantity_list = []
for Dict in Dicts:
    Work_order_data_list.append(Dict["Work_order_data"])
    Qrbi_data_list.append(Dict["Qrbi_data"])
    Unquantity_list.append(Dict["Unquantity"])

#多表合并
df_1 = pd.read_excel(io=path, sheet_name=1)   #未结表
columns_name1 = df_1.columns  #获取所有列名
Work_orders = columns_name1[1]

#设置新的
df_data = pd.DataFrame({"{}".format(Work_orders):Work_order_data_list,"已收未验量":Qrbi_data_list,"未交量":Unquantity_list})  #新的表单
#两表单合并  =============非常关键的一步
result = pd.merge(df_1 ,df_data,on=[Work_orders],how='outer')#on为以什么为判定      how为链接方式默认取交集   outer取并集

#保存xlsx
writer = pd.ExcelWriter('ss.xlsx')
result.to_excel(writer, index=False, sheet_name="sheet1")
writer.save()