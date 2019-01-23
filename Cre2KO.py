#！/usr/bin/env python

import pandas as pd


#read cre_ko file
df_cre_ko = pd.read_csv('E:\CR_genome\only_cre_ko.txt', sep='\t')
df_ko_den = pd.read_csv('E:\CR_genome\KO_Pathwayko_Denifition.txt', sep=',')
# print(df_ko_den.shape)

#form responsing file
cre_ko = {}
len_df_cre_ko = len(df_cre_ko)
for i in range(len_df_cre_ko-1):
    cre_ko[df_cre_ko.loc[i, 'KO']] = df_cre_ko.loc[i, 'Geneid']


#make every KO have a Cre
df_ko_den['Geneid'] = df_cre_ko['KO'].map(cre_ko)
# print(df_ko_den.shape)

df_ko_den.to_csv('E:\CR_genome\KO_Pathwayko_Denifition_Geneid.txt', sep='\t')

