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

    # Maybe try add_node function outside of Tree class. Maybe problem with referencing self.head...
    def add_node(self, added_to, val):
        node_to_add = Node(val)
        current_node = self.dfs(self.head, added_to)
        current_node.links.append(node_to_add) # current_node has no links? Figure this out


# TESTING

tree = Tree('Do you want to watch a serious or funny movie?')

print(tree.add_node('Do you want to watch a serious or funny movie?', 'Do you want to watch a true story? Enter Yes or No'))
print(tree.add_node('Do you want to watch a serious or funny movie?', 'Do you want to watch an action movie or a comedy?'))

print(tree.add_node('Do you want to watch a true story? Enter Yes or No', "I recommend Schindler's List"))
print(tree.add_node('Do you want to watch a true story? Enter Yes or No', 'I recommend 2001: A Space Odyssey'))
print(tree.add_node('Do you want to watch an action movie or a comedy?', 'I recommend Rush Hour'))
print(tree.add_node('Do you want to watch an action movie or a comedy?', 'I recommend Step Brothers'))