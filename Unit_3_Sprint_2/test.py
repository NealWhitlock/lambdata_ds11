import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.head())

for row in df:
    print(row)
    #print(row[0])

df['name'] = df['name'].str.replace("'", "''")

for i in range(5):
    survived = df.iloc[i][0]
    pclass = df.iloc[i][1]
    name = df.iloc[i][2]
    sex = df.iloc[i][3]
    age = df.iloc[i][4]
    sib_count = df.iloc[i][5]
    par_count = df.iloc[i][6]
    far = df.iloc[i][7]
    values = f"({survived}, {pclass}, '{name}', '{sex}', {age}, {sib_count}, {par_count}, {far})"
    print("INSERT INTO passengers VALUES " + values)
    # f"({survived}, {pclass}, {name}, {sex}, {age}, " +
    # f"{sib_count}, {par_count}, {far})")

    # print(len(name))
    # print(type(values))