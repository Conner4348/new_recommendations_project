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
            if path_found is not None:
               return path_found
        return None

    # Maybe try add_node function outside of Tree class. Maybe problem with referencing self.head...
    def add_node(self, added_to, val):
        node_to_add = Node(val)
        current_node = self.dfs(self.head, added_to)
        current_node.links.append(node_to_add) # current_node has no links? Figure this out


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

tree = Tree('Do you want to watch a serious or funny movie? Enter 1 or 2')

tree.add_node('Do you want to watch a serious or funny movie? Enter 1 or 2', 'Do you want to watch a true story? Enter 1 (Yes) or 2 (No)')
tree.add_node('Do you want to watch a serious or funny movie? Enter 1 or 2', 'Do you want to watch an action movie or a comedy? Enter 1 or 2')

tree.add_node('Do you want to watch a true story? Enter 1 (Yes) or 2 (No)', "I recommend Schindler's List")
tree.add_node('Do you want to watch a true story? Enter 1 (Yes) or 2 (No)', 'I recommend 2001: A Space Odyssey')
tree.add_node('Do you want to watch an action movie or a comedy? Enter 1 or 2', 'I recommend Rush Hour')
tree.add_node('Do you want to watch an action movie or a comedy? Enter 1 or 2', 'I recommend Step Brothers')

print('')
print(
"""
 __  __            _        _____                                                   _       _   _                 
|  \/  |          (_)      |  __ \                                                 | |     | | (_)                
| \  / | _____   ___  ___  | |__) |___  ___ ___  _ __ ___  _ __ ___   ___ _ __   __| | __ _| |_ _  ___  _ __  ___ 
| |\/| |/ _ \ \ / / |/ _ \ |  _  // _ \/ __/ _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / _` |/ _` | __| |/ _ \| '_ \/ __|
| |  | | (_) \ V /| |  __/ | | \ \  __/ (_| (_) | | | | | | | | | | |  __/ | | | (_| | (_| | |_| | (_) | | | \__ \ 
|_|  |_|\___/ \_/ |_|\___| |_|  \_\___|\___\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__,_|\__,_|\__|_|\___/|_| |_|___/
                                                                                                                   
                                                                                                                
"""
)


current = tree.head
while len(current.links) > 0:
    print(current.get_val())
    dec = take_input()
    print(int(dec))
    current = current.links[int(dec)-1]
print(current.get_val())