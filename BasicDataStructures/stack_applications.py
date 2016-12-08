from stack import Stack


def par_checker(statement):
    s = Stack()
    for char in statement:
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.isEmpty():
                return False
            s.pop()
    return s.isEmpty()

def closed_checker(statement):
    s = Stack()
    for char in statement:
        if char in "({[":
            s.push(char)
        elif char in ")}]":
            if s.isEmpty():
                return False
            top = s.pop()
            ending = {'{': '}', '(': ')', '[': ']'}
            if ending[top] != char:
                return False
    return s.isEmpty()
"""print(closed_checker("({}[()])"))
print(closed_checker("((){[}])"))
"""
def to_binary(num):
    s = Stack()
    if num == 0:
        return 0
    while num > 0:
        rem = num % 2
        s.push(rem)
        num //= 2
    ret_string = ""
    while not s.isEmpty():
        ret_string += str(s.pop())
    return ret_string

print(to_binary(256))
