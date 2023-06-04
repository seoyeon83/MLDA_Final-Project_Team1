import InterparkCrawling as ic
import pandas as pd

info = pd.read_csv("C:/Users/1ayou/PycharmProjects/MLDA_Final-Project_Team1/data/musical_info/musical_info_ay.csv",
                   encoding="utf-8-sig")

name = info["Musical"]
code = info["Code"]
th = info["Th"]

for i in range(len(name)):
    print(code[i], name[i], th[i])
    ic.IPCrawling(str(code[i]), str(name[i]), th[i])