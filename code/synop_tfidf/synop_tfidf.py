import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Okt

def synop_tfidf(data):
    synop = data["시놉시스"]
    title = data["제목"]

    for i in range(len(synop)):
        synop[i] = re.sub(r'[a-zA-Z]*', '', str(synop[i]))
        synop[i] = re.sub(r'[ㄱ-ㅎㅏ-ㅣ]*', '', str(synop[i]))
        synop[i] = re.sub(r'[*/!?~^,.#:\\\(\)\'\"]*', '', str(synop[i]))
        synop[i] = re.sub(r'[\n\r]*', '', str(synop[i]))
        synop[i] = re.sub(r'[♡♥]*', '', str(synop[i]))

    tfidf = TfidfVectorizer(ngram_range=(2,2)).fit(synop)
    tfidf_arr = tfidf.fit_transform(synop).toarray()
    tfidf_vocab = tfidf.vocabulary_

    voc_index = tfidf_vocab.values()
    voc_data = tfidf_vocab.keys()

    tfidf_vocab_s = pd.DataFrame(data=voc_data, index=voc_index, columns=["text"]).sort_index()
    print(tfidf_vocab_s)

    tfidf_result = pd.DataFrame(tfidf_arr, index=title, columns=tfidf_vocab_s["text"])

    tfidf_result.to_csv("../../data/synopsis_tfidf_data/synop_tfidf.csv", encoding="utf-8-sig")


data = pd.read_excel("../../data/musical_tot_info/musical_synop.xlsx")
print(data)

synop_tfidf(data)