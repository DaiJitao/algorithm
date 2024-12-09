from typing import List, Optional
import json


inf = r'D:\myData\易车\大模型调研\T5数据集\squad1.1\dev-v1.1.json'

if __name__ == '__main__':
    with open(inf,mode='r', encoding='utf-8') as fp:
        data = fp.read().strip()
        jdata = json.loads(data)
        arr = jdata['data']
        print(f'---->几个文章：{len(arr)}')
        for obj in arr:
            paragraphs = obj['paragraphs']
            count = 0
            for inner in paragraphs:
                size = len(inner['qas'])
                count += size

        print(f'------->count:{count}')
