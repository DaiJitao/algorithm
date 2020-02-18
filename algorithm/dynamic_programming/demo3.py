

def max_profit(prices):

    n = len(prices)
    r = [0]*(n+1)
    r[1] = prices[1]
    for i in range(2, n+1):
        r[i] = max(prices[i], r_p(i, r[:i-1]))
    return r[n]


def r_p(n, r):
    res = []
    for i in range(1,n):
        res.append(r[i] + r[n-1])
    return max(res)
