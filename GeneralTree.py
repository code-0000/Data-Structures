class Tree:
    def __init__(self, data) -> None:
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)
        return
    
    def print_tree(self):
        print(self.data)
        for self.child