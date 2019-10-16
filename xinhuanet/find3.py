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


def readKafkaFile(infile, outwebGroupIdFile, outindustryDynamicFile, outAssetInIndustrysFile,
                  outAssetInIndustrysSecondlevelFile):
    try:
        outwebGroupIdData = open(outwebGroupIdFile, mode='a+', encoding="utf-8")
        outindustryDynamicData = open(outindustryDynamicFile, mode='a+', encoding="utf-8")
        outAssetInIndustrysData = open(outAssetInIndustrysFile, mode='a+', encoding="utf-8")
        outAssetInIndustrysSecondlevelData = open(outAssetInIndustrysSecondlevelFile, mode='a+', encoding="utf-8")
        count = 0
        with open(infile, encoding='utf-8', mode="r") as f:
            lines = f.readlines()
            for line in lines:
                res = json.loads(line)
                taskID = res["taskId"]
                if "L:2019101518" in taskID:
                    count += 1
                    listData = res['data']
                    setIDs = set()
                    for temp in listData:
                        webGroupId = temp['webGroupId']
                        industryDynamic = temp['industryDynamic']
                        assetInIndustrys = temp['assetInIndustrys']
                        assetInIndustrysSecondlevel = temp['assetInIndustrysSecondlevel']
                        if webGroupId == "1":
                            assetId = temp['assetId']
                            setIDs.add(taskID)
                            d = {"taskId": taskID, "assetId": assetId, "webGroupId": webGroupId}
                            outwebGroupIdData.write(json.dumps(d))
                            outwebGroupIdData.write("\n")
                        if industryDynamic != "0":
                            assetId = temp['assetId']
                            d = {"taskId": taskID, "assetId": assetId, "industryDynamic": industryDynamic}
                            outindustryDynamicData.write(json.dumps(d))
                            outindustryDynamicData.write("\n")
                        if assetInIndustrys == 1:
                            assetId = temp['assetId']
                            d = {"taskId": taskID, "assetId": assetId, "assetInIndustrys": assetInIndustrys}
                            outAssetInIndustrysData.write(json.dumps(d))
                            outAssetInIndustrysData.write("\n")
                        if assetInIndustrysSecondlevel != "":
                            assetId = temp['assetId']
                            d = {"taskId": taskID, "assetId": assetId,
                                 "assetInIndustrysSecondlevel": assetInIndustrysSecondlevel}
                            outAssetInIndustrysSecondlevelData.write(json.dumps(d))
                            outAssetInIndustrysSecondlevelData.write("\n")
                    if count % 100 == 0:
                        print("写入！已遍历", count, "次")
                        outAssetInIndustrysSecondlevelData.flush()
                        outAssetInIndustrysData.flush()
                        outindustryDynamicData.flush()
                        outwebGroupIdData.flush()
            #
            outAssetInIndustrysSecondlevelData.close()
            outAssetInIndustrysData.close()
            outindustryDynamicData.close()
            outwebGroupIdData.close()
    except Exception as e:
        print("读取文件失败！" + infile, e)


if __name__ == "__main__":
    infile = "/data/program/kafka211100/bin/20191015kafka.txt"
    outwebGroupIdFile = "./webGroupId.txt"
    outAssetInIndustrysSecondlevelFile = "./assetInIndustrysSecondlevel.txt"
    outAssetInIndustrysFile = "./assetInIndustrys.txt"
    outindustryDynamicFile = "./industryDynamic.txt"
    readKafkaFile(infile=infile, outwebGroupIdFile=outwebGroupIdFile,
                  outAssetInIndustrysFile=outAssetInIndustrysFile,
                  outAssetInIndustrysSecondlevelFile=outAssetInIndustrysSecondlevelFile,
                  outindustryDynamicFile=outindustryDynamicFile)
