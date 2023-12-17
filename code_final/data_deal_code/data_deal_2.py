import pandas as pd
from sklearn.model_selection import train_test_split

# 读取四个攻击文件和正常工作文件
df_dos = pd.read_csv('./DATA_SA/new_data/nDos_dataset.csv')
df_fuzzy = pd.read_csv('./DATA_SA/new_data/nFuzzy_dataset.csv')
df_gear = pd.read_csv('./DATA_SA/new_data/ngear_dataset.csv')
df_rpm = pd.read_csv('./DATA_SA/new_data/nRPM_dataset.csv')


# 将四个攻击文件合并为一个数据集
df_attack = pd.concat([df_dos, df_fuzzy, df_gear, df_rpm], ignore_index=True)

# 计算每种攻击类型的数量
n_dos = len(df_dos)
n_fuzzy = len(df_fuzzy)
n_gear = len(df_gear)
n_rpm = len(df_rpm)

# 划分测试集，每种攻击类型数量基本相同
test_size = 0.2
test_dos_size = int(test_size * n_dos)
test_fuzzy_size = int(test_size * n_fuzzy)
test_gear_size = int(test_size * n_gear)
test_rpm_size = int(test_size * n_rpm)
#test_normal_size = int(test_size * len(df_normal))

df_test_dos = df_dos.sample(n=test_dos_size, random_state=42)
df_test_fuzzy = df_fuzzy.sample(n=test_fuzzy_size, random_state=42)
df_test_gear = df_gear.sample(n=test_gear_size, random_state=42)
df_test_rpm = df_rpm.sample(n=test_rpm_size, random_state=42)
#df_test_normal = df_normal.sample(n=test_normal_size, random_state=42)

df_test_dos.loc[df_test_dos['Flag']=='T','label'] = 1
df_test_dos.loc[df_test_dos['Flag']=='R','label'] = 0
df_test_fuzzy.loc[df_test_fuzzy['Flag']=='T','label'] = 2
df_test_fuzzy.loc[df_test_fuzzy['Flag']=='R','label'] = 0
df_test_gear.loc[df_test_gear['Flag']=='T','label'] = 3
df_test_gear.loc[df_test_gear['Flag']=='R','label'] = 0
df_test_rpm.loc[df_test_rpm['Flag']=='T','label'] = 4
df_test_rpm.loc[df_test_rpm['Flag']=='R','label'] = 0


df_test = pd.concat([df_test_dos, df_test_fuzzy, df_test_gear, df_test_rpm], ignore_index=True)
#df_test.insert(1, 'rlabel', df_test['label'])
#df_test= df_test.drop('label', axis=1)
df_test= df_test.drop('Flag', axis=1)
df_test.to_csv('./DATA_SA/f_d/test_dataset.csv', index=False)

# 划分训练集，每种攻击类型数量基本相同
train_size = 0.8
train_dos_size = int(train_size * n_dos)
train_fuzzy_size = int(train_size * n_fuzzy)
train_gear_size = int(train_size * n_gear)
train_rpm_size = int(train_size * n_rpm)
#train_normal_size = int(train_size * len(df_normal))

df_train_dos, df_train_dos_b = train_test_split(df_dos, train_size=train_dos_size, random_state=42)
df_train_fuzzy, df_train_fuzzy_b = train_test_split(df_fuzzy, train_size=train_fuzzy_size, random_state=42)
df_train_gear, df_train_gear_b = train_test_split(df_gear, train_size=train_gear_size, random_state=42)
df_train_rpm, df_train_rpm_b = train_test_split(df_rpm, train_size=train_rpm_size, random_state=42)
#df_tr ain_normal, df_train_normal_b = train_test_split(df_normal, train_size=train_normal_size, random_state=42)


#df.loc[df['previous_column']=='T', 'label'] = 1
#df.loc[df['previous_column']=='R', 'label'] = 0
df_train_dos.loc[df_train_dos['Flag']=='T','label'] = 1
df_train_dos.loc[df_train_dos['Flag']=='R','label'] = 0
df_train_fuzzy.loc[df_train_fuzzy['Flag']=='T','label'] = 2
df_train_fuzzy.loc[df_train_fuzzy['Flag']=='R','label'] = 0
df_train_gear.loc[df_train_gear['Flag']=='T','label'] = 3
df_train_gear.loc[df_train_gear['Flag']=='R','label'] = 0
df_train_rpm.loc[df_train_rpm['Flag']=='T','label'] = 4
df_train_rpm.loc[df_train_rpm['Flag']=='R','label'] = 0
df_train_dos_b.loc[df_train_dos_b['Flag']=='T','label'] = 1
df_train_dos_b.loc[df_train_dos_b['Flag']=='R','label'] = 0
df_train_fuzzy_b.loc[df_train_fuzzy_b['Flag']=='T','label'] = 2
df_train_fuzzy_b.loc[df_train_fuzzy_b['Flag']=='R','label'] = 0
df_train_gear_b.loc[df_train_gear_b['Flag']=='T','label'] = 3
df_train_gear_b.loc[df_train_gear_b['Flag']=='R','label'] = 0
df_train_rpm_b.loc[df_train_rpm_b['Flag']=='T','label'] = 4
df_train_rpm_b.loc[df_train_rpm_b['Flag']=='R','label'] = 0


# 合并两份训练数据集为一个训练数据集
df_train_a = pd.concat([df_train_dos, df_train_fuzzy, df_train_gear, df_train_rpm], ignore_index=True)
df_train_b = pd.concat([df_train_dos_b, df_train_fuzzy_b, df_train_gear_b, df_train_rpm_b], ignore_index=True)
#df_train_a.insert(1, 'rlabel', df_train_a['label'])
#df_train_a= df_train_a.drop('label', axis=1)
df_train_a= df_train_a.drop('Flag', axis=1)
#df_train_b.insert(1, 'rlabel', df_train_b['label'])
#df_train_b= df_train_b.drop('label', axis=1)
df_train_b= df_train_b.drop('Flag', axis=1)
df_train_a.to_csv('./DATA_SA/f_d/train_dataset_a.csv', index=False)
df_train_b.to_csv('./DATA_SA/f_d/train_dataset_b.csv', index=False)

