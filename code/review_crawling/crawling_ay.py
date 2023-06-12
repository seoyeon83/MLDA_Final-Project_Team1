import InterparkCrawling as ic
import pandas as pd

info = pd.read_csv("C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/musical_info/musical_info_ay.csv",
                   encoding="utf-8-sig")

name = info["Musical"]
code = info["Code"]
th = info["Th"]


for i in range(len(name)):
    print(code[i], name[i], th[i])
    ic.IPCrawling(str(code[i]), str(name[i]), str(th[i]))

"""
IPCrawling에서 기대평으로 들어간다면?
elem = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[2]/div[2]/nav/div/div/ul/li[4]/a")
li[4]를 li[3]으로 수정할 것
"""
