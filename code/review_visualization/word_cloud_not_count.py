from collections import Counter
from wordcloud import WordCloud
import os
import pandas as pd

# 카운팅을 따로 안하고 카운트해둔 데이터로 워드클라우드 찍기
def make_cloud_not_count():
    # 상대경로로 수정함
    data_dir = ("../../data/review_count")
    file_list = os.listdir(data_dir)


    for i in file_list:
        data = pd.read_csv(f"{data_dir}/{i}", index_col=0)
        print(i)
        # word : count 형태의 딕셔너리가 되도록.
        musical_morphs = data.set_index("word").T.to_dict("list")
        musical_morphs = { k:v[0] for k, v in musical_morphs.items() }


        # 잘 들어갔나 확인
        # print(musical_morphs)

        # # 빈도수 카운트 후 가장 많이 나온 단어부터 100개
        # counts = Counter(musical_morphs)
        # tags = counts.most_common(100)

        #
        wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white",
                       width=800, height=800, max_font_size=300)
        cloud = wc.generate_from_frequencies(musical_morphs)
        #
        # # 상대경로로 수정
        cloud.to_file(f"../../visualization/word_cloud_count/{i[:-4]}.jpg")


make_cloud_not_count()
