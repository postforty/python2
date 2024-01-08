# pip install folium
# pip install openpyxl

# https://kess.kedi.re.kr/index
# 자료실 > 주소록

import pandas as pd

path = '고등교육기관 하반기 주소록(2022).xlsx'
df_excel = pd.read_excel(path, engine='openpyxl')
# 5번째 학교명 가져오기
df_excel.columns = df_excel.loc[4].tolist()
# 엑셀 데이터의 0~5 row 삭제
df_excel = df_excel.drop(index=list(range(0, 5)))

print(df_excel.head()) # 데이터를 앞쪽 5줄만 표시

# print(df_excel['학교명'].values)

# print(df_excel['주소'].values)