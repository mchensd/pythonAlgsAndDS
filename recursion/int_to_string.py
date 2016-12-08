def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return reverse_string(s[-1]) + reverse_string(s[0:-1])

def is_palindrome(s):
    if len(s) == 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        return is_palindrome(s[1:-1])

