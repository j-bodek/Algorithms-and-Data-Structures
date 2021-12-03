


# Tree Data Structure

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        ret = "   " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1) 
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)
        

# Create first root node
tree = TreeNode('Drinks', [])
print(tree)

# Create new children nodes
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])

# Add children nodes
tree.addChild(cold)
tree.addChild(hot)
print(tree)

# Create new children nodes (for cold Node)
pepsi = TreeNode('Pepsi',[])
sprite = TreeNode('Sprite',[])

# Create new children nodes (for hot Node)
tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])

#Add children nodes to hot drink
hot.addChild(tea)
hot.addChild(coffee)
#Add children nodes to cold drink
cold.addChild(pepsi)
cold.addChild(sprite)

print('------------------FULL_TREE------------------')
print(tree)






































