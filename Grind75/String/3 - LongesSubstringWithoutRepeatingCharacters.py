#https://leetcode.com/problems/longest-substring-without-repeating-characters/description

def lengthOfLongestSubstring(s) -> int:
    max_length = 0
    aux = ""

    for c in s:
        #If character in aux, cut string from the ocurrency point forward
        if c in aux:
            aux = aux[aux.find(c)+1:]

        aux += c
        max_length = max(max_length, len(aux))

    return max_length

#abcabcbb -> 3 -> abc
#dvdf -> 3 -> vdf
#pwwkew -> 3 wke
s = "bbbcc"
print(lengthOfLongestSubstring(s))
