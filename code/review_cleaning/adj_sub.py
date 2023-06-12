import os
import pandas as pd

'''
슬픈 : 슬프고, 슬퍼요
아쉬운 : 아쉬워요, 아쉽네요, 아쉽지만, 아쉬웠어요, 아쉬웠습니다
행복한 : 행복했습니다, 행복하게, 행복했던, 행복했어요, 행복했으면
따듯한 : 따듯하고, 따듯해지는, 따뜻한, 따뜻하고, 따뜻해지는
재미있는 : 재미있어요,재미있네요,재미있습니다,재미있고,재미있게,재미있었어요,재밌어요,재밌었습니다,재밌네요,재밌어요,재밌습니다,재밌,재미,재밌어,재밌게,재밌고,재밌었어요,재밌는
화려한 : 화려하고,화려하게,화려하여,화려해
좋았던 : 좋 들어간 것. 좋았지만은 냅두기
예쁜 : 예뻐요, 예쁘고, 예뻐서
즐거운 : 즐 들어간 것
아름다운 : 아름 들어간 것
'''

# 형용사 일반화
def adj_sub():
    data_dir = ("../../data/morph_data_okt_cleaning")
    file_list = os.listdir(data_dir)

    for i in file_list:
        if "adj" not in i : continue
        data = pd.read_csv(f"{data_dir}/{i}", index_col=0)
        text = data.iloc[:, 0]  # 텍스트만 가져오기
        new_text = []
        print(i, i[:-13])
        # 일반화
        for t in text :
            # 슬픈
            if t in ["슬프고", "슬퍼요"] :
                new_text.append("슬픈")
            # 아쉬운
            elif t in ["아쉬워요", "아쉽네요", "아쉽지만", "아쉬웠어요", "아쉬웠습니다"] :
                new_text.append("아쉬운")
            # 행복한
            elif t in ["행복했습니다", "행복하게", "행복했던", "행복했어요", "행복했으면"] :
                new_text.append("행복한")
            # 따듯한
            elif t in ["따듯하고", "따듯해지는", "따뜻한", "따뜻하고", "따뜻해지는"] :
                new_text.append("따듯한")
            # 재미있는
            elif t in ["재미있어요","재미있네요","재미있습니다","재미있고","재미있게","재미있었어요","재밌어요","재밌었습니다",
                       "재밌네요","재밌어요","재밌습니다","재밌","재미","재밌어","재밌게","재밌고","재밌었어요","재밌는"] :
                new_text.append("재미있는")
            # 화려한
            elif t in ["화려하고","화려하게","화려하여","화려해"] :
                new_text.append("화려한")
            # 좋았던
            elif '좋' in t and t != "좋았지만" and t != "좋았던" :
                new_text.append("좋았던")
            # 예쁜
            elif t in ["예뻐요", "예쁘고", "예뻐서"] :
                new_text.append("예쁜")
            # 즐거운
            elif '즐' in t and t != "즐거운" :
                new_text.append("즐거운")
            # 아름다운
            elif '아름' in t and t != "아름다운" :
                new_text.append("아름다운")
            # 일반화에 해당 안되는 경우
            else :
                new_text.append(t)

        data.iloc[:,0] = new_text

        data.to_csv(f"../../data/review_adj_sub/{i[:-13]}_adj_sub.csv", encoding='utf-8-sig', index=False)

adj_sub()