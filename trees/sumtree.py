import queue, sys
q = queue.Queue()

sys.path.append('C:/Users/Michael/documents/python/algorithms-datastructures/basicdatastructures')
from stack import Stack
from queue import Queue

def sumtree(l):
    sum = 0
    for i in range(len(l)):
        if not isinstance(l[i], list):
            sum += l[i]
        else:
            sum += sumtree(l[i])
    return sum

def queuesum(l):
    tot = 0
    '''
    for i in l:
        if not isinstance(i, list):
            tot += i
        else:
            l.extend(i)
            '''
    while l:
        item = l.pop()
        if not isinstance(item, list):
            tot += item
        else:
            l.extend(item)
    return tot

print(sumtree([1,[2,[3,[4,[5]]]]]))
print(queuesum([1,[2,[3,[4,[5]]]]]))
print(queuesum([[[[1],2],3],4]))