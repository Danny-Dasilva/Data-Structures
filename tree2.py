class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def add(self, val):
        if val < self.val:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.add(val)
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.add(val)
    def sort(self):
        a = []
        b = [self.val]
        c = []
        if self.left:
            a = self.left.sort()
        if self.right:
            c = self.right.sort()
        return a+b+c
    def str(self):
        a, b = "", ""
        if self.left:
            a = self.left.str()
        if self.right:
            b = self.right.str()
        return "({}, {}, {})".format(self.val, a, b)
def tree_sort(s):
    node = Node(s[0])
    for val in s[1:]:
        node.add(val)
    return node.sort()

l=[123, 48, 23, 100, 56,2, 10, 273, 108, 398, 100, 2651, 12]
print(tree_sort(l))
