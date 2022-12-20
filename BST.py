class BinarySearchTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left =None
        self.right = None

    def insert(self, data):
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BinarySearchTree(data)
            return
        elif self.data > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BinarySearchTree(data)
            return
        else:
            return

    def print_inorder(self):
        element = []
        if self.left:
            element += self.left.print_inorder()
        element.append(self.data)
        if self.right:
            element += self.right.print_inorder()
        return element

    def search(self, data):
        if self.data == data:
            return True
        
        if self.data < data:
            if self.right:
                return self.right.search(data)
            else:
                return False
        
        if self.data > data:
            if self.left:
                return self.left.search(data)
            else:
                return False

    def find_max(self):
        val = self.print_inorder()
        return val[-1]

    def find_min(self):
        val = self.print_inorder()
        return val[0]

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            
            min_val = self.left.find_max()
            self.data = min_val
            self.left = self.left.delete(min_val)

        return self



def BST(elements):
    b = BinarySearchTree(elements[0])
    for i in elements:
        b.insert(i)
    list = b.print_inorder()
    print(list)
    return b

if __name__ == '__main__' :
    elements = [53,87,0,67,89,92,34,16,72]
    tree = BST(elements)
    tree.delete(72)
    tree.delete(53)
    print(tree.print_inorder())
    print(tree.find_max())