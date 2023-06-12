from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import os

def GetVector(df) :
    corpus = df["text"]

    # 벡터화
    vect = CountVectorizer(max_features=None)
    document_term_matrix = vect.fit_transform(corpus)
    tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names())

    return tf


def joinWords(n) : # n은 몇 단어를 카운팅 후 벡터화 했는지. 파일명에 들어가는 거라 빼도 상관 X
    data_dir = ("../../data/review_count")
    file_list = os.listdir(data_dir)

    # 형용사, 명사 별 리뷰 내용, 작품 제목 저장
    adj_all_text = []
    adj_all_tit = []
    noun_all_text = []
    noun_all_tit = []

    for i in file_list:
        print(i) # 확인용
        data = pd.read_csv(f"{data_dir}/{i}")

        if "adj_sub" in i :
            adj_all_tit.append(i.split("_")[2])
            adj_all_text.append(" ".join(data["word"]))

        elif "noun" in i :
            noun_all_tit.append(i.split("_")[2])
            noun_all_text.append(" ".join(data["word"]))

    adj = pd.DataFrame({"title" : adj_all_tit, "text" : adj_all_text})
    noun = pd.DataFrame({"title": noun_all_tit, "text": noun_all_text})

    # adj.iloc[:, [0]].to_csv("../../data/review_vector/reviews_vector_title.csv", encoding="utf-8-sig", index=False)
    GetVector(adj).to_csv(f"../../data/review_vector/adj_reviews_vector_{n}.csv", encoding="utf-8-sig", index=False)
    GetVector(noun).to_csv(f"../../data/review_vector/noun_reviews_vector_{n}.csv", encoding="utf-8-sig", index=False)

