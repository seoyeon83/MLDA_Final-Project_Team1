from collections import Counter
from wordcloud import WordCloud
import os
import pandas as pd


def make_cloud():
    data_dir = ("C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/morph_data_okt")
    file_list = os.listdir(data_dir)

    with open("new_stopwords.txt", "r", encoding="utf-8") as f:
        stopwords = f.readlines()  # list

    for i in file_list:
        data = pd.read_csv(f"{data_dir}/{i}")
        musical_morphs = []
        print(i)

        for j in data.iloc[:, 0]:
            if j not in stopwords:
                musical_morphs.append(j)

        # 잘 들어갔나 확인
        # print(musical_morphs)

        # 빈도수 카운트 후 가장 많이 나온 단어부터 100개
        counts = Counter(musical_morphs)
        tags = counts.most_common(300)

        wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white",
                       width=1000, height=1000, max_font_size=300)
        cloud = wc.generate_from_frequencies(dict(tags))

        cloud.to_file(f"C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/visualization/word_cloud/{i[:-4]}.jpg")


make_cloud()
