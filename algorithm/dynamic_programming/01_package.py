from pprint import pprint


def demo1(max_weight: int, weights, values):
    '''

    :param max_weight: 背包最大重量
    :param weights:
    :param values:
    :return:
    '''
    inner = [0] * len(weights)
    dp = [[0] * (max_weight + 1) for _ in inner]
    for i in range(len(weights)):
        dp[i][0] = 0
    for i in range(1, max_weight + 1):
        weight = i
        if weight >= weights[0]:
            dp[0][i] = values[0]
        else:
            dp[0][i] = 0

    for i in range(1, len(weights)):
        for j in range(1, max_weight + 1):
            if j >= weights[i]:
                print(i, j)
                print(values[i])
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + values[i])
            else:
                dp[i][j] = dp[i - 1][j]


    return dp[i][j]
'''
容量为j的背包，所背物品最大价值为dp[j]
'''
def demo1_version2(max_weight, weights, values):
    dp = [0] * (max_weight+1)
    dp[0] = 0
    # 放物品
    dp[j] = d[j-weights[i]] + values[i]
    # 不放
    dp[j] = dp[j-weights[i]]




if __name__ == '__main__':
    dp = demo1(4, weights=[1, 3, 4], values=[15, 20, 30])
    print(dp)
