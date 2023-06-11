from collections import Counter
from wordcloud import WordCloud
import os
import pandas as pd


def make_cloud():
    # 상대경로로 수정함
    data_dir = ("../../data/morph_data_okt/spacing이전")
    file_list = os.listdir(data_dir)

    # 불용어 파일 가져오기
    with open("newnew_stopwords.txt", "r", encoding="utf-8") as f:
        stopwords_list = f.readlines()  # list

    stopwords = stopwords_list[0].split(",")

    for i in file_list:
        data = pd.read_csv(f"{data_dir}/{i}")
        musical_morphs = []
        print(i)

        #불용어 제거
        for j in data.iloc[:, 0]:
            if j not in stopwords and len(j) > 1: # 단어 크기가 2 이상인 것만
                musical_morphs.append(j)

        # 잘 들어갔나 확인
        print(musical_morphs)

        # 빈도수 카운트 후 가장 많이 나온 단어부터 100개
        counts = Counter(musical_morphs)
        tags = counts.most_common(300)

        wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white",
                       width=1000, height=1000, max_font_size=300)
        cloud = wc.generate_from_frequencies(dict(tags))

        # 상대경로로 수정
        cloud.to_file(f"../../visualization/word_cloud/spacing이전/{i[:-4]}.jpg")


make_cloud()
