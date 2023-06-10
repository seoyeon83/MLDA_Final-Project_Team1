import re
import os
import pandas as pd
from pykospacing import Spacing

data_list = os.listdir("C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/tot_review")

def remove_else(review_data):
    sp = Spacing()
    data = pd.read_csv(f"C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/tot_review/{review_data}")
    # 중복 제거하기
    data.drop_duplicates(subset=["Id", "Date", "Title", "Text"], inplace=True)

    # 이상한 애들 제거 - 알파벳, 초성, 특수문자, \가 포함된 탭, 엔터 등 기호
    for i in range(len(data["Text"])):
        data.iloc[i, 8] = re.sub(r'[a-zA-Z]*', '', str(data.iloc[i, 8]))
        data.iloc[i, 8] = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]*', '', str(data.iloc[i, 8]))
        data.iloc[i, 8] = re.sub(r'[*/!?~^,.#:\\\(\)\'\"]*', '', str(data.iloc[i, 8]))
        data.iloc[i, 8] = re.sub(r'[\n\r]*', '', str(data.iloc[i, 8]))
        data.iloc[i, 8] = re.sub(r'[♡♥]*', '', str(data.iloc[i, 8]))
    # 스페이싱 다시 해주기
        data.iloc[i, 8] = sp(str(data.iloc[i, 8]))

    data.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
    data.to_csv(f"C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/tot_review/{review_data}", index=True, sep=",", encoding="utf-8-sig")
    return print(data)



for i in data_list:
    print(i)
    remove_else(i)
