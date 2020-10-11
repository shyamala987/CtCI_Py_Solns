'''
Write an algorithm to replace all spaces in a string with %20

'''


def urlify(input, l):
    return '%20'.join([s for s in input.strip().split()])


print(urlify("Mr John Smith  ", 13))
print(urlify("   a  b ", 1))
print(urlify("   a   ", 1))
