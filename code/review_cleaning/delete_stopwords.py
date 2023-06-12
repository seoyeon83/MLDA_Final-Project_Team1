import os
import pandas as pd

# 불용어 삭제 함수
def deleteStopwords():
    data_dir = ("../../data/musical_morph_okt")
    file_list = os.listdir(data_dir)

    with open("../vis_code/newnew_stopwords.txt", "r", encoding="utf-8") as f:
        stopwords_list = f.readlines()  # list

    stopwords = stopwords_list[0].split(",")

    for i in file_list:
        data = pd.read_csv(f"{data_dir}/{i}")
        text = data.iloc[:, 0]  # 텍스트만 가져오기

        # 확인용
        # print(text)

        # 불용어 인덱스 수집
        drop_idx = [j for j in range(len(text)) if text[j] in stopwords or len(text[j]) < 2]

        # 확인용
        # print(drop_idx)

        # 불용어 삭제
        data.drop(drop_idx, axis=0, inplace=True)

        data.to_csv(f"../../data/morph_data_okt_cleaning/{i[:-4]}_cleaning.csv", encoding='utf-8-sig')

deleteStopwords()