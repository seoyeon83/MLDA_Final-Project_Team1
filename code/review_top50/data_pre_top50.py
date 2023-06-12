import pandas as pd
import os

# 데이터 목록 리스트로 불러오기
data_list = os.listdir("./MLDA_Final-Project_Team1/data/musical_top10_since2019")

# 데이터 쌓아줄 빈 df
all_data = pd.DataFrame()

# 빈 df에 데이터 차곡차곡 합쳐줌
for tit in data_list:
    data = pd.read_csv("./MLDA_Final-Project_Team1/data/musical_top10_since2019/%s"%tit)
    all_data = pd.concat([all_data, data], axis=0)

# 카운트값 가져오고 라이선스인지 창작인지 넣어주기 위해 빈 컬럼 생성
counts_data = all_data["SRCHWRD_NM"].value_counts().to_frame()
counts_data = counts_data.assign(GENRE_NM="")

# 장르를 가져오기 위해 기존의 데이터에서 필요한 컬럼만 추출하여 가져오고 인덱스를 뮤지컬명으로 설정
all_data_pre = all_data.iloc[:, 2:6]
all_data_pre.drop_duplicates(["SRCHWRD_NM"], inplace=True, ignore_index=False)
all_data_pre = all_data_pre.set_index("SRCHWRD_NM")

# 뮤지컬명들이 담긴 리스트
musical = all_data["SRCHWRD_NM"].unique()

# 뮤지컬 명을 하나하나 모두 꺼내어 해당 값의 장르 데이터를 추가해줌
for i in musical:
    counts_data.loc[i, "GENRE_NM"] = all_data_pre.loc[i, "GENRE_NM"]

# 확인용
# print(counts_data)

# 인덱스를 기본 숫자로 재설정 및 컬럼 명 수정, 탑 60을 뽑아 csv로 저장 (60을 뽑은 이유는 아동이나 기타 장르가 포함되어있을 수 있기에)
counts_data = counts_data.reset_index().rename(columns={"index": "SRCHWRD_NMA", "count": "Count"})
top50 = counts_data.iloc[:60, :]
top50.to_csv("top50_since2019.csv", index=True, sep=",", encoding="utf-8-sig")
