# encoding=utf8
import sys
from typing import List


def isValie(word2size, word):
    return word in word2size


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        
        if len(wordDict) == 0 and len(s) == 0:
            return True
        if len(wordDict) == 0 and len(s) > 0:
            return False
        
        dp = [0] * (len(s) + 1)
        dp[0] = True if s[0] in wordDict else False
        for i in range(1, len(s)):
            dp[i] = True if s[:i+1] in wordDict else False
            j = 0
            while j < i:
                if dp[i]:
                    break
                p = s[j + 1: i+1]
                print(p)
                dp[i] = dp[j] and isValie(wordDict, p)
                j += 1
        print(dp)
        return dp[len(s)-1]

if __name__ == '__main__':
    s = "lovyou"
    wordDict = ["lov", "you"]
    r = Solution().wordBreak(s, wordDict)
    print(r)