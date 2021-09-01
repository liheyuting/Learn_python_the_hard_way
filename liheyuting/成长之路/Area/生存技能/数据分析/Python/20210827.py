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

# l1[i] = pd.to_numeric(l1[i])
# l2 = pd.to_numeric(l2)
# l = np.asarray([l1,l2], dtype= float)

#l1 = np.asarray(l1, dtype= float)
#l2 = np.asarray(l2, dtype= float)

data = {
        "a的值": l1,
        "objective的值": l2
    }
df = pd.DataFrame(data, dtype = float)
df.to_excel('value.xlsx', index=False)


# def deal():
#     data = {
#         "a的值": l1,
#         "objective的值": l2
#     }
#     df = pd.DataFrame(data, dtype = float)
#     df.to_excel('value.xlsx', index=False)

    # df = pd.DataFrame(l1, columns=['a的值'], dtype=float)
    # df = pd.DataFrame(l2, columns=['objective的值'], dtype=float)

# if __name__ == '__main__':
#     deal()

#print(l)

# a = lines.strip().split(',') #去掉空白和逗号
# a = np.array(a)

f.close()
