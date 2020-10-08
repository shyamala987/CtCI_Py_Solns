'''
Given a string, determine if it's the permutation of a palindrome
'''
'''

ex: madma ==> True
tact coa ==> True
acac ==> True

'''

from collections import Counter


def permPal(input):
    odds = 0
    ctr = Counter()
    for i in input:
        if i != ' ':
            ctr[i.lower()] += 1
    print(ctr)
    for k, v in ctr.items():
        if v % 2 != 0:
            odds += 1

        if odds > 1:
            return False

    return odds <= 1

print(permPal("madma"))
print(permPal("Tact Coa"))
print(permPal("addffa"))
print(permPal("acd"))