import os
import pandas as pd

file_path  = ("../../data/review_morph_okt")

file_list = os.listdir(file_path)

for i in file_list[2:]:
    src = os.path.join(file_path, i)
    print(f'i : {i}')
    if "_spacing" in i :
        dst = ''.join(i.split('_spacing'))

    elif "musical_review_raw_data" not in i :
        if "adj" in i :
            dst = f'{i[:3]}_reviews{i[3:]}'
        elif "noun" in i :
            dst = f'{i[:4]}_reviews{i[4:]}'

    print(f'dst {dst}')
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)


    # data = pd.read_csv(f"{data_dir}/{i}")
