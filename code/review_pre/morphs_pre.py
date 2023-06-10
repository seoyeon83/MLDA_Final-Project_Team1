from konlpy.tag import Kkma
from konlpy.tag import Okt
import os
import pandas as pd

import konlpy

konlpy.jvm.init_jvm(jvmpath=None, max_heap_size=2048)

def pos_kk():
    kk = Kkma()

    # 전처리 완료된 데이터 경로로 수정해주기!!
    input_dir = '../MLDA_Final-Project_Team1/data/review_cleaning'
    # 저장 경로, 맞춰서 경로 수정해주기!! 근데 이걸로 통일하자
    output_dir = '../MLDA_Final-Project_Team1/data/morph_data_kkm'

    # 확인할 디렉토리 내의 파일 리스트 가져오기
    file_list = os.listdir(input_dir)

    for file_name in file_list:
        # 잘 돌아가는지 확인용 출력
        print(file_name)

        if file_name.endswith('.csv'):
            # 입력 파일 경로
            input_file = os.path.join(input_dir, file_name)

            # 출력 파일 경로
            output_file = os.path.join(output_dir, file_name)

            # CSV 파일 읽기
            df = pd.read_csv(input_file)
            review = df['text']

            noun_list = []
            adjective_list = []

            for text in review:
                pos_tags = kk.pos(str(text))
                nouns = []
                adjectives = []

                for word, pos in pos_tags:
                    if pos.startswith('NN'):  # Noun
                        nouns.append(word)
                    elif pos.startswith('VA'):  # Adjective
                        adjectives.append(word)

                noun_list.append(nouns)
                adjective_list.append(adjectives)

            n_df = pd.DataFrame({'Nouns': noun_list})
            a_df = pd.DataFrame({'Adjectives': adjective_list})

            n_df.to_csv(output_dir + f"/noun_{file_name}", index=False, encoding="utf-8-sig")
            a_df.to_csv(output_dir + f"/adj_{file_name}", index=False, encoding="utf-8-sig")


def pos_okt():
    okt = Okt()  # Instantiate the Okt class

    # 전처리 완료된 데이터 경로로 수정해주기!!
    input_dir = 'C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/review_cleaning'
    # 저장 경로, 맞춰서 경로 수정해주기!! 근데 이걸로 통일하자
    output_dir = 'C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/morph_data_okt'

    # 확인할 디렉토리 내의 파일 리스트 가져오기
    file_list = os.listdir(input_dir)

    for file_name in file_list:
        # 잘 돌아가는지 확인용 출력
        print(file_name)

        if file_name.endswith('.csv'):
            # 입력 파일 경로
            input_file = os.path.join(input_dir, file_name)

            # 출력 파일 경로
            output_file = os.path.join(output_dir, file_name)

            # CSV 파일 읽기,
            df = pd.read_csv(input_file)
            review = df['text']

            noun_list = []
            adjective_list = []

            for text in review:
                pos_tags = okt.pos(str(text))


                for word, pos in pos_tags:
                    if pos.startswith('Noun'):  # Noun
                        noun_list.append(word)
                    elif pos.startswith('Adjective'):  # Adjective
                        adjective_list.append(word)


            n_df = pd.DataFrame({'Nouns': noun_list})
            a_df = pd.DataFrame({'Adjectives': adjective_list})

            n_df.to_csv(output_dir+f"/noun_{file_name}", index=False, encoding="utf-8-sig")
            a_df.to_csv(output_dir+f"/adj_{file_name}", index=False, encoding="utf-8-sig")

# #태그세트 보기
# kkma = Kkma()
# okt = Okt()
# print(kkma.tagset, "\n", okt.tagset)

pos_okt()
# pos_kk()