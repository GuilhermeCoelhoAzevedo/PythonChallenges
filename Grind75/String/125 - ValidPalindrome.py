#https://leetcode.com/problems/valid-palindrome/description
def isPalindrome(s):
    phrase = ""

    for c in s.lower():
        if c.isalnum():
            phrase += c

    return phrase == phrase[::-1]

#s = "0P"
#s = "ab_a"
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

# c.isalnum() - Filter alphanumeric characters a-z 0-9
# c.isdigit() - Filter numbers 0 - 9
# c.isalpha() - Filter a-z
