import json
import numpy as np
import pandas
import time


def get_id(file):
    df = pandas.read_csv(file)
    industryid = df['industryid']
    channelid = df[['channelid']].drop_duplicates()
    siteid = df[["siteid"]].drop_duplicates()
    return list(channelid['channelid']), list(siteid['siteid'])


def save_file(content, file):
    with open(file, mode="w+", encoding="utf-8") as f:
        f.write(content)


"""行业动态"""


def filter_file(file, siteId, channelId):
    content = ""
    try:
        with open(file, encoding='utf-8', mode="r") as f:
            line = f.read().strip()
            print(line)
            content = json.loads(line)

    except Exception as e:
        print("读取文件失败！" + file, e)

    datas = content["data"]
    for data in datas:
        siteId = data["siteId"]
        channelId = data["channelId"]
        assetId = data["assetId"]
        # 匹配


def remove(path=None):
    import os
    delFiles = "C:/Users/dell/Desktop/test2/classify/"
    files = os.listdir(delFiles)
    count = 0
    try:
        for file in files:
            if file.startswith("L_"):
                os.remove(delFiles + file)
                count += 1
                print(count)
    except Exception as e:
        print(e)



path = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\local_L_20191014041525_7887_yuqing-consumer-group.txt"
csvfile = r"F:\pycharm_workspce\dai_github\algorithm\leetcode_china\data\industry_column.csv"

if __name__ == "__main__":
    local_file_path = r"C:\Users\dell\Desktop\classify"
    while True:
        time.sleep(5)
        remove()
