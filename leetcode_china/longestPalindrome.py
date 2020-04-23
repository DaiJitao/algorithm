class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s:
            size = len(s)
            if size == 1:
                return s
            if size == 2:
                return s if s[0] == s[1] else s[0]
            maxStr = ""
            for i in range(size):
                left = i - 1  # 左边
                right = i + 1  # 右边
                while left >= 0 and right < size:
                    if s[left] == s[right]:
                        left -= 1
                        right += 1
                    else: # 考虑偶数huiwen
                        if  right + 1 < size and s[left] == s[right+1]:
                            left -= 1
                            right = right + 2
                        if left - 1 >= 0 and s[left-1] == s[right]:
                            left = left - 2
                            right += 1
                        else:
                            break

                left = left + 1

                if len(s[left:right]) > len(maxStr):
                    maxStr = s[left:right]

            return maxStr

if __name__ == '__main__':
    m = "asdsdddddddddddmabgbam"
    s = Solution()
    r = s.longestPalindrome(m)
    print(r)