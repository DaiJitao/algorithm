from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs:
            if len(strs) == 1:
                return strs[0]
            str_one = strs[0]
            str_size = len(str_one)
            result = ""
            flag = True
            for i in range(str_size):
                c = str_one[i]
                for temp in strs[1:]:
                    if (i + 1) > len(temp) or c != temp[i]:
                        flag = False
                if flag:
                    result += c
                else:
                    break

            return result
        return ""


if __name__ == '__main__':
    strs = ["cf","cf","c"]
    s = Solution()
    print(s.longestCommonPrefix(strs))