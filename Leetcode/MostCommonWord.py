import re

def mostCommonWord(paragraph, banned):
    a = re.split(r'\W+', paragraph.lower())
    b = []

    for e in a:
        if e not in banned:
            b.append(e)

    return max(b, key=b.count)

paragraph = "a, a, a, a, b,b,b,c, c".strip()
banned = ["a"]

print(mostCommonWord(paragraph, banned))
