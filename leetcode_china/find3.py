import json
import numpy as np
import pandas
import time
import os


def get_id(file):
    df = pandas.read_csv(file)
    channelid = df[['channelid']].drop_duplicates().astype("str")
    siteid = df[["siteid"]].drop_duplicates().astype("str")
    return list(channelid['channelid']), list(siteid['siteid'])


"""行业动态"""


def filter_file(inFilePath, fileName, channelid_list, siteid_list, out_data):
    content = ""
    try:
        file = inFilePath + fileName
        with open(file, encoding='utf-8', mode="r") as f:
            line = f.read().strip()
            content = json.loads(line)  # 转换为字典

    except Exception as e:
        print("读取文件失败！" + file, e)

    try:
        datas = content["data"]
        for data in datas:
            siteId = data["siteId"]
            channelId = data["channelId"]
            assetId = data["assetId"]
            if siteId == None or channelId == None:
                raise Exception("siteId == None or channelId == None")
            if str(siteId) in siteid_list or str(channelId) in channelid_list:
                d = {"siteId": siteId, "channelId": channelId, "assetId": assetId, "fileName": fileName}
                out_data.write(json.dumps(d))
                print(d)
    except Exception as e:
        print(e)


def remove(path=None):
    delFiles = "C:/Users/dell/Desktop/test2/classify/"
    files = os.listdir(delFiles)
    count = 0
    for file in files:
        if file.startswith("L_"):
            os.remove(delFiles + file)
            count += 1
            print(count)



if __name__ == "__main__":
    local_file_path = "C:/Users/dell/Desktop/test2/classify/"
    # industrycsv = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\industry_column.csv"
    # channelid_list, siteid_list = get_id(industrycsv)
    # 行业站点
    rank_sitecsv = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\rank_site.csv"
    channelid_list, siteid_list = get_id(rank_sitecsv)

    # outFile = "./data/dyn_filted3.txt"
    outFileRankSite = "./data/ranksit_filted.txt"

    fileNames = os.listdir(local_file_path)
    middleIndex = int(len(fileNames) / 2)
    fileNamesPart1 = fileNames[:middleIndex]
    fileNamesPart2 = fileNames[middleIndex:]

    count = 0
    for fileName in fileNames:
        if count % 500 == 0:
            out_data = open(outFileRankSite, mode="a+", encoding="utf-8")
            filter_file(inFilePath=local_file_path, fileName=fileName, channelid_list=channelid_list,
                        siteid_list=siteid_list, out_data=out_data)
            print(count, fileName, "--文件保存完毕")
            out_data.close()
        count += 1
