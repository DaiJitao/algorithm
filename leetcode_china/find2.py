import json
import numpy as np
import pandas
import time
import os


def get_id(file):
    df = pandas.read_csv(file)
    industryid = df['industryid']
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

            if siteId in siteid_list or channelId in channelid_list:
                d = {"siteId": siteId, "channelId": channelId, "assetId": assetId, "fileName": fileName}
                out_data.write(json.dumps(d))
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


path = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\local_L_20191014041525_7887_yuqing-consumer-group.txt"

if __name__ == "__main__":
    local_file_path = "C:/Users/dell/Desktop/classify/"
    industrycsv = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\industry_column.csv"
    channelid_list, siteid_list = get_id(industrycsv)
    fileNames = os.listdir(local_file_path)
    outFile = "./data/filted.txt"
    out_data = open(outFile, mode="w+", encoding="utf-8")
    for fileName in fileNames:
        filter_file(inFilePath=local_file_path, fileName=fileName, channelid_list=channelid_list,
                    siteid_list=siteid_list, out_data=out_data)
    print("文件保存完毕")
    out_data.close()
