#https://leetcode.com/problems/valid-anagram/description

def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))