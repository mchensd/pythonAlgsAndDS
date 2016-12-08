class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, t):
        bTree = BinaryTree(t)
        if self.left == None:
            self.left = bTree
        else:
            bTree.left = self.left
            self.left = bTree

    def insertRight(self, t):
        bTree = BinaryTree(t)
        if self.right == None:
            self.right = bTree
        else:
            bTree.right = self.right
            self.right = bTree

    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setKey(self, obj):
        self.key = obj
    def getKey(self):
        return self.key

def inOrderWalk(tree):
    if tree:
        inOrderWalk(tree.left)
        print(tree.key)
        inOrderWalk(tree.right)

def treeSearch(node, key):
    if not node:  # we are at the end
        return False
    if node.key == key:
        return True
    if node.key > key:  # if the right side is too big...
        return treeSearch(node.left, key)  # search the left side
    elif node.key < key:
        return treeSearch(node.right, key)

def minimum(node):
    while node.left is not None:
        node = node.left
    return node.key

def maximum(node):
    while node.right is not None:
        node = node.right
    return node.key


if __name__ == '__main__':
    r = BinaryTree(5)
    r.insertLeft(3)
    r.insertRight(7)
    l = r.getLeft()
    l.insertLeft(2)
    l.insertRight(4)
    inOrderWalk(r)
    print(treeSearch(r, 7))
    print(treeSearch(r,10))
    print(minimum(r))
    print(maximum(r))
    '''
    r = BinaryTree('a')
    print(r.getKey())
    print(r.getLeft())
    r.insertLeft('b')
    print(r.getLeft())
    print(r.getLeft().getKey())
    r.insertRight('c')
    print(r.getRight())
    print(r.getRight().getKey())
    r.getRight().setKey('hello')
    print(r.getRight().getKey())

    '''
