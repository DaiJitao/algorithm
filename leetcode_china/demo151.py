def demo151(sentence):
    sentence = sentence.strip()
    n = len(sentence)
    if n <= 1:
        return None
    words = sentence.split(' ')
    print(words)
    return ' '.join(words[::-1])

if __name__ == '__main__':
    s = "I like china"
    res = demo151(s)
    print(res)
