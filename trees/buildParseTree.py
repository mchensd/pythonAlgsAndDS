from Algs.BasicDataStructures import stack
from Algs.trees import BinTreeNode

def buildParseTree(expr):
    expList = expr.split()
    pStack = stack.Stack()
    eTree = BinTreeNode.BinaryTree('')
    pStack.push(eTree)  # parent tree

    eTree.insertLeft('')
    currentTree = eTree.getLeft()

    for i in expList:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeft()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setKey(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setKey(i)
            pStack.push(currentTree)
            currentTree.insertRight('')
            currentTree = currentTree.getRight()
        elif i == ')':
            parent = pStack.pop()
            currentTree = parent
    return eTree

p = buildParseTree(""
                   "3 + 5 * 3")
print(p.getLeft().getKey())
print(p.getKey())
print(p.getRight().getKey())

