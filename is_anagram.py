import string

def is_anagram(s1, s2):
    letters = string.ascii_letters[0:26]
    checker1 = dict()
    checker2 = dict()
    for i in letters:
        checker1[i] = 0
        checker2[i] = 0

    for l in s1:
        checker1[l] += 1
    for l in s2:
        checker2[l] += 1

    return True if checker1 == checker2 else False

print(is_anagram('heart', 'earth'))
print(is_anagram('jump', 'pump'))

