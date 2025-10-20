#https://neetcode.io/problems/permutation-string

def checkInclusion(s1, s2):
    i = 0
    s1 = sorted(s1)

    while i < len(s2):
        aux = ""
        j = i
        #Look for all letters of permutation
        while j < len(s2) and s2[j] in s1:
            aux += s2[j]

            #When possible permutation achieves proper length, compare to s1
            if len(aux) == len(s1):
                if sorted(aux) == s1:
                    return True
                else:
                    break

            j+=1

        i+=1

    return False

s1 = "abc"
s2 = "lecabee"

print(checkInclusion(s1, s2))