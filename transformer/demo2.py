import json


def save_to_excel(inf: str, data: dict):
    import pandas as pd
    dataFrame = pd.DataFrame(data)
    writer = pd.ExcelWriter(inf)
    dataFrame.to_excel(writer, index=False)
    writer.save()


inf = r'C:\Users\daijitao\Desktop\base_result.txt'
with open(inf, encoding='utf-8') as fp:
    data = json.loads(fp.read())
    titles = []
    predict1 = []
    predict2 = []
    predict3 = []
    contents = []
    for obj in data:
        titles.append(obj['title'])
        contents.append(obj['content'])
        predict1.append(obj['predict1'])
        predict2.append(obj['predict2'])
        predict3.append(obj['predict3'])

    res = {'原文标题': titles, 'GPT生成的标题1': predict1, 'GPT生成的标题2': predict2, 'GPT生成的标题3': predict3, "政策原文": contents}
    save_to_excel('GPT2文本写作效果.xls', res)

