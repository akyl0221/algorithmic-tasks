"""https://www.algoexpert.io/questions/bst-construction"""


# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left:
               self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left:
                return self.left.contains(value)
            return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            return False
        return True

    def remove(self, value):
        if not self:
            return self

        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if not self.right and not self.left:
                return None
            elif not self.left:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return self
            elif not self.right:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left
                return self
            else:
                successor = self.right.in_order_successor()
                self.value = successor.value
                self.right = self.right.remove(successor.value)
        return self

    def in_order_successor(self):
        while self.left:
            self = self.left
        return self
