from collections import Counter
from wordcloud import WordCloud
import os
import pandas as pd

def make_cloud():
    input_dir = 'C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/morph_data_okt'
    file_list = os.listdir(input_dir)
    musical_morphs = []

    for file_name in file_list:
        print(file_name)

        if file_name.endswith('.csv'):
            input_file = os.path.join(input_dir, file_name)

            data = pd.read_csv(input_file)

            for i in data.iloc[:, 0]:
                musical_morphs.append(i)

            #전처리 잘 되었는지 확인용
            print(musical_morphs)

            # 빈도수 카운트 후 가장 많이 나온 단어부터 100개
            counts = Counter(musical_morphs)
            tags = counts.most_common(300)

            wc = WordCloud(font_path="C:/Windows/Fonts/malgun.ttf", background_color="white",
                           width=1000, height=1000, max_font_size=300)
            cloud = wc.generate_from_frequencies(dict(tags))

            cloud.to_file(f"{file_name[:-4]}.jpg")

make_cloud()