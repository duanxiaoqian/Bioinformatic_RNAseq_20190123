#！/usr/bin/env python


import pandas as pd
import os

#read all gene 2class pathway file, and DEG file
def readfile(filepath):
    '''
    file is dataframe or like
    '''
    df = pd.read_csv(filepath, sep="\t")

    return df

#extract DEG corresponding pathway information , and make it to be a file
def extract_DEG_inf(df_pathway, df_DEG, filename):
    df_UPGene = df_pathway[df_pathway["Geneid"].isin(df_DEG["UP_Geneid"])]
    df_DownGene = df_pathway[df_pathway["Geneid"].isin(df_DEG["DOWN_Geneid"])]
    # print(df_UPGene.shape)
    fileNm_UP = filename + '_UPGene_pathway.txt'
    fileNm_DOWN = filename + '_DownGene_pathway.txt'
    df_UPGene.to_csv(os.path.join(os.getcwd(), fileNm_UP), sep='\t', index=None)
    df_DownGene.to_csv(os.path.join(os.getcwd(), fileNm_DOWN), sep='\t', index=None)
    # print(os.getcwd())

def main():
    # read all gene 2class pathway file, and DEG file
    pathway_file = 'E:\CR_genome\Geneid_KO_Pathwayko_Denifition.txt'
    DEG_file_CrvsCon = r'C:\Users\Administrator\Desktop\CR_RNAseq-20181127\Cr_Con\Cr_Con_geneKO.txt'
    DEG_file_SevsCon = r'C:\Users\Administrator\Desktop\CR_RNAseq-20181127\Se_Con\Se_Con_geneKO.txt'
    df_pathway = readfile(pathway_file)
    df_CrvsCon = readfile(DEG_file_CrvsCon)
    df_SevsCon = readfile(DEG_file_SevsCon)
    extract_DEG_inf(df_pathway, df_CrvsCon, 'Cr_Con')
    extract_DEG_inf(df_pathway, df_SevsCon, 'Se_Con')

if __name__ == '__main__':
    main()