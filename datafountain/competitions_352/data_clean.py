import pandas as pd

base_dir = "./datasets/train/"
# 历史销量数据
train_sales_data = base_dir + "train_sales_data.csv"
# 车型搜索数据
train_search_data = base_dir + "train_search_data.csv"
# 汽车垂直媒体新闻评论数据和车型评论数据
train_user_reply_data = base_dir + "train_user_reply_data.csv"

train_sales_data = pd.read_csv(train_sales_data)
train_search_data = pd.read_csv(train_search_data)
train_user_reply_data = pd.read_csv(train_user_reply_data)

print("历史销量数据 ", train_sales_data.shape)
print("车型搜索数据 ", train_search_data.shape)
print("汽车垂直媒体新闻评论数据和车型评论数据", train_user_reply_data.shape)


def clean_data():
    adcode_1, adcode_2 = train_sales_data['adcode'].unique(), train_search_data['adcode'].unique()  # 省份编码
    print(len(adcode_1), len(adcode_2))


    # print(train_sales_data.loc[(train_sales_data['model']=='3c974920a76ac9c1') & (train_sales_data['adcode']==310000), ['province','adcode','model','bodyType','regYear','regMonth']])
    # print(train_search_data.loc[(train_search_data['model']=='3c974920a76ac9c1') & (train_search_data['adcode']==310000), ['province','adcode','model','regYear','regMonth']])
    df = pd.DataFrame()

    df = train_sales_data.merge(train_search_data, how='inner', on=['province', 'adcode', 'model', 'regYear', 'regMonth'])
    print(df.shape)
    df.to_csv("./datasets/train/all_merge.csv", encoding='utf-8', header=True, index=False)


if __name__ == '__main__':
    clean_data()