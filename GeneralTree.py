class TreeNode:
    def __init__(self, name) -> None:
        self.name = name
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)
        return

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self, level):
        spaces = ' '*self.get_level()*3
        prefix = spaces + "|__" if self.parent else ""
        if self.get_level() <= level:
            print(f'{prefix + self.name}')
            for i in self.child:
                i.print_tree(level)

def build_management_tree():
    # India Hierarchy
    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Banglore"))
    karnataka.add_child(TreeNode("Mysore"))

    india = TreeNode("India")
    india.add_child(gujarat)
    india.add_child(karnataka)

    # USA hierarchy
    new_jersey = TreeNode("New Jersey")
    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain view"))
    california.add_child(TreeNode("Palo Alto"))

    usa = TreeNode("USA")
    usa.add_child(new_jersey)
    usa.add_child(california)

    globals = TreeNode("Global")
    globals.add_child(india)
    globals.add_child(usa)

    return globals

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree(3)