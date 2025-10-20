#https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    openStack = []
    bracketPairs = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    for e in s:
        if e in bracketPairs:
            openStack.append(e)
        else:
            if len(openStack) == 0 or not e == bracketPairs[openStack.pop()]:
                return False

    return True

s = "("
print(isValid(s))