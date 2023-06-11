from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import os

#TF-IDF로 키워드별 중요도 구하기
def GetTFIDF(df) :
    corpus = df["text"]

    # 벡터화
    vect = CountVectorizer(max_features = 100)
    document_term_matrix = vect.fit_transform(corpus)

    # tf-idf 구하는 과정
    tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names())
    D = len(tf)
    df = tf.astype(bool).sum(axis=0)
    idf = np.log((D+1) / (df+1)) + 1

    tfidf = tf * idf
    tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)

    return tfidf

# 상대경로로 수정함
def joinWords() :
    data_dir = ("../../data/musical_morph_okt")
    file_list = os.listdir(data_dir)

    # 형용사, 명사 별 리뷰 내용, 작품 제목 저장
    adj_all_text = []
    adj_all_tit = []
    noun_all_text = []
    noun_all_tit = []

    for i in file_list:
        print(i) # 확인용
        data = pd.read_csv(f"{data_dir}/{i}")

        if "adj" in i :
            adj_all_tit.append(i.split("_")[2][:-4])
            adj_all_text.append(" ".join(data["Adjectives"]))

        elif "noun" in i :
            noun_all_tit.append(i.split("_")[2][:-4])
            noun_all_text.append(" ".join(data["Nouns"]))

    adj = pd.DataFrame({"title" : adj_all_tit, "text" : adj_all_text})
    noun = pd.DataFrame({"title": noun_all_tit, "text": noun_all_text})

    adj.iloc[:, [0]].to_csv("../../data/musical_review_tfidf/reviews_title.csv", encoding="utf-8-sig")
    GetTFIDF(adj).to_csv("../../data/musical_review_tfidf/adj_reviews_tf-idf.csv", encoding="utf-8-sig")
    GetTFIDF(noun).to_csv("../../data/musical_review_tfidf/noun_reviews_tf-idf.csv", encoding="utf-8-sig")

# 제목과 tf-idf 결과는 손으로 합쳐줌
joinWords()