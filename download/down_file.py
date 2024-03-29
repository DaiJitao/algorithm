# encoding=utf-8

import numpy as np
import os
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re


def mk_name(min_, max_):
    names = []
    for i in range(min_, max_ + 1):
        p = str(i)
        if len(p) == 2:
            p = "0" + p
        elif len(p) == 1:
            p = "00" + p

        print(p)
        names.append(p)

    return names


interval = [100, 8.3, 9.2, 10, 13, 15, 20, 150, 140, 123, 5, 15, 3.3, 118, 1.6, 119, 57, 16, 6, 7, 1, 5, 54.5, 33.8,
            21.8,
            6.6, 8, 7, 10, 11, 12.3, 47, 5.5, 54, 11.5]


def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)


# def url_html_parser(html):
#     files = {}
#     soup = BeautifulSoup(html, 'lxml')
#     tables = soup.find_all('table', attrs={'bordercolor': "#CCCCCC", 'cellspacing': 0, 'border': "1"})
#     for tb in tables:
#         for tb in tables:
#             inner_trs = tb.find_all("tr")[1:]
#             for tr in inner_trs:
#                 tds = tr.find_all('td')
#                 if len(tds) == 3:
#                     name = tds[0].get_text().strip()
#                     num = tds[2].get_text().strip()
#                     url = tds[1].find('a')['href']
#                     key = '{}_{}卷'.format(name, num)
#                     if key in files:
#                         key += '_2'
#                     else:
#                         files[key] = url_cleaner(url)
#     return files


def url_cleaner(url):
    return re.sub('\r\n', '', url)


def load_to_pdf(base_dir, file_name, url):
    """
    下载pdf文件
    :param base_dir:
    :param file_name:
    :return:
    """
    failed_file = base_dir + '/load_failed.txt'
    try:
        pdf_file = base_dir + '/' + file_name + '.pdf'

        if os.path.exists(pdf_file):
            fsize = os.path.getsize(pdf_file)
            if fsize > 0:
                print('{} 已经存在'.format(pdf_file))
                return

        response = requests.get(url, stream=True, timeout=300)
        if response.status_code == 200:
            print("loaded ok, starting to save:")
            with open(pdf_file, mode='wb') as fp:
                fp.write(response.content)
            print("saved pdf in {}".format(pdf_file))
            res = np.random.choice(interval, size=1)
            print("sleep {}".format(res[0]))
            time.sleep(res[0])
        else:
            print(f"error:{response.status_code}")
            raise Exception(response.status_code)
    except Exception as e:
        with open(failed_file, mode='a', encoding='utf-8') as fp:
            fp.write('url: {}, name:{}\n'.format(url, file_name))

        print('saved in {}'.find(failed_file))


def __get_data():
    """下载论集部"""
    bdir = r'D:/myData/大正藏典籍分类/論集部'
    mkdir(bdir)

    files = {'因明正理門論本1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1628.pdf',
             '因明正理門論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1629.pdf',
             '因明入正理論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1630.pdf',
             '迴諍論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1631.pdf',
             '方便心論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1632.pdf',
             '如實論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1633.pdf',
             '入大乘論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1634.pdf',
             '大乘寶要義論10': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1635.pdf',
             '大乘集菩薩學論25': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1636.pdf',
             '集大乘相論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1637.pdf',
             '集諸法寶最上義論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1638.pdf',
             '提婆菩薩破楞伽經中外道小乘四宗論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1639.pdf',
             '提婆菩薩釋楞伽經中外道小乘涅槃論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1640.pdf',
             '隨相論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1641.pdf',
             '金剛針論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1642.pdf',
             '尼乾子問無我義經1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1643.pdf',
             '佛說立世阿毘曇論10': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1644.pdf',
             '彰所知論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1645.pdf',
             '成實論16': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1646.pdf',
             '四諦論4': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1647.pdf',
             '解脫道論12': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1648.pdf',
             '三彌底部論3': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1649.pdf',
             '辟支佛因緣論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1650.pdf',
             '十二因緣論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1651.pdf',
             '緣生論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1652.pdf',
             '大乘緣生論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1653.pdf',
             '因緣心論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1654.pdf',
             '止觀門論頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1655.pdf',
             '寶行王正論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1656.pdf',
             '手杖論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1657.pdf',
             '諸教決定名義論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1658.pdf',
             '發菩提心經論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1659.pdf',
             '菩提資糧論6': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1660.pdf',
             '菩提心離相論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1661.pdf',
             '菩提行經4': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1662.pdf',
             '菩提心觀釋1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1663.pdf',
             '廣釋菩提心論4': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1664.pdf',
             '金剛頂瑜伽中發阿耨多羅三藐三菩提心論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1665.pdf',
             '大乘起信論1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1666.pdf',
             '大乘起信論2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1667.pdf',
             '釋摩訶衍論10': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1668.pdf',
             '大宗地玄文本論20': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1669.pdf',
             '那先比丘經2': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1670A.pdf',
             '那先比丘經3': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1670B.pdf',
             '福蓋正行所集經12': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1671.pdf',
             '龍樹菩薩為禪陀迦王說法要偈1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1672.pdf',
             '勸發諸王要偈1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1673.pdf',
             '龍樹菩薩勸誡王頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1674.pdf',
             '讚法界頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1675.pdf',
             '廣大發願頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1676.pdf',
             '三身梵讚1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1677.pdf',
             '佛三身讚1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1678.pdf',
             '佛一百八名讚1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1679.pdf',
             '一百五十讚佛頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1680.pdf',
             '佛吉祥德讚3': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1681.pdf',
             '七佛讚唄伽他1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1682.pdf',
             '揵稚梵讚1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1683.pdf',
             '八大靈塔梵讚1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1684.pdf',
             '佛說八大靈塔名號經1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1685.pdf',
             '賢聖集伽陀一百頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1686.pdf',
             '事師法五十頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1687.pdf',
             '密跡力士大權神王經偈頌1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1688.pdf',
             '請賓頭盧法1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1689.pdf',
             '賓頭盧突羅闍為優陀延王說法經1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1690.pdf',
             '迦葉仙人說醫女人經1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1691.pdf',
             '勝軍化世百瑜伽他經1': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1692.pdf'}
    for name, url in files.items():
        load_to_pdf(bdir, name, url)
    print(len(files))


def get_urls():
    """论集部 主页地址下载，找到urls"""
    url = "https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra16.jsp"
    inf = r'D:\myData\大正藏典籍分类\論集部\index.html'
    data = {'論集部': url}
    files = {}
    index_html_file = r"D:\myData\大正藏典籍分类\論集部\index.html"
    response = requests.get(url, stream=True, timeout=300)
    if response.status_code == 200:
        html = response.text
        with open(inf, mode='w', encoding='utf-8') as fp:
            fp.write(html)

        files = url_html_parser(html)
        print(files)
    else:
        print(f"error:{response.status_code}")


class LUBU():
    """律部"""

    def __init__(self, url, name, files=None):
        if url is None:
            raise Exception()

        if files is not None:
            self.files = files
        else:
            self.__init_files(name, url)

        if self.files == None or len(self.files) == 0:
            raise Exception()

        print('files={}'.format(self.files))

    def __init_files(self, name, url):
        """下载文件地址"""
        inf = r'D:/myData/大正藏典籍分类/{}/index.html'.format(name)
        response = requests.get(url, stream=True, timeout=300)
        if response.status_code == 200:
            html = response.text
            with open(inf, mode='w', encoding='utf-8') as fp:
                fp.write(html)

            self.files = self.url_html_parser(html)
        else:
            print(f"error:{response.status_code}")

    def load(self, bdir):

        for name, url in self.files.items():
            self.load_to_pdf(bdir, name, url)
        print('{} 下载完成'.format(bdir))

    def url_html_parser(self, html):
        files = {}
        soup = BeautifulSoup(html, 'lxml')
        tables = soup.find_all('table', attrs={'bordercolor': "#CCCCCC", 'cellspacing': 0, 'border': "1"})
        for tb in tables:
            inner_trs = tb.find_all("tr")[1:]
            for tr in inner_trs:
                tds = tr.find_all('td')
                if len(tds) == 3:
                    name = tds[0].get_text().strip()
                    num = tds[2].get_text().strip()
                    url = tds[1].find('a')['href']
                    key = '{}_{}卷'.format(name, num)
                    if key in files:
                        key += '_2'
                    else:
                        files[key] = url_cleaner(url)
        return files

    def load_to_pdf(self, base_dir, file_name, url):
        """
        下载pdf文件
        :param base_dir:
        :param file_name:
        :return:
        """
        failed_file = base_dir + '/load_failed.txt'
        try:
            file_name = file_name.replace('*', '_')
            pdf_file = base_dir + '/' + file_name + '.pdf'

            if os.path.exists(pdf_file):
                fsize = os.path.getsize(pdf_file)
                if fsize > 0:
                    print('{} 已经存在'.format(pdf_file))
                    return

            response = requests.get(url, stream=True, timeout=300)
            if response.status_code == 200:
                print("loaded ok, starting to save:{}".format(file_name))
                with open(pdf_file, mode='wb') as fp:
                    fp.write(response.content)
                print("saved pdf in {}".format(pdf_file))
                res = np.random.choice(interval, size=1)
                print("sleep {}".format(res[0]))
                time.sleep(res[0])
            else:
                print(f"error:{response.status_code}")
                line = 'url: {}, name:{}\n'.format(url, file_name)
                print(f"error:{response.status_code}, load_file: {line}")
                with open(failed_file, mode='a', encoding='utf-8') as fp:
                    fp.write('url: {}, name:{}\n'.format(url, file_name))

                print('saved in {}'.find(failed_file))
        except Exception as e:
            time.sleep(3)
            with open(failed_file, mode='a', encoding='utf-8') as fp:
                fp.write('url: {}, name:{}\n'.format(url, file_name))

            print('saved in {}'.find(failed_file))
        print()


class ZhongGuanBu(LUBU):
    pass


class MiJiaoBu(LUBU):
    """密教部"""
    files = {'大毘盧遮那成佛神變加持經_7卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0848.pdf',
             '大毘盧遮那佛說要略念誦經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0849.pdf',
             '攝大毘盧遮那成佛神變加持經入蓮華胎藏海會悲生曼荼攞廣大念誦儀軌供養方便會_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0850.pdf',
             '大毘盧遮那經廣大儀軌_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0851.pdf',
             '大毘盧遮那成佛神變加持經蓮華胎藏悲生曼荼羅廣大成就儀軌供養方便會_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0852a.pdf',
             '大毘盧舍那成佛神變加持經蓮華胎藏悲生曼荼羅廣大成就儀軌_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0852b.pdf',
             '大毘盧遮那成佛神變加持經蓮華胎藏菩提幢標幟普通真言藏廣大成就瑜伽_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0853.pdf',
             '胎藏梵字真言_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0854.pdf',
             '青龍寺軌記_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0855.pdf',
             '大毘盧遮那成佛神變加持經略示七支念誦隨行法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0856.pdf',
             '大日經略攝念誦隨行法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0857.pdf',
             '大毘盧遮那略要速疾門五支念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0858.pdf',
             '供養儀式_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0859.pdf',
             '大日經持誦次第儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0860.pdf',
             '毘盧遮那五字真言修習儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0861.pdf',
             '阿闍梨大曼荼[打-丁+羅]灌頂儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0862.pdf',
             '大毘盧遮那經阿闍梨真實智品中阿闍梨住阿字觀門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0863.pdf',
             '大日如來劍印_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0864A.pdf',
             '胎藏金剛教法名號_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0864B.pdf',
             '金剛頂一切如來真實攝大乘現證大教王經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0865.pdf',
             '金剛頂瑜伽中略出念誦經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0866.pdf',
             '金剛峰樓閣一切瑜伽瑜祇經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0867.pdf',
             '諸佛境界攝真實經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0868.pdf',
             '金剛頂經瑜伽十八會指歸_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0869.pdf',
             '略述金剛頂瑜伽分別聖位修證法門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0870.pdf',
             '金剛頂瑜伽略述三十七尊心要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0871.pdf',
             '金剛頂瑜伽三十七尊出生義_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0872.pdf',
             '金剛頂蓮華部心念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0873.pdf',
             '金剛頂一切如來真實攝大乘現證大教王經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0874.pdf',
             '蓮華部心念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0875.pdf',
             '金剛頂瑜伽修習毘盧遮那三摩地法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0876.pdf',
             '金剛頂經毘盧遮那一百八尊法身契印_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0877.pdf',
             '金剛頂經金剛界大道場毘盧遮那如來自受用身內證智眷屬法身異名佛最上乘祕密三摩地禮懺文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0878.pdf',
             '金剛頂瑜伽三十七尊禮_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0879.pdf',
             '瑜伽金剛頂經釋字母品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0880.pdf',
             '賢劫十六尊_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0881.pdf',
             '佛說一切如來真實攝大乘現證三昧大教王經_30卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0882.pdf',
             '佛說祕密三昧大教王經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0883.pdf',
             '佛說祕密相經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0884.pdf',
             '佛說一切如來金剛三業最上祕密大教王經_7卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0885.pdf',
             '佛說金剛場莊嚴般若波羅蜜多教中一分_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0886.pdf',
             '佛說無二平等最上瑜伽大教王經_6卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0887.pdf',
             '一切祕密最上名義大教王儀軌_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0888.pdf',
             '一切如來大祕密王未曾有最上微妙大曼拏羅經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0889.pdf',
             '佛說瑜伽大教王經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0890.pdf',
             '佛說幻化網大瑜伽教十忿怒明王大明觀想儀軌經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0891.pdf',
             '佛說大悲空智金剛大教王儀軌經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0892.pdf',
             '蘇悉地羯羅經 PART 1_9卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0893a.pdf',
             '蘇悉地羯羅經 PART 2_9卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0893b.pdf',
             '蘇悉地羯羅經 PART 3_9卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0893c.pdf',
             '蘇悉地羯羅供養法 PART 1_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0894a.pdf',
             '蘇悉地羯羅供養法 PART 2_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0894b.pdf',
             '蘇婆呼童子請問經 PART 1_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0895a.pdf',
             '蘇婆呼童子請問經 PART 2_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0895b.pdf',
             '妙臂菩薩所問經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0896.pdf',
             '蕤呬耶經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0897.pdf',
             '佛說毘奈耶經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0898.pdf',
             '清淨法身毘盧遮那心地法門成就一切陀羅尼三種悉地_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0899.pdf',
             '十八契印_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0900.pdf',
             '陀羅尼集經_12卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0901.pdf',
             '總釋陀羅尼義讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0902.pdf',
             '都部陀羅尼目_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0903.pdf',
             '念誦結護法普通諸部_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0904.pdf',
             '三種悉地破地獄轉業障出三界祕密陀羅尼法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0905.pdf',
             '佛頂尊勝心破地獄轉業障出三界祕密三身佛果三種悉地真言儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0906.pdf',
             '佛頂尊勝心破地獄轉業障出三界祕密陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0907.pdf',
             '金剛頂瑜伽護摩儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0908.pdf',
             '梵天擇地法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0910.pdf',
             '建立曼荼羅及揀擇地法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0911.pdf',
             '建立曼荼羅護摩儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0912.pdf',
             '火[合*牛]供養儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0913.pdf',
             '火吽軌別錄_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0914.pdf',
             '受菩提心戒儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0915.pdf',
             '受五戒八戒文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0916.pdf',
             '無畏三藏禪要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T18n0917.pdf',
             '諸佛心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0918.pdf',
             '諸佛心印陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0919.pdf',
             '佛心經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0920.pdf',
             '阿閦如來念誦供養法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0921.pdf',
             '藥師琉璃光如來消災除難念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0922.pdf',
             '藥師如來觀行儀軌法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0923.pdf',
             '藥師如來念誦儀軌 PART 1_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0924A.pdf',
             '藥師如來念誦儀軌 PART 2_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0924B.pdf',
             '藥師儀軌一具_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0924C.pdf',
             '藥師琉璃光王七佛本願功德經念誦儀軌_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0925.pdf',
             '藥師琉璃光王七佛本願功德經念誦儀軌供養法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0926.pdf',
             '藥師七佛供養儀軌如意王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0927.pdf',
             '修藥師儀軌布壇法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0928.pdf',
             '淨琉璃淨土摽_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0929.pdf',
             '無量壽如來觀行供養儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0930.pdf',
             '金剛頂經觀自在王如來修行法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0931.pdf',
             '金剛頂經瑜伽觀自在王如來修行法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0932.pdf',
             '九品往生阿彌陀三摩地集陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0933.pdf',
             '佛說無量功德陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0934.pdf',
             '極樂願文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0935.pdf',
             '大乘無量壽經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0936.pdf',
             '佛說大乘聖無量壽決定光明王如來陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0937.pdf',
             '釋迦文尼佛金剛一乘修行儀軌法品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0938.pdf',
             '佛說大乘觀想曼拏羅淨諸惡趣經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0939.pdf',
             '佛說帝釋巖祕密成就儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0940.pdf',
             '釋迦牟尼佛成道在菩提樹降魔讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0941.pdf',
             '釋迦佛讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0942.pdf',
             '佛說無能勝幡王如來莊嚴陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0943.pdf',
             '大佛頂如來放光悉怛多缽怛囉陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0944A.pdf',
             '大佛頂大陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0944B.pdf',
             '大佛頂如來密因修證了義諸菩薩萬行首楞嚴經_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0945.pdf',
             '大佛頂廣聚陀羅尼經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0946.pdf',
             '大佛頂如來放光悉怛多般怛羅大神力都攝一切咒王陀羅尼經大威德最勝金輪三昧呪品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0947.pdf',
             '金輪王佛頂要略念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0948.pdf',
             '奇特最勝金輪佛頂念誦儀軌法要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0949.pdf',
             '菩提場所說一字頂輪王經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0950.pdf',
             '一字佛頂輪王經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0951.pdf',
             '五佛頂三昧陀羅尼經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0952.pdf',
             '一字奇特佛頂經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0953.pdf',
             '一字頂輪王念誦儀軌_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0954A.pdf',
             '一字頂輪王瑜伽觀行儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0955.pdf',
             '大陀羅尼末法中一字心呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0956.pdf',
             '金剛頂一字頂輪王瑜伽一切時處念誦成佛儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0957.pdf',
             '金剛頂經一字頂輪王儀軌音義_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0958.pdf',
             '頂輪王大曼荼羅灌頂儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0959.pdf',
             '一切如來說佛頂輪王一百八名讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0960.pdf',
             '如意寶珠轉輪祕密現身成佛金輪呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0961.pdf',
             '寶悉地成佛陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0962.pdf',
             '佛說熾盛光大威德消災吉祥陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0963.pdf',
             '佛說大威德金輪佛頂熾盛光如來消除一切災難陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0964.pdf',
             '大妙金剛大甘露軍拏利焰鬘熾盛佛頂經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0965.pdf',
             '大聖妙吉祥菩薩說除災教令法輪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0966.pdf',
             '佛頂尊勝陀羅尼經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0967.pdf',
             '最勝佛頂陀羅尼淨除業障呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0970.pdf',
             '佛說佛頂尊勝陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0971.pdf',
             '佛頂尊勝陀羅尼念誦儀軌法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0972.pdf',
             '尊勝佛頂脩瑜伽法軌儀_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0973.pdf',
             '最勝佛頂陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974A.pdf',
             '佛頂尊勝陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974B.pdf',
             '加句靈驗佛頂尊勝陀羅尼記_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974C.pdf',
             '佛頂尊勝陀羅尼注義_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974D.pdf',
             '佛頂尊勝陀羅尼真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974E.pdf',
             '佛頂尊勝陀羅尼別法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0974F.pdf',
             '白傘蓋大佛頂王最勝無比大威德金剛無礙大道場陀羅尼念誦法要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0975.pdf',
             '佛頂大白傘蓋陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0976.pdf',
             '佛說大白傘蓋總持陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0977.pdf',
             '佛說一切如來烏瑟膩沙最勝總持經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0978.pdf',
             '于瑟抳沙毘左野陀囉尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0979.pdf',
             '大勝金剛佛頂念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0980.pdf',
             '大毘盧遮那佛眼修行儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0981.pdf',
             '佛母大孔雀明王經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0982.pdf',
             '佛說大孔雀明王畫像壇場儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0983a.pdf',
             '孔雀經真言等梵本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0983b.pdf',
             '孔雀王咒經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0984.pdf',
             '佛說大孔雀咒王經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0985.pdf',
             '大金色孔雀王呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0986.pdf',
             '佛說大金色孔雀王呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0987.pdf',
             '孔雀王呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0988.pdf',
             '大雲輪請雨經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0989.pdf',
             '大雲經祈雨壇法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0990.pdf',
             '大方等大雲經請雨品第六十四_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0992.pdf',
             '大雲經請雨品第六十四_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0993.pdf',
             '新譯仁王般若經陀羅尼念誦儀軌序_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0994.pdf',
             '新譯仁王般若經陀羅尼念誦軌儀序_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0995.pdf',
             '仁王般若陀羅尼釋_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0996.pdf',
             '守護國界主陀羅尼經_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0997.pdf',
             '佛說迴向輪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0998.pdf',
             '佛說守護大千國土經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n0999.pdf',
             '成就妙法蓮華經王瑜伽觀智儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1000.pdf',
             '法華曼荼羅威儀形色法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1001.pdf',
             '不空罥索毘盧遮那佛大灌頂光真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1002.pdf',
             '大樂金剛不空真實三昧耶經般若波羅蜜多理趣釋_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1003.pdf',
             '般若波羅蜜多理趣經大樂不空三昧真實金剛薩埵菩薩等一十七聖大曼荼羅義述_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1004.pdf',
             '大寶廣博樓閣善住祕密陀羅尼經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1005A.pdf',
             '寶樓閣經梵字真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1005B.pdf',
             '廣大寶樓閣善住祕密陀羅尼經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1006.pdf',
             '牟梨曼陀羅呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1007.pdf',
             '菩提場莊嚴陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1008.pdf',
             '出生無邊門陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1009.pdf',
             '佛說出生無邊門陀羅尼儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1010.pdf',
             '佛說無量門微密持經 (一名成道降魔得一切智)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1011.pdf',
             '佛說出生無量門持經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1012.pdf',
             '阿難陀目佉尼呵離陀經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1013.pdf',
             '無量門破魔陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1014.pdf',
             '佛說阿難陀目佉尼呵離陀鄰尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1015.pdf',
             '舍利弗陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1016.pdf',
             '佛說一向出生菩薩經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1017.pdf',
             '大方廣佛華嚴經入法界品四十二字觀門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1019.pdf',
             '大方廣佛花嚴經入法界品頓證毘盧遮那法身字輪瑜伽儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1020.pdf',
             '華嚴經心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1021.pdf',
             '一切如來心祕密全身舍利寶篋印陀羅尼經 PART 1_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1022A.pdf',
             '一切如來心祕密全身舍利寶篋印陀羅尼經 PART 2_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1022B.pdf',
             '一切如來正法祕密篋印心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1023.pdf',
             '無垢淨光大陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1024.pdf',
             '佛頂放無垢光明入普門觀察一切如來心陀羅尼經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1025.pdf',
             '佛說造塔延命功德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1026.pdf',
             '金剛光焰止風雨陀羅尼經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1027a.pdf',
             '佛說護諸童子陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1028A.pdf',
             '童子經念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1028B.pdf',
             '佛說安宅陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T19n1029.pdf',
             '觀自在大悲成就瑜伽蓮華部念誦法門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1030.pdf',
             '聖觀自在菩薩心真言瑜伽觀行儀軌 (出大毘盧遮那成道經)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1031.pdf',
             '瑜伽蓮華部念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1032.pdf',
             '金剛恐怖集會方廣軌儀觀自在菩薩三世最勝心明王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1033.pdf',
             '呪五首_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1034.pdf',
             '千轉陀羅尼觀世音菩薩呪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1035.pdf',
             '千轉大明陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1036.pdf',
             '觀自在菩薩說普賢陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1037.pdf',
             '清淨觀世音普賢陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1038.pdf',
             '阿唎多羅陀羅尼阿嚕力經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1039.pdf',
             '金剛頂降三世大儀軌法王教中觀自在菩薩心真言一切如來蓮花大曼荼羅品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1040.pdf',
             '觀自在菩薩心真言一印念誦法 (千手千眼軌出)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1041.pdf',
             '觀自在菩薩大悲智印周遍法界利益眾生薰真如法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1042.pdf',
             '請觀世音菩薩消伏毒害陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1043.pdf',
             '佛說六字呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1044.pdf',
             '佛說六字神呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1045a.pdf',
             '六字神呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1045b.pdf',
             '六字大陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1046.pdf',
             '佛說聖六字大明王陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1047.pdf',
             '佛說大護明大陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1048.pdf',
             '聖六字增壽大明陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1049.pdf',
             '佛說大乘莊嚴寶王經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1050.pdf',
             '佛說一切佛攝相應大教王經聖觀自在菩薩念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1051.pdf',
             '讚觀世音菩薩頌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1052.pdf',
             '聖觀自在菩薩功德讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1053.pdf',
             '聖觀自在菩薩一百八名經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1054.pdf',
             '佛說聖觀自在菩薩梵讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1055.pdf',
             '金剛頂瑜伽千手千眼觀自在菩薩修行儀軌經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1056.pdf',
             '千眼千臂觀世音菩薩陀羅尼神呪經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1057a.pdf',
             '千手千眼觀世音菩薩姥陀羅尼身經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1058.pdf',
             '千手千眼觀世音菩薩治病合藥經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1059.pdf',
             '千手千眼觀世音菩薩廣大圓滿無礙大悲心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1060.pdf',
             '千手千眼觀自在菩薩廣大圓滿無礙大悲心陀羅尼呪本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1061.pdf',
             '千手千眼觀世音菩薩大身呪本(出大悲經中卷)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1062A.pdf',
             '世尊聖者千眼千首千足千舌千臂觀自在菩提薩埵怛嚩廣大圓滿無礙大悲心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1062B.pdf',
             '番大悲神呪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1063.pdf',
             '千手千眼觀世音菩薩大悲心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1064.pdf',
             '千光眼觀自在菩薩祕密法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1065.pdf',
             '大悲心陀羅尼修行念誦略儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1066.pdf',
             '攝無礙大悲心大陀羅尼經計一法中出無量義南方滿願補陀落海會五部諸尊等弘誓力方位及威儀形色執持三摩耶幖幟曼荼羅儀軌(但呪讚及作法宜視大儀軌內)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1067.pdf',
             '千手觀音造次第法儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1068.pdf',
             '十一面觀自在菩薩心密言念誦儀軌經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1069.pdf',
             '佛說十一面觀世音神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1070.pdf',
             '十一面神呪心經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1071.pdf',
             '聖賀野紇哩縛大威怒王立成大神驗供養念誦儀軌法品_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1072A.pdf',
             '馬頭觀音心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1072B.pdf',
             '何耶揭唎婆像法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1073.pdf',
             '何耶揭唎婆觀世音菩薩受法壇_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1074.pdf',
             '佛說七俱胝佛母准提大明陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1075.pdf',
             '七俱胝佛母所說准提陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1076.pdf',
             '佛說七俱胝佛母心大准提陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1077.pdf',
             '七佛俱胝佛母心大准提陀羅尼法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1078.pdf',
             '七俱胝獨部法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1079.pdf',
             '如意輪陀羅尼經(此經出大蓮華金剛三昧耶加持祕密無障礙經)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1080.pdf',
             '佛說觀自在菩薩如意心陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1081.pdf',
             '觀世音菩薩祕密藏如意輪陀羅尼神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1082.pdf',
             '觀世音菩薩如意摩尼陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1083.pdf',
             '觀世音菩薩如意摩尼輪陀羅尼念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1084.pdf',
             '觀自在菩薩如意輪念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1085.pdf',
             '觀自在菩薩如意輪瑜伽_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1086.pdf',
             '觀自在如意輪菩薩瑜伽法要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1087.pdf',
             '如意輪菩薩觀門義注祕訣_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1088.pdf',
             '都表如意摩尼轉輪聖王次第念誦祕密最要略法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1089.pdf',
             '佛說如意輪蓮華心如來修行觀門儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1090.pdf',
             '七星如意輪祕密要經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1091.pdf',
             '不空罥索神變真言經_30卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1092.pdf',
             '不空羂索呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1093.pdf',
             '不空羂索神呪心經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1094.pdf',
             '不空羂索呪心經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1095.pdf',
             '不空羂索陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1096.pdf',
             '不空羂索陀羅尼自在王呪經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1097.pdf',
             '佛說不空罥索陀羅尼儀軌經(一名不空羂索教法密言)_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1098.pdf',
             '佛說聖觀自在菩薩不空王祕密心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1099.pdf',
             '葉衣觀自在菩薩經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1100.pdf',
             '佛說大方廣曼殊室利經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1101.pdf',
             '金剛頂經多羅菩薩念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1102.pdf',
             '觀自在菩薩隨心呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1103a.pdf',
             '觀自在菩薩怛嚩多唎隨心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1103b.pdf',
             '佛說聖多羅菩薩經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1104.pdf',
             '聖多羅菩薩一百八名陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1105.pdf',
             '讚揚聖德多羅菩薩一百八名經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1106.pdf',
             '聖多羅菩薩梵讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1107.pdf',
             '御製救度佛母二十一種禮讚經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1108A.pdf',
             '救度佛母二十一種禮讚經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1108B.pdf',
             '白救度佛母讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1109.pdf',
             '佛說一髻尊陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1110.pdf',
             '青頸觀自在菩薩心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1111.pdf',
             '金剛頂瑜伽青頸大悲王觀自在念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1112.pdf',
             '觀自在菩薩廣大圓滿無礙大悲心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1113A.pdf',
             '大慈大悲救苦觀世音自在王菩薩廣大圓滿無礙自在青頸大悲心陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1113B.pdf',
             '毘俱胝菩薩一百八名經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1114.pdf',
             '觀自在菩薩阿麼[齒*來]法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1115.pdf',
             '廣大蓮華莊嚴曼拏羅滅一切罪陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1116.pdf',
             '佛說觀自在菩薩母陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1117.pdf',
             '佛說十八臂陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1118.pdf',
             '大樂金剛薩埵修行成就儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1119.pdf',
             '金剛頂勝初瑜伽經中略出大樂金剛薩埵念誦儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1120A.pdf',
             '勝初瑜伽儀軌真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1120B.pdf',
             '金剛頂普賢瑜伽大教王經大樂不空金剛薩埵一切時方成就儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1121.pdf',
             '金剛頂瑜伽他化自在天理趣會普賢修行念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1122.pdf',
             '金剛頂勝初瑜伽普賢菩薩念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1123.pdf',
             '普賢金剛薩埵略瑜伽念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1124.pdf',
             '金剛頂瑜伽金剛薩埵五祕密修行念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1125.pdf',
             '佛說普賢曼拏羅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1126.pdf',
             '佛說普賢菩薩陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1127.pdf',
             '最上大乘金剛大教寶王經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1128.pdf',
             '佛說金剛手菩薩降伏一切部多大教王經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1129.pdf',
             '大乘金剛髻珠菩薩修行分_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1130.pdf',
             '聖金剛手菩薩一百八名梵讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1131.pdf',
             '金剛王菩薩祕密念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1132.pdf',
             '金剛壽命陀羅尼念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1133.pdf',
             '金剛壽命陀羅尼經法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1134A.pdf',
             '金剛壽命陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1134B.pdf',
             '佛說一切如來金剛壽命陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1135.pdf',
             '佛說一切諸如來心光明加持普賢菩薩延命金剛最勝陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1136.pdf',
             '佛說善法方便陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1137.pdf',
             '金剛祕密善門陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1138a.pdf',
             '金剛祕密善門陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1138b.pdf',
             '護命法門神咒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1139.pdf',
             '佛說延壽妙門陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1140.pdf',
             '慈氏菩薩略修愈誐念誦法_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1141.pdf',
             '佛說慈氏菩薩陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1142.pdf',
             '佛說慈氏菩薩誓願陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1143.pdf',
             '佛說彌勒菩薩發願王偈_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1144.pdf',
             '虛空藏菩薩能滿諸願最勝心陀羅尼求聞持法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1145.pdf',
             '大虛空藏菩薩念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1146.pdf',
             '聖虛空藏菩薩陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1147.pdf',
             '佛說虛空藏菩薩陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1148.pdf',
             '五大虛空藏菩薩速疾大神驗祕密式經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1149.pdf',
             '轉法輪菩薩摧魔怨敵法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1150.pdf',
             '修習般若波羅蜜菩薩觀行念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1151.pdf',
             '佛說佛母般若波羅蜜多大明觀想儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1152.pdf',
             '普遍光明清淨熾盛如意寶印心無能勝大明王大隨求陀羅尼經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1153.pdf',
             '佛說隨求即得大自在陀羅尼神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1154.pdf',
             '金剛頂瑜伽最勝祕密成佛隨求即得神變加持成就陀羅尼儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1155.pdf',
             '大隨求即得大陀羅尼明王懺悔法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1156A.pdf',
             '宗叡僧正於唐國師所口受_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1156B.pdf',
             '香王菩薩陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1157.pdf',
             '地藏菩薩儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1158.pdf',
             '[峚-大+(企-止)]窖大道心驅策法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1159A.pdf',
             '佛說地藏菩薩陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1159B.pdf',
             '日光菩薩月光菩薩陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1160.pdf',
             '佛說觀藥王藥上二菩薩經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1161.pdf',
             '持世陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1162.pdf',
             '佛說雨寶陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1163.pdf',
             '佛說大乘聖吉祥持世陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1164.pdf',
             '聖持世陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1165.pdf',
             '馬鳴菩薩大神力無比驗法念誦軌儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1166.pdf',
             '八大菩薩曼荼羅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1167.pdf',
             '佛說大乘八大曼拏羅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1168A.pdf',
             '八曼荼羅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1168B.pdf',
             '佛說持明藏瑜伽大教尊那菩薩大明成就儀軌經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1169.pdf',
             '佛說金剛香菩薩大明成就儀軌經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1170.pdf',
             '金剛頂經瑜伽文殊師利菩薩法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1171.pdf',
             '金剛頂超勝三界經說文殊五字真言勝相_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1172.pdf',
             '金剛頂經曼殊室利菩薩五字心陀羅尼品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1173.pdf',
             '五字陀羅尼頌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1174.pdf',
             '金剛頂經瑜伽文殊師利菩薩供養儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1175.pdf',
             '曼殊室利童子菩薩五字瑜伽法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1176.pdf',
             '大乘瑜伽金剛性海曼殊室利千臂千鉢大教王經_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1177A.pdf',
             '千鉢文殊一百八名讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1177B.pdf',
             '文殊菩薩獻佛陀羅尼名烏蘇吒_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1178.pdf',
             '文殊師利菩薩六字呪功能法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1179.pdf',
             '六字神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1180.pdf',
             '大方廣菩薩藏經中文殊師利根本一字陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1181.pdf',
             '曼殊室利菩薩呪藏中一字呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1182.pdf',
             '一髻文殊師利童子陀羅尼念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1183.pdf',
             '大聖妙吉祥菩薩祕密八字陀羅尼修行曼荼羅次第儀軌法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1184.pdf',
             '佛說文殊師利法寶藏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1185A.pdf',
             '文殊師利寶藏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1185B.pdf',
             '佛說妙吉祥菩薩陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1186.pdf',
             '佛說最勝妙吉祥根本智最上祕密一切名義三摩地分_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1187.pdf',
             '文殊所說最勝名義經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1188.pdf',
             '佛說文殊菩薩最勝真實名義經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1189.pdf',
             '梵語阿耶曼祖悉哩捺麻捺機矴此云誦聖妙吉祥真實名經聖妙吉祥真實名經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1190.pdf',
             '大方廣菩薩藏文殊師利根本儀軌經_20卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1191.pdf',
             '妙吉祥平等祕密最上觀門大教王經_5卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1192.pdf',
             '妙吉祥平等瑜伽祕密觀身成佛儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1193.pdf',
             '妙吉祥平等觀門大教王經略出護摩儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1194.pdf',
             '大聖文殊師利菩薩讚佛法身禮_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1195.pdf',
             '曼殊室利菩薩吉祥伽陀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1196.pdf',
             '佛說文殊師利一百八名梵讚_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1197.pdf',
             '聖者文殊師利發菩提心願文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T20n1198.pdf',
             '金剛手光明灌頂經最勝立印聖無動尊大威怒王念誦儀軌法品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1199.pdf',
             '底哩三昧耶不動尊威怒王使者念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1200.pdf',
             '底哩三昧耶不動尊聖者念誦祕密法_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1201.pdf',
             '不動使者陀羅尼祕密法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1202.pdf',
             '聖無動尊安鎮家國等法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1203.pdf',
             '聖無動尊一字出生八大童子祕要法品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1204.pdf',
             '勝軍不動明王四十八使者祕密成就儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1205.pdf',
             '佛說俱利伽羅大龍勝外道伏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1206.pdf',
             '說矩里迦龍王像法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1207.pdf',
             '俱力迦羅龍王儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1208.pdf',
             '金剛頂瑜伽降三世成就極深密門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1209.pdf',
             '降三世忿怒明王念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1210.pdf',
             '甘露軍荼利菩薩供養念誦成就儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1211.pdf',
             '西方陀羅尼藏中金剛族阿蜜哩多軍吒利法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1212.pdf',
             '千臂軍荼利梵字真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1213.pdf',
             '聖閻曼德迦威怒王立成大神驗念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1214.pdf',
             '大乘方廣曼殊室利菩薩華嚴本教閻曼德迦忿怒王真言大威德儀軌品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1215.pdf',
             '大方廣曼殊室利童真菩薩華嚴本教讚閻曼德迦忿怒王真言阿毘遮嚕迦儀軌品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1216.pdf',
             '佛說妙吉祥最勝根本大教經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1217.pdf',
             '文殊師利耶曼德迦呪法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1218.pdf',
             '曼殊室利焰曼德迦萬愛祕術如意法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1219.pdf',
             '金剛藥叉瞋怒王息災大威神驗念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1220.pdf',
             '青色大金剛藥叉辟鬼魔法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1221.pdf',
             '聖迦柅忿怒金剛童子菩薩成就儀軌經_6卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1222a.pdf',
             '佛說無量壽佛化身大忿迅俱摩羅金剛念誦瑜伽儀軌法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1223.pdf',
             '金剛童子持念經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1224.pdf',
             '大威怒烏芻澁麼儀軌經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1225.pdf',
             '烏芻澁明王儀軌梵字_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1226.pdf',
             '大威力烏樞瑟摩明王經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1227.pdf',
             '穢跡金剛說神通大滿陀羅尼法術靈要門_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1228.pdf',
             '穢跡金剛禁百變法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1229.pdf',
             '佛說大輪金剛總持陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1230.pdf',
             '大輪金剛修行悉地成就及供養法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1231.pdf',
             '播般曩結使波金剛念誦儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1232.pdf',
             '佛說無能勝大明王陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1233.pdf',
             '無能勝大明陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1234.pdf',
             '無能勝大明心陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1235.pdf',
             '聖無能勝金剛火陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1236.pdf',
             '阿吒婆拘鬼神大將上佛陀羅尼神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1237.pdf',
             '阿吒婆[牛*句]鬼神大將上佛陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1238.pdf',
             '阿吒薄俱元帥大將上佛陀羅尼經修行儀軌_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1239.pdf',
             '阿吒薄[牛*句]付囑呪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1240.pdf',
             '伽馱金剛真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1241.pdf',
             '佛說妙吉祥瑜伽大教金剛陪囉嚩輪觀想成就儀軌經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1242.pdf',
             '佛說出生一切如來法眼遍照大力明王經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1243.pdf',
             '毘沙門天王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1244.pdf',
             '佛說毘沙門天王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1245.pdf',
             '摩訶吠室囉末那野提婆喝囉闍陀羅尼儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1246.pdf',
             '北方毘沙門天王隨軍護法儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1247.pdf',
             '北方毘沙門天王隨軍護法真言_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1248.pdf',
             '毘沙門儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1249.pdf',
             '北方毘沙門多聞寶藏天王神妙陀羅尼別行儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1250.pdf',
             '吽迦陀野儀軌_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1251.pdf',
             '佛說大吉祥天女十二名號經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1252a.pdf',
             '大吉祥天女十二契一百八名無垢大乘經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1253.pdf',
             '末利支提婆華鬘經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1254.pdf',
             '佛說摩利支天菩薩陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1255a.pdf',
             '佛說摩利支天經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1255b.pdf',
             '佛說摩利支天陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1256.pdf',
             '佛說大摩里支菩薩經_7卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1257.pdf',
             '摩利支菩薩略念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1258.pdf',
             '摩利支天一印法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1259.pdf',
             '大藥叉女歡喜母并愛子成就法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1260.pdf',
             '訶利帝母真言經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1261.pdf',
             '佛說鬼子母經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1262.pdf',
             '氷揭羅天童子經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1263.pdf',
             '觀自在菩薩化身蘘麌哩曳童女銷伏毒害陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1264a.pdf',
             '佛說穰麌梨童女經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1264b.pdf',
             '佛說常瞿利毒女陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1265.pdf',
             '大聖天歡喜雙身毘那夜迦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1266.pdf',
             '使咒法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1267.pdf',
             '大使咒法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1268.pdf',
             '佛說金色迦那缽底陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1269.pdf',
             '大聖歡喜雙身大自在天毘那夜迦王歸依念誦供養法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1270.pdf',
             '摩訶毘盧遮那如來定惠均等入三昧耶身雙身大聖歡喜天菩薩修行祕密法儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1271.pdf',
             '金剛薩埵說頻那夜迦天成就儀軌經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1272.pdf',
             '毘那夜迦[言*我]那缽底瑜伽悉地品祕要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1273.pdf',
             '大聖歡喜雙身毘那夜迦天形像品儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1274.pdf',
             '聖歡喜天式法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1275.pdf',
             '文殊師利菩薩根本大教王經金翅鳥王品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1276.pdf',
             '速疾立驗魔醯首羅天說阿尾奢法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1277.pdf',
             '迦樓羅及諸天密言經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1278.pdf',
             '摩醯首羅天法要_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1279.pdf',
             '摩醯首羅大自在天王神通化生伎藝天女念誦法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1280.pdf',
             '那羅延天共阿修羅王鬪戰法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1281.pdf',
             '寶藏天女陀羅尼法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1282.pdf',
             '佛說寶藏神大明曼拏羅儀軌經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1283.pdf',
             '佛說聖寶藏神儀軌經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1284.pdf',
             '佛說寶賢陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1285.pdf',
             '堅牢地天儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1286.pdf',
             '大黑天神法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1287.pdf',
             '佛說最上祕密那拏天經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1288.pdf',
             '佛說金毘羅童子威德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1289.pdf',
             '焰羅王供行法次第_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1290.pdf',
             '深沙大將儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1291.pdf',
             '法華十羅剎法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1292.pdf',
             '般若守護十六善神王形體_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1293.pdf',
             '施八方天儀則_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1294.pdf',
             '供養護世八天法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1295.pdf',
             '十天儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1296.pdf',
             '供養十二大威德天報恩品_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1297.pdf',
             '十二天供儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1298.pdf',
             '文殊師利菩薩及諸仙所說吉凶時日善惡宿曜經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1299.pdf',
             '摩登伽經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1300.pdf',
             '舍頭諫太子二十八宿經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1301.pdf',
             '諸星母陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1302.pdf',
             '佛說聖曜母陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1303.pdf',
             '宿曜儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1304.pdf',
             '北斗七星念誦儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1305.pdf',
             '北斗七星護摩祕要儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1306.pdf',
             '佛說北斗七星延命經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1307.pdf',
             '七曜攘災決_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1308.pdf',
             '七曜星辰別行法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1309.pdf',
             '北斗七星護摩法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1310.pdf',
             '梵天火羅九曜_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1311.pdf',
             '難汝計濕嚩囉天說支輪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1312.pdf',
             '佛說救拔焰口餓鬼陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1313.pdf',
             '佛說救面然餓鬼陀羅尼神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1314.pdf',
             '施諸餓鬼飲食及水法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1315.pdf',
             '佛說甘露經陀羅尼呪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1316.pdf',
             '甘露陀羅尼呪_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1317.pdf',
             '瑜伽集要救阿難陀羅尼焰口軌儀經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1318.pdf',
             '瑜伽集要焰口施食起教阿難陀緣由_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1319.pdf',
             '瑜伽集要焰口施食儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1320.pdf',
             '佛說施餓鬼甘露味大陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1321.pdf',
             '新集浴像儀軌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1322.pdf',
             '除一切疾病陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1323.pdf',
             '能淨一切眼疾病陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1324.pdf',
             '佛說療痔病經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1325.pdf',
             '佛說呪時氣病經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1326.pdf',
             '佛說呪齒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1327.pdf',
             '佛說呪目經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1328.pdf',
             '佛說呪小兒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1329.pdf',
             '囉嚩拏說救療小兒疾病經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1330.pdf',
             '佛說灌頂七萬二千神王護比丘呪經_12卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1331.pdf',
             '七佛八菩薩所說大陀羅尼神呪經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1332.pdf',
             '虛空藏菩薩問七佛陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1333.pdf',
             '如來方便善巧呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1334.pdf',
             '大吉義神呪經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1335.pdf',
             '陀羅尼雜集_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1336.pdf',
             '種種雜咒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1337.pdf',
             '咒三首經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1338.pdf',
             '大方等陀羅尼經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1339.pdf',
             '大法炬陀羅薩經_20卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1340.pdf',
             '大威德陀羅尼經_20卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1341.pdf',
             '佛說無崖際總持法門經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1342.pdf',
             '尊勝菩薩所問一切諸法入無量門陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1343.pdf',
             '金剛上味陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1344.pdf',
             '金剛場陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1345.pdf',
             '諸佛集會陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1346.pdf',
             '息除中夭陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1347.pdf',
             '佛說十二佛名神呪校量功德除障滅罪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1348.pdf',
             '佛說稱讚如來功德神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1349.pdf',
             '佛說一切如來名號陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1350.pdf',
             '佛說持句神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1351.pdf',
             '佛說陀鄰尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1352.pdf',
             '東方最勝燈王陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1353.pdf',
             '東方最勝燈王如來經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1354.pdf',
             '佛說聖最上燈明如來陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1355.pdf',
             '佛說華積陀羅尼神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1356.pdf',
             '佛說師子奮迅菩薩所問經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1357.pdf',
             '佛說花聚陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1358.pdf',
             '佛說花積樓閣陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1359.pdf',
             '六門陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1360.pdf',
             '六門陀羅尼經論_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1361.pdf',
             '佛說善夜經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1362.pdf',
             '勝幢臂印陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1363.pdf',
             '妙臂印幢陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1364.pdf',
             '八名普密陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1365.pdf',
             '佛說祕密八名陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1366.pdf',
             '佛說大普賢陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1367.pdf',
             '佛說大七寶陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1368.pdf',
             '百千印陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1369a.pdf',
             '佛說持明藏八大總持王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1370.pdf',
             '佛說聖大總持王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1371.pdf',
             '增慧陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1372.pdf',
             '佛說施一切無畏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1373.pdf',
             '佛說一切功德莊嚴王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1374.pdf',
             '佛說莊嚴王陀羅尼呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1375.pdf',
             '佛說聖莊嚴陀羅尼經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1376.pdf',
             '佛說寶帶陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1377.pdf',
             '佛說玄師颰陀所說神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1378a.pdf',
             '幻師颰陀神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1378b.pdf',
             '佛說大愛陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1379.pdf',
             '佛說善樂長者經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1380.pdf',
             '佛說大吉祥陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1381.pdf',
             '佛說宿命智陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1382.pdf',
             '佛說宿命智陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1383.pdf',
             '佛說缽蘭那賒嚩哩大陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1384.pdf',
             '佛說俱枳羅陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1385.pdf',
             '佛說妙色陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1386.pdf',
             '佛說栴檀香身陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1387.pdf',
             '佛說無畏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1388.pdf',
             '佛說無量壽大智陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1389.pdf',
             '佛說洛叉陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1390.pdf',
             '佛說檀特羅麻油述經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1391.pdf',
             '大寒林聖難拏陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1392.pdf',
             '佛說摩尼羅亶經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1393.pdf',
             '佛說安宅神呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1394.pdf',
             '拔濟苦難陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1395.pdf',
             '佛說拔除罪障呪王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1396.pdf',
             '智炬陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1397.pdf',
             '佛說智光滅一切業障陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1398.pdf',
             '佛說滅除五逆罪大陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1399.pdf',
             '佛說消除一切災障寶髻陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1400.pdf',
             '佛說大金剛香陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1401.pdf',
             '消除一切閃電障難隨求如意陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1402.pdf',
             '佛說如意摩尼陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1403.pdf',
             '佛說如意寶總持王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1404.pdf',
             '佛說息除賊難陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1405.pdf',
             '佛說辟除賊害呪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1406.pdf',
             '佛說辟除諸惡陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1407.pdf',
             '佛說最上意陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1408.pdf',
             '佛說聖最勝陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1409.pdf',
             '佛說勝幡瓔珞陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1410.pdf',
             '佛說蓮華眼陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1411.pdf',
             '佛說寶生陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1412.pdf',
             '佛說尊勝大明王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1413.pdf',
             '佛說金身陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1414.pdf',
             '大金剛妙高山樓閣陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1415.pdf',
             '金剛摧碎陀羅尼_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1416.pdf',
             '佛說壞相金剛陀羅尼經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1417.pdf',
             '佛說一切如來安像三昧儀軌經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1418.pdf',
             '佛說造像量度經解_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1419.pdf',
             '龍樹五明論_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra10/T21n1420.pdf'}


class AHanBu(LUBU):
    pass

# 已开始
name2url_task1 = \
    {'毘曇部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra13.jsp',
     '中觀部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra14.jsp',
     '瑜伽部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra15.jsp'}

# 已开始
name2url_task3 = \
    {'論集部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra16.jsp',
     '經疏部':'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra17.jsp',
     '律疏部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra18.jsp',
     '論疏部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra19.jsp'}

# 已开始
name2url_task4 = \
    {'諸宗部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra20.jsp',
     '史傳部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra21.jsp',
     '事彙部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra22.jsp',
     '外教部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra23.jsp'}

# 已开始
name2url_task1 = \
    {'目錄部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra24.jsp',
     '古逸部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra25.jsp',
     '疑似部': 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra26.jsp'}

if __name__ == '__main__':
    bdir = r'C:\Users\daijitao\Desktop\data\data\經集部'
    fiels = {}
    with open(bdir +'/load_failed.txt', encoding='utf-8') as fp:
        for line in fp:
            data = [data for data in line.strip().split(',')]
            url = data[0].split(':')[-1].strip()
            name = data[1].split(':')[-1].strip()
            fiels[name] = 'https:' + url
    print(fiels)
    task = ZhongGuanBu(url, name, files=fiels)
    task.load(bdir)

if __name__ == '__main__1':
    name = '阿含部'
    url = 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra1.jsp'
    bdir = r'D:/myData/大正藏典籍分类/{}'.format(name)
    mkdir(bdir)
    files = {'長阿含經_22卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0001.pdf',
             '佛說七佛經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0002.pdf',
             '毘婆尸佛經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0003.pdf',
             '七佛父母姓字經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0004.pdf',
             '佛般泥洹經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0005.pdf',
             '般泥洹經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0006.pdf',
             '大般涅槃經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0007.pdf',
             '大堅固婆羅門緣起經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0008.pdf',
             '佛說人仙經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0009.pdf',
             '白衣金幢二婆羅門緣起經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0010.pdf',
             '尼拘陀梵志經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0011.pdf',
             '大集法門經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0012.pdf',
             '長阿含十報法經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0013.pdf',
             '佛說人本欲生經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0014.pdf',
             '佛說帝釋所問經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0015.pdf',
             '佛說尸迦羅越六方禮經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0016.pdf',
             '佛說善生子經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0017.pdf',
             '佛說信佛功德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0018.pdf',
             '佛說大三摩惹經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0019.pdf',
             '佛開解梵志阿颰經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0020.pdf',
             '佛說梵網六十二見經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0021.pdf',
             '佛說寂志果經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0022.pdf',
             '大樓炭經_6卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0023.pdf',
             '起世經_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0024.pdf',
             '起世因本經_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0025.pdf',
             '中阿含經_60卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0026.pdf',
             '佛說七知經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0027.pdf',
             '佛說園生樹經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0028.pdf',
             '佛說鹹水喻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0029.pdf',
             '佛說薩缽多酥哩踰捺野經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0030.pdf',
             '佛說一切流攝守因經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0031.pdf',
             '佛說四諦經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0032.pdf',
             '佛說恒水經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0033.pdf',
             '佛說法海經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0034.pdf',
             '佛說海八德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0035.pdf',
             '佛說本相猗致經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0036.pdf',
             '佛說緣本致經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0037.pdf',
             '佛說輪王七寶經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0038.pdf',
             '佛說頂生王故事經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0039.pdf',
             '佛說文陀竭王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0040.pdf',
             '佛說頻婆娑羅王經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0041.pdf',
             '佛說鐵城泥犁經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0042.pdf',
             '佛說閻羅王五天使者經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0043.pdf',
             '佛說古來世時經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0044.pdf',
             '大正句王經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0045.pdf',
             '佛說阿那律八念經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0046.pdf',
             '佛說離睡經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0047.pdf',
             '佛說是法非法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0048.pdf',
             '佛說求欲經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0049.pdf',
             '佛說受歲經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0050.pdf',
             '佛說梵志計水淨經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0051.pdf',
             '佛說大生義經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0052.pdf',
             '佛說苦陰經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0053.pdf',
             '佛說釋摩男本四子經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0054.pdf',
             '佛說苦陰因事經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0055.pdf',
             '佛說樂想經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0056.pdf',
             '佛說漏分布經 (出中阿含令劫意)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0057.pdf',
             '佛說阿耨風經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0058.pdf',
             '佛說諸法本經 (出中阿含別翻)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0059.pdf',
             '佛說瞿曇彌記果經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0060.pdf',
             '佛說受新歲經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0061.pdf',
             '佛說新歲經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0062.pdf',
             '佛說解夏經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0063.pdf',
             '佛說瞻婆比丘經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0064.pdf',
             '佛說伏婬經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0065.pdf',
             '佛說魔嬈亂經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0066.pdf',
             '弊魔試目連經 (一名魔嬈亂經)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0067.pdf',
             '佛說賴吒和羅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0068.pdf',
             '佛說護國經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0069.pdf',
             '佛說數經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0070.pdf',
             '梵志頞波羅延問種尊經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0071.pdf',
             '佛說三歸五戒慈心厭離功德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0072.pdf',
             '佛說須達經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0073.pdf',
             '佛說長者施報經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0074.pdf',
             '佛為黃竹園老婆羅門說學經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0075.pdf',
             '梵摩渝經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0076.pdf',
             '佛說尊上經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0077.pdf',
             '佛說兜調經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0078.pdf',
             '佛說鸚鵡經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0079.pdf',
             '佛為首迦長者說業報差別經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0080.pdf',
             '分別善惡報應經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0081.pdf',
             '佛說意經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0082.pdf',
             '佛說應法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0083.pdf',
             '佛說分別布施經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0084.pdf',
             '佛說息諍因緣經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0085.pdf',
             '佛說泥犁經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0086.pdf',
             '佛說齋經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0087.pdf',
             '優陂夷墮舍迦經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0088.pdf',
             '佛說八關齋經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0089.pdf',
             '佛說鞞摩肅經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0090.pdf',
             '佛說婆羅門子命終愛念不離經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0091.pdf',
             '佛說十支居士八城人經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0092.pdf',
             '佛說邪見經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0093.pdf',
             '佛說箭喻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0094.pdf',
             '佛說蟻喻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0095.pdf',
             '佛說治意經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0096.pdf',
             '廣義法門經 (出中阿含經一品)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0097.pdf',
             '佛說普法義經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T01n0098.pdf',
             '雜阿含經_50卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0099.pdf',
             '別譯雜阿含經_16卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0100.pdf',
             '雜阿含經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0101.pdf',
             '佛說五蘊皆空經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0102.pdf',
             '佛說聖法印經 (天竺名阿遮曇摩文圖)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0103.pdf',
             '佛說法印經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0104.pdf',
             '五陰譬喻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0105.pdf',
             '佛說水沫所漂經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0106.pdf',
             '佛說不自守意經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0107.pdf',
             '佛說滿願子經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0108.pdf',
             '佛說轉法輪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0109.pdf',
             '佛說三轉法輪經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0110.pdf',
             '佛說相應相可經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0111.pdf',
             '佛說八正道經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0112.pdf',
             '佛說難提釋經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0113.pdf',
             '佛說馬有三相經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0114.pdf',
             '佛說馬有八態譬人經 (出雜阿含別譯)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0115.pdf',
             '佛說戒德香經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0116.pdf',
             '佛說戒香經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0117.pdf',
             '佛說鴦掘摩經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0118.pdf',
             '佛說鴦崛髻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0119.pdf',
             '央掘魔羅經_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0120.pdf',
             '佛說月喻經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0121.pdf',
             '佛說波斯匿王太后崩塵土坌身經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0122.pdf',
             '佛說放牛經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0123.pdf',
             '緣起經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0124.pdf',
             '增壹阿含經_51卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0125.pdf',
             '佛說阿羅漢具德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0126.pdf',
             '佛說四人出現世間經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0127.pdf',
             '須摩提女經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0128a.pdf',
             '佛說三摩竭經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0129.pdf',
             '佛說給孤長者女得度因緣經_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0130.pdf',
             '佛說婆羅門避死經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0131.pdf',
             '佛說食施獲五福報經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0132a.pdf',
             '施食獲五福報經  (亦名佛說施色力經)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0132b.pdf',
             '頻毘娑羅王詣佛供養經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0133.pdf',
             '佛說長者子六過出家經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0134.pdf',
             '佛說力士移山經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0135.pdf',
             '佛說四未曾有法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0136.pdf',
             '舍利弗摩訶目連遊四衢經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0137.pdf',
             '佛說十一想思念如來經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0138.pdf',
             '佛說四泥犁經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0139.pdf',
             '阿那邠邸化七子經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0140.pdf',
             '佛說阿遬達經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0141.pdf',
             '佛說玉耶女經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0142a.pdf',
             '玉耶女經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0142b.pdf',
             '玉耶經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0143.pdf',
             '佛說大愛道般泥洹經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0144.pdf',
             '佛母般泥洹經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0145.pdf',
             '舍衛國王夢見十事經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0146.pdf',
             '佛說舍衛國王十夢經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0147.pdf',
             '國王不梨先泥十夢經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0148.pdf',
             '佛說阿難同學經 (出增一阿含經)_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0149.pdf',
             '佛說七處三觀經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0150A.pdf',
             '佛說九橫經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0150B.pdf',
             '佛說阿含正行經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra1/T02n0151.pdf'}

    task = ZhongGuanBu(url, name, files=files)
    task.load(bdir)


def zhongguan():
    name = '中觀部'
    url = 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra14.jsp'
    bdir = r'D:/myData/大正藏典籍分类/{}'.format(name)
    mkdir(bdir)

    task = ZhongGuanBu(url, name)
    task.load(bdir)


def mijiao():
    name = '密教部'
    url = 'https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra10.jsp'
    bdir = r'D:/myData/大正藏典籍分类/{}'.format(name)
    mkdir(bdir)

    mijiao = MiJiaoBu(url, name, files=MiJiaoBu.files)
    mijiao.load(bdir)


if __name__ == '__main__1':
    url = "https://buddhism.lib.ntu.edu.tw/sutra/chinese/taisho/sutra11.jsp"
    files = {'彌沙塞部和醯五分律_30卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1421.pdf',
             '彌沙塞五分戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1422a.pdf',
             '五分戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1422b.pdf',
             '五分比丘尼戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1423.pdf',
             '彌沙塞羯磨本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1424.pdf',
             '摩訶僧祇律_40卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1425.pdf',
             '摩訶僧祇律大比丘戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1426.pdf',
             '摩訶僧祇比丘尼戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1427.pdf',
             '四分律_60卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1428.pdf',
             '四分律比丘戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1429.pdf',
             '四分僧戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1430.pdf',
             '四分比丘尼戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1431.pdf',
             '曇無德律部雜羯磨_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1432.pdf',
             '羯磨_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1433.pdf',
             '四分比丘尼羯磨法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T22n1434.pdf',
             '十誦律_61卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1435.pdf',
             '十誦比丘波羅提木叉戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1436.pdf',
             '十誦比丘尼波羅提木叉戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1437.pdf',
             '大沙門百一羯磨法_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1438.pdf',
             '十誦羯磨比丘要用_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1439.pdf',
             '薩婆多毘尼毘婆沙_9卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1440.pdf',
             '薩婆多部毘尼摩得勒伽_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1441.pdf',
             '根本說一切有部毘奈耶_50卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1442.pdf',
             '根本說一切有部苾芻尼毘奈耶_20卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1443.pdf',
             '根本說一切有部毘奈耶出家事_4卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1444.pdf',
             '根本說一切有部毘奈耶安居事_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1445.pdf',
             '根本說一切有部毘奈耶隨意事_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1446.pdf',
             '根本說一切有部毘奈耶皮革事_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T23n1447.pdf',
             '根本說一切有部毘奈耶藥事_18卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1448.pdf',
             '根本說一切有部毘奈耶羯恥那衣事_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1449.pdf',
             '根本說一切有部毘奈耶破僧事_20卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1450.pdf',
             '根本說一切有部毘奈耶雜事_40卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1451.pdf',
             '根本說一切有部尼陀那_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1452.pdf',
             '根本說一切有部百一羯磨_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1453.pdf',
             '根本說一切有部戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1454.pdf',
             '根本說一切有部苾芻尼戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1455.pdf',
             '根本說一切有部毘奈耶尼陀那目得迦攝頌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1456.pdf',
             '根本說一切有部略毘奈耶雜事攝頌_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1457.pdf',
             '根本薩婆多部律攝_14卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1458.pdf',
             '根本說一切有部毘奈耶頌_3卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1459.pdf',
             '解脫戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1460.pdf',
             '律二十二明了論_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1461.pdf',
             '善見律毘婆沙_18卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1462.pdf',
             '毘尼母經_8卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1463.pdf',
             '鼻奈耶_10卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1464.pdf',
             '舍利弗問經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1465.pdf',
             '優波離問佛經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1466.pdf',
             '佛說犯戒罪報輕重經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1467a.pdf',
             '佛說目連所問經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1468.pdf',
             '佛說迦葉禁戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1469.pdf',
             '大比丘三千威儀_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1470.pdf',
             '沙彌十戒法并威儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1471.pdf',
             '沙彌威儀_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1472.pdf',
             '佛說沙彌十戒儀則經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1473.pdf',
             '沙彌尼戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1474.pdf',
             '沙彌尼離戒文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1475.pdf',
             '佛說優婆塞五戒相經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1476.pdf',
             '佛說戒消災經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1477.pdf',
             '大愛道比丘尼經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1478.pdf',
             '佛說苾芻五法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1479.pdf',
             '佛說苾芻迦尸迦十法經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1480.pdf',
             '佛說五恐怖世經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1481.pdf',
             '佛阿毘曇經出家相品_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1482.pdf',
             '佛說目連問戒律中五百輕重事_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1483a.pdf',
             '佛說目連問戒律中五百輕重事經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1483b.pdf',
             '梵網經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1484.pdf',
             '菩薩瓔珞本業經_2卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1485.pdf',
             '受十善戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1486.pdf',
             '佛說菩薩內戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1487.pdf',
             '優婆塞戒經_7卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1488.pdf',
             '清淨毘尼方廣經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1489.pdf',
             '寂調音所問經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1490.pdf',
             '菩薩藏經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1491.pdf',
             '佛說舍利弗悔過經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1492.pdf',
             '大乘三聚懺悔經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1493.pdf',
             '佛說淨業障經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1494.pdf',
             '善恭敬經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1495.pdf',
             '佛說正恭敬經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1496.pdf',
             '佛說大乘戒經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1497.pdf',
             '佛說八種長養功德經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1498.pdf',
             '菩薩戒羯磨文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1499.pdf',
             '菩薩戒本_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1500.pdf',
             '菩薩受齋經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1502.pdf',
             '優婆塞五戒威儀經_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1503.pdf',
             '菩薩五法懺悔文_1卷': 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra11/T24n1504.pdf'}

    name = '律部'
    bdir = r'D:\myData\大正藏典籍分类\{}'.format(name)
    mkdir(bdir)
    lubu = LUBU()
    lubu.load(bdir)

if __name__ == '__main__2':
    path = r'D:\myData\大正藏典籍分类\{}'

    url = 'http://buddhism.lib.ntu.edu.tw/FULLTEXT/sutra/chi_pdf/sutra15/T32n1628.pdf'

    response = requests.get(url, stream=True, timeout=300)
    if response.status_code == 200:
        print("loaded ok, starting to save:")
        with open(base_dir, mode='wb') as fp:
            fp.write(response.content)
        print("saved pdf in {}".format(base_dir))
        res = np.random.choice(interval, size=1)
        print("sleep {}".format(res[0]))
        time.sleep(res[0])
    else:
        print(f"error:{response.status_code}")

if __name__ == '__main__1':
    """"大乘般若部": [16, 18], "大乘寶積部": [19, 23], "大乘大集部": [23, 26],
             "大乘經華嚴": [27, 32], "大乘涅槃部": [32, 35], 
                          "大乘五大部外重譯經": [43, 46], "小乘單譯經": [65, 66], 
             "大乘單譯經": [47, 54], "小乘阿含部": [55, 62], "大乘律": [76, 77], 
             "小乘律": [77, 91], "大乘論": [92, 105], "小乘論": [106, 125], "宋元入藏諸大小乘經": [75, 75],
             "宋元續入藏諸論": [125, 126], "西土聖賢撰集": [127, 132],
             # ---
    parts = {
        "此土著述": [133, 183],
        "大明續入藏": [183, 195], "附入南藏函": [196, 200]
    }
    """

    names = mk_name(150, 168)
    part_dir = r"C:\Users\daijitao\Downloads\乾隆大藏经"
    for name in names:
        url = f"https://buddhism.lib.ntu.edu.tw/sutra/chinese/dragon/sutra/{name}.pdf"
        base_dir = part_dir + '\{}.pdf'.format(name)
        print("loading pdf:{}".format(base_dir))
        if os.path.exists(base_dir):
            print("pdf:{} 已经存在".format(base_dir))
            continue

        response = requests.get(url, stream=True, timeout=300)
        if response.status_code == 200:
            print("loaded ok, starting to save:")
            with open(base_dir, mode='wb') as fp:
                fp.write(response.content)
            print("saved pdf in {}".format(base_dir))
            res = np.random.choice(interval, size=1)
            print("sleep {}".format(res[0]))
            time.sleep(res[0])
        else:
            print(f"error:{response.status_code}")
