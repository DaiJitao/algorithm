import json


def save_to_excel(inf: str, data: dict):
    import pandas as pd
    dataFrame = pd.DataFrame(data)
    writer = pd.ExcelWriter(inf)
    dataFrame.to_excel(writer, index=False)
    writer.save()


# inf = r'C:\Users\daijitao\Desktop\base_result.txt'
# with open(inf, encoding='utf-8') as fp:
#     data = json.loads(fp.read())
#     titles = []
#     predict1 = []
#     predict2 = []
#     predict3 = []
#     contents = []
#     for obj in data:
#         titles.append(obj['title'])
#         contents.append(obj['content'])
#         predict1.append(obj['predict1'])
#         predict2.append(obj['predict2'])
#         predict3.append(obj['predict3'])
#
#     res = {'原文标题': titles, 'GPT生成的标题1': predict1, 'GPT生成的标题2': predict2, 'GPT生成的标题3': predict3, "政策原文": contents}
#     save_to_excel('GPT2文本写作效果.xls', res)


if __name__ == '__main__':
    import numpy as np

    p1 = np.random.standard_normal(798)
    p2 = np.random.standard_normal(798)
    p1 = np.random.uniform(low=0, high=1,size=798)
    p2 = np.random.uniform(low=0, high=1, size=798)

    d = np.dot(p1, p2)
    print(d/np.sqrt(798))

    m = np.array([[1, 2, 3], [4, 5, 6]])  ##2X3
    n = np.array([[1, 2], [3, 4], [5, 6]])  ##3X2
    p = np.dot(m, n)
    q = np.matmul(m, n)
    print(p, '\n', q)
