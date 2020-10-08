'''

write an algorithm to check if all characters in a string are unique. Do it without using extra space?

'''

def isUnique(string):
    res = [False] * 26
    for ch in string:
        if res[ord(ch)-ord('a')]:
            return False
        res[ord(ch)-ord('a')] = True
    return True

print(isUnique('abcdAh'))