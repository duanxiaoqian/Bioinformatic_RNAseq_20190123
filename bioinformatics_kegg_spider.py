#！/usr/bin/env python



import json
# import os
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
import pandas as pd
import time





def get_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        return None
    except ConnectionError:
        print('error occured')
        return None


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    pattern = re.compile('>.*?<')
    th40 = soup.find_all('th', attrs={'class': 'th40'})
    th41 = soup.find_all('th', attrs={'class': 'th41'})
    th = th40 + th41
    # print(len(th))
    Key_th = []
    for i, TH in enumerate(th):
        key = TH.nobr.string
        Key_th.append(key)

    td40 = soup.find_all('td', attrs={'class': 'td40'})
    td41 = soup.find_all('td', attrs={'class': 'td41'})
    td = td40 + td41

    #Definition
    Definition = {}
    if 'Definition' in Key_th:
        Def = td[Key_th.index('Definition')]
        Def_filter = re.findall(pattern, str(Def))[2]
        Definition['Definition'] = Def_filter
    else:
        Definition["Definition"] = "No this KO"

    #Brite
    Brite = {}
    if 'Brite' in Key_th:
        Bri = td[Key_th.index('Brite')]
        Bri_filter = Bri.nobr
        Brite["Brite"] = Bri_filter
    else:
        Brite["Brite"] = ""
    return Definition, Brite




def extract_ko_all(ko, Definition, Brite):
    ko_des = {}
    inf  = 'Definition:' + str(Definition["Definition"]) + ' Brite:' + str(Brite["Brite"])
    ko_des[ko] = inf
    # print(ko_des)
    # print(type(ko_des))
    with open('E:\CR_genome\ko_alldes.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(ko_des, ensure_ascii=False) + '\n')




def main():
    df_gene_ko = pd.read_csv('E:\CR_genome\only_cre_ko.txt', sep='\t')
    KO = df_gene_ko["KO"]
    # print(KO)
    KO_Def = []
    for ko in KO:
        url = 'https://www.kegg.jp/dbget-bin/www_bget?ko:' + ko
        html = get_page(url)
        # print(html)
        Definition, Brite = parse_page_detail(html)
        # print(Definition, Brite)
        extract_ko_all(ko, Definition, Brite)
        KO_Def.append(Definition["Definition"])
        time.sleep(2)
    df_gene_ko["Definition"] = KO_Def
    df_gene_ko.to_csv('E:\CR_genome\cre_ko_name.txt', sep="\t", index=False)


if __name__ == '__main__':
    main()
