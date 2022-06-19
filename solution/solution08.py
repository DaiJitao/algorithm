class Solution:
    def myAtoi(self, s: str) -> int:
        minp = -2**31
        maxp = 2**31 - 1
        numbers = [str(i) for i in range(10)]
        t_s = s.lstrip()
        n = len(t_s)
        if n == 1:
            return int(t_s)

        isStart = True
        res = ''
        i = 0
        while i < n:
            if t_s[i] not in numbers and t_s[i] != '-':
                i += 1
                continue

            if isStart and t_s[i] == '-' and t_s[i+1] in numbers:
                isStart = False
                res += t_s[i:i+2]
                i += 1

            elif isStart and  t_s[i] == '+' and t_s[i+1] in numbers:
                isStart = False
                res += t_s[i:i+2]
                i += 1

            elif isStart and t_s[i] in numbers:
                isStart = False
                res += t_s[i]
            else:
                if t_s[i] in numbers:
                    res += t_s[i]
                else:
                    break

            i += 1

        t = int(res)
        if t < minp:
            return minp
        if t > maxp:
            return maxp

        return t

if __name__ == '__main__':
    s = "words and 987"
    res = Solution().myAtoi(s)
    print(res)

