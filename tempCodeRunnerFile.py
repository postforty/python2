i, v in enumerate(address_list):
#     # print(i)
#     # print(v)
#     # print(request_geo(v))
#     new_address = re.sub('\([^)]*|\)', '', v) # "("로 시작해서 ")"가 포함되지 않는 0개 이상의 모든 문자 또는 )를 ''으로 만듦
#     # print(new_address)
#     x, y = request_geo(new_address)
#     sheet.append([name_list[i], new_address, x, y]) # 시트 내용 추가

# # 추가된 시트 내용 보기 
# from pandas import DataFrame
# df = DataFrame(sheet.values)
# print(df)

# wb.save("학교주소좌