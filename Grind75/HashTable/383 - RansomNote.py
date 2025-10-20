#https://leetcode.com/problems/ransom-note/description/

from collections import Counter

def canConstruct(ransomNote, magazine):

    #Creating dictionary with magazine letters count
    d = Counter(magazine)

    #Checking if ransonNote can be built from magazine letters
    for l in ransomNote:
        if l in d and d[l] > 0:
            d[l] -=1
        else:
            return False

    return True

ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote, magazine))

#Optimized answer:
"""
def canConstruct(ransomNote, magazine):
    st1, st2 = Counter(ransomNote), Counter(magazine)

    if st1 & st2 == st1:
        return True
    return False
"""