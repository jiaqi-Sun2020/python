import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("./不同人群的读书需求.xlsx")
clomn = list(df)
#print(list(df))  #输出列名

age = list(df[clomn[2]].drop_duplicates())
age[1],age[3] = age[3],age[1]   #跟换数据
print(age)

data = df[clomn[3]].value_counts()
print(data)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体，否则中文会显示异常

dict_datas = []  #打包成字典
for row_index in df.index.values:
    row_data = df.loc[row_index, [clomn[2], clomn[3]]].to_dict()
    dict_datas.append(row_data)

# age_0_male =[]  #年龄
# age_1_male =[]
# age_2_male=[]
# age_3_male=[]
#
# age_0_female =[]  #年龄
# age_1_female =[]
# age_2_female=[]
# age_3_female=[]

age_0 =[]  #年龄
age_1 =[]
age_2=[]
age_3=[]

male = []
female = []
m_1=m_2=m_3=m_4=f_1=f_2=f_3=f_4 =0
for dict_data in dict_datas:
    if dict_data[clomn[2]] ==age[0]:  #查找年龄
        if dict_data[clomn[3]] == "男":
            m_1= m_1+1
        if dict_data[clomn[3]] == "女":
            f_1= f_1+1
    if dict_data[clomn[2]] ==age[1]:  #查找年龄
        if dict_data[clomn[3]] == "男":
            m_2 = m_2 + 1
        if dict_data[clomn[3]] == "女":
            f_2 = f_2 + 1
    if dict_data[clomn[2]] ==age[2]:  #查找年龄
        if dict_data[clomn[3]] == "男":
            m_3 = m_3 + 1
        if dict_data[clomn[3]] == "女":
            f_3 = f_3 + 1
    if dict_data[clomn[2]] ==age[3]:  #查找年龄
        if dict_data[clomn[3]] == "男":
            m_4 = m_4 + 1
        if dict_data[clomn[3]] == "女":
            f_4 = f_4 + 1

male.append(m_1)
male.append(m_2)
male.append(m_3)
male.append(m_4)

female.append(f_1)
female.append(f_2)
female.append(f_3)
female.append(f_4)


print(male)

# N = 2
# year = df.columns.values.tolist()[4:-2:N]
# data = df.iloc[-2].values.tolist()[4:-2:N]
# female = np.abs(np.asarray(data) - 45) + 10
# male = np.abs(100 - np.asarray(data) - 45) + 10


fig = plt.figure(figsize=(12, 8))
size = len(age)
print(size)

x = np.arange(size)
print(x)
bar_width = 0.4

plt.title("男女人数")
plt.ylim(0, 20)
plt.ylabel("人\n数", rotation=0)
plt.yticks([0, 100], ["$0$", "$100$"])
plt.xticks(x, age, rotation=45)
plt.xlabel("年份")
plt.bar(x, female,  width=bar_width, label='女性')  #female是根据xage来的
plt.bar(x + bar_width, male, width=bar_width, label='男性')

plt.legend()
plt.show()
