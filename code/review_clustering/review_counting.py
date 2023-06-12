from collections import Counter
import os
import pandas as pd

def count_words(n) : # n은 몇 단어를 카운팅할지.
    # 상대경로로 수정함
    data_dir = ("../../data/review_adj_sub")
    file_list = os.listdir(data_dir)

    # 불용어 파일 가져오기
    with open("../review_visualization/newnew_stopwords.txt", "r", encoding="utf-8") as f:
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

        # # 잘 들어갔나 확인
        # print(musical_morphs)

        # 빈도수 카운트 후 가장 많이 나온 단어부터 20개
        counts = Counter(musical_morphs)
        tags = counts.most_common(n)
        df = pd.DataFrame(tags, columns=["word", "count"])

        df.to_csv(f'../../data/review_count/{i[:-4]}_count_{n}.csv', encoding='utf-8-sig', index=False)
