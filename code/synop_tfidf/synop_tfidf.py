import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def synop_tfidf(data):
    synop = data["시놉시스"]
    title = data["제목"]

    tfidf = TfidfVectorizer().fit(synop)
    print(tfidf.vocabulary_)
    tfidf_arr = tfidf.transform(synop).toarray()

    tfidf_result = pd.DataFrame(tfidf_arr, columns=tfidf.vocabulary_)

    tfidf_result.to_csv("../../data/synopsis_tfidf_data/synop_tfidf.csv", encoding="utf-8-sig")

data = pd.read_excel("../../data/musical_tot_info/musical_synop.xlsx")
print(data)

synop_tfidf(data)