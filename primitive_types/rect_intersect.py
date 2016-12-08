def do_intersect(c1, w1, h1, c2, w2, h2):  # two rectangles with corners c1, c2, widths w1, w2 and heights h1, h2
    x1 = c1[0]
    y1 = c1[1]
    x2 = c2[0]
    y2 = c2[1]
    max_x1 = x1 + w1
    max_x2 = x2 + w2
    min_x1 = x1
    min_x2 = x2


    w_range1 = set([i for i in range(x1, w1 + 1)])
    w_range2 = set([i for i in range(x2, w2 + 1)])

    if w_range1.isdisjoint(w_range2):
        return False

    h_range1 = set([i for i in range(y1, h1 + 1)])
    h_range2 = set([i for i in range(y2, h2 + 1)])

    if h_range1.isdisjoint(h_range2):
        return False
    return True




print(do_intersect((1,2), 3, 4, (5,3), 2, 4))
print(do_intersect((5,2), 10, 10, (6,3), 10, 10))