import copy

"""
参考：https://leetcode.cn/problems/substring-with-concatenation-of-all-words/solution/30-chuan-lian-suo-you-dan-ci-de-zi-chuan-bvy9/
"""

from typing import List


class Solution:

    def isEval(self, dic1, dic2):

        print("words_dict={}".format(dic1))
        print("res_dic:{}\n".format(dic2))


        if len(dic1) != len(dic2):
            return False


        for word, num in dic1.items():
            if dic2.get(word) != num:
                return False

        return True

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = {}
        for i in words:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        if len(words) == 0 or len(s) == 0:
            return []

        wordlen = len(words[0])
        n = len(s)
        if wordlen > n:
            return []

        temp = {}
        wordlen = len(words[0])
        wordNum = len(words)
        i = 0
        res = []
        while i + wordlen * wordNum <= n:
            substring = s[i: i + wordlen * wordNum]
            j = 0
            while j < wordlen * wordNum:
                word = substring[j:j + wordlen]
                if word in temp:
                    temp[word] += 1
                else:
                    temp[word] = 1
                j += wordlen

            if self.isEval(dic, temp):
                res.append(i)

            i += 1
            temp.clear()

        return res


if __name__ == '__main__':
    solution = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]

    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]

    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]


    res = solution.findSubstring(s, words)
    print(res)
