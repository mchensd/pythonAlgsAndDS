# USES DIVIDE AND CONQUER

def exponent(x, y):  # returns x**y
    if y == 0:  # unrelated case
        return 1
    if y == 1:
        return x
    else:
        expo1 = y // 2
        expo2 = y - expo1
        x1 = exponent(x, expo1)
        x2 = exponent(x, expo2)

        x = x1 * x2
        return x

print(exponent(2,5))
print(exponent(3,6))
