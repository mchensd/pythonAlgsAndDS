from deque import Deque


def palindrome_checker(s):
    d = Deque()

    for char in s:
        d.addFront(char)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False
    return True

print(palindrome_checker('1335331'))
print(palindrome_checker('22334433'))
print(palindrome_checker("ffaaddaaff"))