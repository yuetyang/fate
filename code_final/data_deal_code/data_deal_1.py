import pandas as pd

# 读取CSV文件
df = pd.read_csv('./DATA_SA/new_data/nDos_dataset.csv')
df = pd.read_csv('./DATA_SA/new_data/nFuzzy_dataset.csv')
df = pd.read_csv('./DATA_SA/new_data/ngear_dataset.csv')
df = pd.read_csv('./DATA_SA/new_data/nRPM_dataset.csv')
# 检查DLC列是否为8

# 将TimeSTAMPS列中的每个值减1478389
df['Timestamp'] = df['Timestamp']-1478191030

# 删除CAN ID列
df.drop('CAN ID', axis=1, inplace=True)

# 将rlabel列名改为y
df.rename(columns={'y': 'rlabel'}, inplace=True)
df.insert(0, 'id', range(1, len(df) + 1))
df.drop('id', axis=1, inplace=True)


#ID
df.insert(0, 'id', range(1, len(df) + 1))

# 将修改后的数据保存回CSV文件
df.to_csv('./DATA_SA/new_data/nDos_dataset.csv', index=False)
#df.to_csv('./DATA_SA/new_data/nFuzzy_dataset.csv', index=False)
#df.to_csv('./DATA_SA/new_data/ngear_dataset.csv', index=False)
#df.to_csv('./DATA_SA/new_data/nRPM_dataset.csv', index=False)
