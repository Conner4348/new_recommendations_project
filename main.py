# Recommendations Project for codecademy

class Node:

    def __init__(self, val):
        self.val = val
        self.links = []

    def get_val(self):
        return self.val
    
    def get_links(self):
        return self.links
    

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

    def add_node(self, added_to, val):
        node_to_add = Node(val)
        current_node = self.dfs(self.head, added_to)
        current_node.links.append(node_to_add)
        return


# TESTING

tree = Tree(0)
print(tree.add_node(0, 1))