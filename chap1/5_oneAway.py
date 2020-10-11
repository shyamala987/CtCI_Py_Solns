'''
Given two strings, check if they are one edit away
An edit can be an insert, a removal or a replacement of a character
pale - bale True
pale - pal True
pale - pales True
pale - bake False
'''

def checkOneAway(str1, str2):

    def _checkOneInsert(str1, str2):
        if len(str2) - len(str1) != 1:
            return False
        ops = 0
        first, sec = 0, 0
        while first < len(str1) and sec < len(str2):
            if str1[first] == str2[sec]:
                first += 1
                sec += 1
            else:
                sec += 1
                ops += 1

        return (ops == 1) or (first == len(str1) and sec == len(str2)-1)

    def _checkOneRemove(str1, str2):
        return _checkOneInsert(str2, str1)

    def _checkOneRepl(str1, str2):
        if len(str1) != len(str2):
            return False

        ops = 0
        first, sec = 0, 0
        while first < len(str1) and sec < len(str2):
            if str1[first] != str2[sec]:
                ops += 1
            first += 1
            sec += 1

        return ops == 1

    return _checkOneInsert(str1, str2) or _checkOneRemove(str1, str2) or _checkOneRepl(str1, str2)

str1, str2 = "pale", "ple"
print(checkOneAway(str1, str2))