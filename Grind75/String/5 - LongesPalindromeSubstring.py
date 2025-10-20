#https://leetcode.com/problems/longest-palindromic-substring/description

def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    longest = s[0]

    for i in range(0, len(s)):
        aux = s[i]

        for j in range(i + 1, len(s)):
            aux += s[j]

            if aux == aux[::-1]:
                if len(aux) > len(longest):
                    longest = aux


    return longest

s = ""
print(longestPalindrome(s))