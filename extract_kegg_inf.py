#！/usr/bin/env python
import pandas as pd
import re


##1.读取文件并提取信息
file_path = 'E:\CR_genome\ko_alldes_filter2lane.txt'
df = pd.read_csv(file_path, sep='\t')
df_Brite = df["Brite"]
df_KO = df["KO"]
df_Geneid = df["Geneid"]
ko_final = []
for (KO, Bri, Gen) in zip(df_KO, df_Brite, df_Geneid):
    # print(KO)
    # print(Bri)
    pattern = re.compile('  \d{5}.*?   ')
    #find all 2class KO and its description
    ko = re.findall(pattern, Bri)
    ko_filter = []
    len_ko = len(ko)
    if len_ko:
        for k in ko:
            ko_split = k.strip().split(' ')
            ko_num = ko_split[0]
            ko_des = ' '.join(ko_split[1:])
            # print(k)
            # print(ko_num)
            # print(ko_des)
            point = Gen + '\t' + KO + '\t' + ko_num + '\t' + ko_des
            # pattern_drop_str = re.compile('\xa0')
            # k_filter = re.sub(pattern_drop_str, '', k)
            ko_filter.append(point)


    else:
        pass


    for koset in ko_filter:
        ko_final.append(koset)

    # print(len(ko_filter))

# print(ko_final)
df_ko_final = pd.DataFrame(ko_final, columns=['1'])
print(df_ko_final)

#split df into we need
df_ko_final['Geneid'] = df_ko_final['1'].map(lambda x: x.split('\t')[0])
df_ko_final['KO'] = df_ko_final['1'].map(lambda x: x.split('\t')[1])
df_ko_final['Pathway_ko'] = df_ko_final['1'].map(lambda x: x.split('\t')[2])
df_ko_final['Definition'] = df_ko_final['1'].map(lambda x: x.split('\t')[3])
df_ko_final1 = df_ko_final.drop('1', axis=1)
print(df_ko_final1)

#write it into file
df_ko_final1.to_csv('Geneid_KO_Pathwayko_Denifition.txt')