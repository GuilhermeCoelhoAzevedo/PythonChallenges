#https://leetcode.com/problems/add-binary/description

def addBinary(a, b):
    return bin(int(a,2) + int(b,2))[2:]

a = "1010"
b = "1011"

print(addBinary(a, b))