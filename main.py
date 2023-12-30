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
            if path_found is not None:
               return path_found
        return None
    
    def extend(self, root, val):
        find = self.dfs(root, val)
        return find


def take_input():
    choice = input()
    try:
        int(choice)
    except:
        print('Please select either 1 or 2')
        take_input()
    else:

        if int(choice) != 1 and int(choice) != 2:
            print('Please select either 1 or 2')
            take_input()
        
    return choice


# TESTING

tree = Tree('Do you want to watch a serious or funny movie?')

print(tree.add_node('Do you want to watch a serious or funny movie?', 'Do you want to watch a true story? Enter Yes or No'))
print(tree.add_node('Do you want to watch a serious or funny movie?', 'Do you want to watch an action movie or a comedy?'))

print(tree.add_node('Do you want to watch a true story? Enter Yes or No', "I recommend Schindler's List"))
print(tree.add_node('Do you want to watch a true story? Enter Yes or No', 'I recommend 2001: A Space Odyssey'))
print(tree.add_node('Do you want to watch an action movie or a comedy?', 'I recommend Rush Hour'))
print(tree.add_node('Do you want to watch an action movie or a comedy?', 'I recommend Step Brothers'))