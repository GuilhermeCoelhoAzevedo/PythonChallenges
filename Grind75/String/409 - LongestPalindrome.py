#https://leetcode.com/problems/longest-palindrome/description

from collections import Counter

def longestPalindrome(s) -> int:
    #Gets frequency of each character
    d = Counter(s)
    count = 0
    flag = True

    for e in d.values():
        #Even numbers can always build palindromes
        if e % 2 == 0:
            count += e
        else:
            #Reduce 1 from odd number to become even number and add to count
            count += e - 1

            #Palindromes can have one even number, so this block can be true once
            if flag:
                count +=1
                flag = False

    return count

#s = "aaadddddeeeee" #ddeeaaaeedd
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
print(longestPalindrome(s))