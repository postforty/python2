# pip install folium
# pip install openpyxl

# https://kess.kedi.re.kr/index
# 자료실 > 주소록

import pandas as pd

path = '고등교육기관 하반기 주소록(2022).xlsx'
df_excel = pd.read_excel(path, engine='openpyxl')

df_excel.columns = df_excel.loc[0].tolist()

df_excel = df_excel.drop(index=list(range(0, 5)))

# print(df_excel)

print(df_excel.head()) # 데이터를 앞쪽 5줄만 표시

# print(df_excel['학교명'].values)

# print(df_excel['주소'].values)