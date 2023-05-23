from typing import List, Optional


def check(sub_str, s3):
    n = len(s3)
    m = len(sub_str)
    i = 0
    all_str = list(s3)
    del_count = 0
    isFlag = False  # sub_str 是否全部用了
    while i < n:
        if all_str[i] == sub_str[0]:
            sub_str = sub_str[1:]
            all_str[i] = 'del'
            del_count += 1

        if len(sub_str) == 0:
            isFlag = True
            break

        i += 1

    for i in range(del_count):
        all_str.remove('del')

    return ''.join(all_str), isFlag


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if s1 is None or s2 is None or s3 is None:
            return None

        if s1 == s2 and s3 == '' and s1 == '':
            return True

        temp_s2, isFlag = check(s1, s3)
        if isFlag:
            if temp_s2 == s2:
                return True

        return False


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if s1 is None or s2 is None or s3 is None:
            return None

        if s1 == s2 and s3 == '' and s1 == '':
            return True

        """
        dp[i][j] 代表S1[:i]和s2[:1]能否组合成s3[:i+j],可以即为True,不可以即为False
        dp[0][0] 什么都不取，True
        
        dp[1][1] = 
        if s1[:1]+s2[:1] == s3[:i+j] or s2[:1] + s1[:1] == s3[:i+j]:
            True
        else:
            False
        """
        n1 = len(s1) # 行数
        n2 = len(s2)
        if n1 + n2 != len(s3):
            return False

        inner = [0] * (n2 + 1)
        dp = [ inner[:] for _ in range(n1+1)]
        print(dp)
        dp[0][0] = True


if __name__ == '__main__':
    s1 = 'aabbcg'
    s2 = 'bcghdu'
    s3 = 'bcghduaabbcg'

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    plus, isFlag = check(s1, s3)
    print(plus, isFlag)
    res = Solution().isInterleave(s1, s2, s3)
    print(res)
