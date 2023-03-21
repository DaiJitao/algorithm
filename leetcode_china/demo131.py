
def is_huiwen(s):
    if len(s) == 1:
        return True
    if s == s[::-1]:
        return True

    return False

def is_path(path):
    for s in path:
        if not is_huiwen(s):
            return False

    return True


def demo131(s):
    if not s or len(s).strip() == 0:
        return []

    n = len(s)
    path = []

    def backtracing(start_index, path):

        if not is_path(path):
            return

        for i in range(start_index, n):
            sub_str = s[:i + 1]
            path.append(sub_str)
            backtracing(start_index+1, path)
            path.pop()

    start_index = 0
    backtracing(start_index, path)

if __name__ == '__main__':
    pass