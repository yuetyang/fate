#随机分数据

import pandas as pd
from sklearn.utils import shuffle

def data(url):
    file=pd.read_csv(url)
    column_name = {'rlabel': 'y', 'data[0]': 0, 'data[1]': 1, 'data[2]': 2, 'data[3]': 3,
                   'data[4]': 4, 'data[5]': 5, 'data[6]': 6, 'data[7]': 7}
    file.rename(columns=column_name, inplace=True)
    file.drop('Flag', axis=1, inplace=True)

    return file


def save_data(split_data):
    for i, split in enumerate(split_data):
        csv_filename = f'split_{i + 1}.csv'
        split.to_csv(csv_filename, index=False)
        print(f"分割 {i + 1} 已保存为 {csv_filename}")

if __name__=='__main__':
    url_1="E:\黑客松\\nDos_dataset.csv"
    url_2="E:\黑客松\\nFuzzy_dataset.csv"
    url_3="E:\黑客松\\ngear_dataset.csv"
    url_4="E:\黑客松\\nRPM_dataset.csv"
    file_1=data(url_1)
    file_2=data(url_2)
    file_3=data(url_3)
    file_4=data(url_4)
    all_file = pd.concat([file_1, file_2, file_3, file_4], axis=0, ignore_index=True)
    shuffle_file = shuffle(all_file).reset_index(drop=True)




