from pprint import pprint


def demo1(bag_weight, weights, values):
    dp = [0] * (bag_weight + 1)
    dp[0] = 0
    for i in range(len(weights)):
        for j in range(bag_weight, weights[i]-1, -1):
            if weights[i] <= j:
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    print(dp)
    return dp[bag_weight]


if __name__ == '__main__':
    dp = demo1(4, weights=[1, 3, 4], values=[15, 20, 30])
    print(dp)
