# Recommendations Project for codecademy

class Node:

    def __init__(self, val):
        self.val = val
        self.children = []
    
    def add_node(self, child):
        self.children.append(child)
    

class Tree:

    def __init__(self, val):
        self.head = Node(val)

    def dfs(self, root, val, path=()):
        path += (root,)
        if root.val == val:
            return path[-1]
        for child in root.links:
            path_found = self.dfs(child, val, path)
            if path is not None:
               return path_found
        return None
    
    def extend(self, root, val):
        find = self.dfs(root, val)
        return find


# TESTING

tree = Tree('root')
# HUH?
print(tree.extend('root', 'root'))