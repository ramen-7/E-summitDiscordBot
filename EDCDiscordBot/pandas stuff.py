import pandas as pd

df = pd.read_csv('teams.csv')
r = len(df)
c = len(df.columns)
role = []
userid = []
x = 4
for i in range(r):
    for j in range(1, c):
        userid.append(df.iloc[i, j])

for a in range(r):
    role.append(df.iloc[a, 0])

for i in range(r):
    role = df.iloc[i, 0]
    for j in range(1, c):
        name = df.iloc[i, j]
        if type(name) == float:
            continue
        else:
            print(role, name, type(name))




print(role)
print(userid)