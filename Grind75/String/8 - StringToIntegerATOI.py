#https://leetcode.com/problems/string-to-integer-atoi/description

def myAtoi(s: str):
    result = ""
    flag = True

    for c in s.strip():
        if c.isdigit():
            result += c
            flag = False
        elif (c == "-" or c == "+") and flag:
            result += c
            flag = False
        else:
            break

    #Avoid exceptions when converting to int
    if len(result) == 0 or result == "-" or result=="+":
        return 0

    # Rounding
    if int(result) < -(2 ** 31):
        return -(2 ** 31)
    elif int(result) > (2 ** 31 - 1):
        return (2 ** 31 - 1)
    else:
        return int(result)

s = "-91283472332"
print(myAtoi(s))
