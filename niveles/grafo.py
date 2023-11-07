class Node:
    def __init__(self, html):
        self.data = html
        self.left = None
        self.right = None

    def addNode(self, html):
        if self.left is None:
            self.left = Node(html)
        elif self.right is None:
            self.right = Node(html)
        else:
            self.left.addNode(html)
