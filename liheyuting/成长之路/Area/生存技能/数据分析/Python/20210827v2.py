import numpy as np
import pandas as pd

f = open(r'C:\Users\lih152\Desktop\1.txt')
l1 = []
l2 = []
i = 0

for m in f.readlines():
    m = m.strip().split()  # 去掉空白和逗号
    if "a" in m:
        l1.append(m[2:3])
        i = i + 1

    if "objective:" in m:
        l2.append(m[1:2])
        i = i + 1

print(l1)

data = {
        "a的值": l1,
        "objective的值": l2
    }
df = pd.DataFrame(data, dtype = float)
df.to_excel('value.xlsx', index=False)

f.close()