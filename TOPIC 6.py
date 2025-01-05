class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2, self.data)
        for child in self.children:
            child.display(level + 1)

print('Hierarchical data\n__________________')
root = TreeNode("Building")
floor1 = TreeNode("Floor 1")
floor2 = TreeNode("Floor 2")
room1 = TreeNode("Room 101")
room2 = TreeNode("Room 102")
room3 = TreeNode("Room 201")
room4 = TreeNode("Room 202")

floor1.add_child(room1)
floor1.add_child(room2)
floor2.add_child(room3)
floor2.add_child(room4)
root.add_child(floor1)
root.add_child(floor2)

root.display()
