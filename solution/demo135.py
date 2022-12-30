from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1

        n = len(ratings)
        right = [1] * n
        left = right[:]
        temp = [0] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(n - 1, -1, -1):
            if ratings[i - 1] > ratings[i]:
                right[i - 1] = right[i] + 1

            temp[i] = max(right[i], left[i])

        return sum(temp)


if __name__ == '__main__':
    arr = [1, 3, 4, 5, 2, 1, 0]
    arr = [6, 5, 4, 3, 2, 3, 2, 2, 1]
    arr = [0, 1, 2, 3, 2, 1]
    arr = [1, 2, 87, 87, 87, 2, 1]
    arr = [2, 2]
    res = Solution().candy(arr)
    print(res)
