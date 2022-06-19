def is_palindrome(s: str, start: int, end: int) -> bool:
    i: int = start
    j: int = end
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


res = []
path = []


def backtracking(s, startIndex):
    if startIndex >= len(s):
        res.append(path[:])
        return

    for i in range(startIndex, len(s)):
        if is_palindrome(s, startIndex, i):
            path.append(s[startIndex:i + 1])
            backtracking(s, i + 1)
            path.pop()
        else:
            continue



s = "aabaa"
backtracking(s, 0)
print(res)

