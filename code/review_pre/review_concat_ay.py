import pandas as pd


def concat_review(review_list, musical_name):
    # 빈 데이터프레임 생성
    cc_review = pd.DataFrame()

    # 데이터 가져와서 합치기
    for i in review_list:
        print(i)
        re1 = pd.read_csv(f"../MLDA_Final-Project_Team1/data/reviews/{i}.csv")
        cc_review = pd.concat([cc_review, re1], axis=0, join='outer', ignore_index=True)


    # 조회수, 공감수 컬럼 삭제, 이상한 컬럼 삭제
    # cc_review.drop(columns=["views", "like"], axis=1, inplace=True)
    cc_review.drop(columns=["Unnamed: 0"], axis=1, inplace=True)
    cc_review = cc_review.reset_index().rename(columns={"":"Index", "id":"Rating", "date":"Id", "rating":"Date", "title":"Title", "text":"Text"})

    # csv 파일로 저장
    cc_review.to_csv(f"../MLDA_Final-Project_Team1/data/tot_review/review_{musical_name}.csv", index=False, sep=",", encoding="utf-8-sig")
    # 확인용 return
    return print(cc_review.value_counts().sum())

# 흠.. 이걸 노가다로 이렇게 안할 수 있는 방법이 있을까?
# 마땅이 무언가 떠오르지 않아 노가다로 해둠...

grease = ["review_그리스_26", "review_그리스_27", "review_그리스_28"]
broad = ["review_브로드웨이42번가_18", "review_브로드웨이42번가_17",
         "review_브로드웨이42번가_16", "review_브로드웨이42번가_15"]
billie = ["review_빌리엘리어트_3"]
head = ["review_헤드윅_13", "review_헤드윅_12"]
hope = ["review_호프_4", "review_호프_3", "review_호프_2"]
mamma = ["review_맘마미아_9", "review_맘마미아_8", "review_맘마미아_7"]
rent = ["review_렌트_8", "review_렌트_7"]
gentle = ["review_젠틀맨스가이드_1", "review_젠틀맨스가이드_2", "review_젠틀맨스가이드_3"]
some = ["review_썸씽로튼_1", "review_썸씽로튼_2"]
ben = ["review_벤허_1", "review_벤허_2"]
pan = ["review_팬레터_4", "review_팬레터_3"]
mari = ["review_마리퀴리_1", "review_마리퀴리_2"]
red = ["review_레드북_1", "review_레드북_2", "review_레드북_3"]
king = ["review_킹아더_2"]
let = ["review_렛미플라이_1"]

pre = [grease, broad, billie, head, hope, mamma, rent,
       gentle, some, ben, pan, mari, red, king, let]

musical = ["그리스", "브로드웨이42번가", "빌리엘리어트", "헤드윅", "호프", "맘마미아", "렌트",
           "젠틀맨스가이드", "썸씽로튼", "벤허", "팬레터", "마리퀴리", "레드북", "킹아더", "렛미플라이"]

# 하나씩 꺼내서 함수 돌리기
for i in range(len(musical)):
    concat_review(pre[i], musical[i])
