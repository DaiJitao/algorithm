import numpy as np
import os
import requests


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


if __name__ == '__main__':
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

    interval = [100, 20, 30, 40, 123, 5, 15, 18, 1.6, 19, 17, 16, 5, 54.5, 33.8, 21.8, 6.6, 8, 7, 10, 11, 12.3, 4, 5.5, 14, 5]
    import time




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
