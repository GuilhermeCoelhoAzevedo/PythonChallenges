#https://neetcode.io/problems/string-encode-and-decode

class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""

        for s in strs:
            result+= str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> list[str]:
        result = []
        j = 0
        i = 0

        while i < len(s):
            if s[i] != "#":
                i +=1
                continue

            #Gets word length
            length = int(s[j:i])
            #Gets word
            word = s[i+1: i+1 + length]
            #Append word to result
            result.append(word)

            #Sets for next word
            j = i+1 + length
            i = j

        return result

input = ["neet", "code", "love", "you"]
solution = Solution()
encode = solution.encode(input)
print("Encode: " + encode)
decode = solution.decode(encode)
print("Decode: " + str(decode))

