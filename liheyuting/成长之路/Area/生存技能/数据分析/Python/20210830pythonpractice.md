title: Python练习：提取txt某2个的值，存到excel
date: 2021-08-31 15:36
categories:
- 生存技能
tags:
- Python
---

**题目：** 从文本文档中提取a和objective对应的值，并存到另一份excel中
文本文档：1.txt（如末尾所示）

```
import numpy as np  
import pandas as pd  
# 使用到pandas
  
# 取出a和objective的值 
f = open(r'C:\Users\lih152\Desktop\1.txt')   # 打开txt文件并命名为f
l1 = []  
l2 = []  # 建立两个空list表格
i = 0  
  
for m in f.readlines():  
    m = m.strip().split()  # 行分列  
 if "a" in m:   # 此处要先看到a和m的情况，用条件语句筛选对应的行
        l1.append(m[2])  # list的append功能，其他dic等没有append模块
        i = i + 1  
  
 if "objective:" in m:  
        l2.append(m[1])  
        i = i + 1  
  
data = {  
        "a的值": l1,  
 "objective的值": l2  
    }  # 将两列值统一成dic
df = pd.DataFrame(data, dtype = float)  # 使用pandas的DataFrame规整数据和数值
df.to_excel('value.xlsx', index=False)  # 存为excel文档
  
f.close() # 关掉文本文档


```

**文本文档数据：**

a =  0.002
solution for: docplex_model1
objective: 0.101055
x_0=0.663
x_1=0.080
x_2=0.133
x_3=0.036
x_4=0.077

a =  0.004
solution for: docplex_model1
objective: 0.15211
x_0=0.327
x_1=0.160
x_2=0.267
x_3=0.073
x_4=0.154

a =  0.006
solution for: docplex_model1
objective: 0.201908
x_1=0.240
x_2=0.400
x_3=0.109
x_4=0.221

a =  0.008
solution for: docplex_model1
objective: 0.211243
x_1=0.320
x_2=0.533
x_3=0.127

a =  0.01
solution for: docplex_model1
objective: 0.21902
x_1=0.400
x_2=0.584

a =  0.012
solution for: docplex_model1
objective: 0.225569
x_1=0.480
x_2=0.505

a =  0.014
solution for: docplex_model1
objective: 0.232118
x_1=0.560
x_2=0.426

a =  0.016
solution for: docplex_model1
objective: 0.238667
x_1=0.640
x_2=0.347

a =  0.018000000000000002
solution for: docplex_model1
objective: 0.245216
x_1=0.720
x_2=0.267

a =  0.020000000000000004
solution for: docplex_model1
objective: 0.251765
x_1=0.800
x_2=0.188

a =  0.022000000000000006
solution for: docplex_model1
objective: 0.258314
x_1=0.880
x_2=0.109

a =  0.024000000000000007
solution for: docplex_model1
objective: 0.264863
x_1=0.960
x_2=0.030

a =  0.02600000000000001
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.02800000000000001
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.030000000000000013
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.032000000000000015
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.034000000000000016
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.03600000000000002
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.03800000000000002
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.04000000000000002
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.04200000000000002
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.044000000000000025
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.04600000000000003
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.04800000000000003
solution for: docplex_model1
objective: 0.267327
x_1=0.990

a =  0.05000000000000003
solution for: docplex_model1
objective: 0.267327
x_1=0.990

